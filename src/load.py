import sqlite3
import pandas as pd
import os

def load_data_to_sql(input_filename="clean_weather_data.csv", db_filename="goldenergy_warehouse.db"):
    """
    Carrega os dados transformados para uma base de dados relacional (SQLite),
    criando a tabela caso não exista.
    """
    print("A iniciar o carregamento (Load) para a base de dados SQL...")

    # 1. Definir caminhos
    base_dir = os.path.dirname(os.path.dirname(__file__))
    input_path = os.path.join(base_dir, 'data', input_filename)
    db_path = os.path.join(base_dir, 'data', db_filename)

    # 2. Ler os dados limpos
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        print(f"Erro: Ficheiro {input_path} não encontrado. Corre o transform.py primeiro.")
        return

    # 3. Conectar à base de dados (Cria o ficheiro .db se não existir)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 4. Criar o esquema da tabela (DDL - Data Definition Language)
    # Isto mostra aos entrevistadores que sabes definir tipos de dados em SQL
    create_table_query = """
    CREATE TABLE IF NOT EXISTS daily_weather (
        date TEXT PRIMARY KEY,
        temp_max REAL,
        temp_min REAL,
        temp_avg REAL,
        total_radiation REAL
    );
    """
    cursor.execute(create_table_query)

    # 5. Inserir os dados (DML)
    # O Pandas tem uma função nativa maravilhosa para enviar DataFrames para SQL
    try:
        # if_exists='replace' garante que se correres o script 2 vezes, ele atualiza a tabela
        df.to_sql('daily_weather', conn, if_exists='replace', index=False)
        print(f"Sucesso! {len(df)} registos inseridos na tabela 'daily_weather'.")
    except Exception as e:
        print(f"Erro ao inserir dados na base de dados: {e}")

    # 6. Fechar a conexão
    conn.close()
    print(f"Base de dados guardada em: {db_path}")

if __name__ == "__main__":
    load_data_to_sql()