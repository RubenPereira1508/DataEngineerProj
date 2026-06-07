import pandas as pd
import os

def transform_weather_data(input_filename="raw_weather_data.csv", output_filename="clean_weather_data.csv"):
    """
    Lê os dados brutos, aplica as regras de negócio (agregação diária) 
    e guarda o resultado limpo.
    """
    print("A iniciar a transformação dos dados...")
    
    # 1. Definir os caminhos dos ficheiros
    base_dir = os.path.dirname(os.path.dirname(__file__))
    input_path = os.path.join(base_dir, 'data', input_filename)
    output_path = os.path.join(base_dir, 'data', output_filename)
    
    # 2. Carregar os dados
    try:
        df = pd.read_csv(input_path)
        print(f"Dados brutos carregados: {len(df)} linhas.")
    except FileNotFoundError:
        print(f"Erro: O ficheiro {input_path} não foi encontrado.")
        return

    # 3. Limpeza e Tipagem (Converter a coluna 'time' para formato Datetime real)
    df['time'] = pd.to_datetime(df['time'])
    
    # Extrair apenas a data (sem as horas) para podermos agrupar
    df['date'] = df['time'].dt.date
    
    # 4. Agregação / Regras de Negócio
    # Vamos agrupar por dia e calcular métricas úteis para o setor da energia
    df_daily = df.groupby('date').agg(
        temp_max=('temperature_2m', 'max'),
        temp_min=('temperature_2m', 'min'),
        temp_avg=('temperature_2m', 'mean'),
        total_radiation=('direct_radiation', 'sum') # Importante para energia solar
    ).reset_index()

    # Arredondar os valores para 2 casas decimais para manter o ficheiro limpo
    df_daily = df_daily.round(2)

    # 5. Guardar (Load)
    df_daily.to_csv(output_path, index=False)
    print(f"Transformação concluída com sucesso!")
    print(f"Dados agregados (diários) guardados em: {output_path}")
    print("\nResumo dos dados limpos:")
    print(df_daily.head()) # Mostra as primeiras 5 linhas no terminal

if __name__ == "__main__":
    transform_weather_data()