import requests
import pandas as pd
from datetime import datetime, timedelta
import os

def fetch_weather_data(lat, lon, start_date, end_date):
    """
    Extrai dados meteorológicos horários da API Open-Meteo.
    """
    print(f"A iniciar extração de dados de {start_date} até {end_date}...")
    
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": "temperature_2m,direct_radiation",
        "timezone": "Europe/London"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Verifica se houve algum erro HTTP
        data = response.json()
        
        # O JSON devolve um dicionário dentro da chave 'hourly'. 
        # O Pandas converte isto perfeitamente para um DataFrame.
        df = pd.DataFrame(data['hourly'])
        print(f"Extração concluída com sucesso! Foram extraídas {len(df)} linhas.")
        return df

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return None

def save_raw_data(df, filename="raw_weather_data.csv"):
    """
    Guarda os dados brutos na pasta 'data' para posterior transformação.
    """
    # Garante que a pasta data existe, subindo um nível a partir de src/
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    file_path = os.path.join(data_dir, filename)
    df.to_csv(file_path, index=False)
    print(f"Dados brutos guardados em: {file_path}")

if __name__ == "__main__":
    # Definir os parâmetros (Coordenadas do Porto e últimos 30 dias)
    latitude_porto = 41.1496
    longitude_porto = -8.611
    
    data_fim = datetime.now().date()
    data_inicio = data_fim - timedelta(days=30)
    
    # Executar o pipeline de extração
    df_raw = fetch_weather_data(
        lat=latitude_porto, 
        lon=longitude_porto, 
        start_date=data_inicio.strftime('%Y-%m-%d'), 
        end_date=data_fim.strftime('%Y-%m-%d')
    )
    
    if df_raw is not None:
        save_raw_data(df_raw)