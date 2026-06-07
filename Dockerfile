# Usar uma imagem oficial e leve do Python
FROM python:3.9-slim

# Definir a pasta de trabalho dentro do contentor
WORKDIR /app

# Copiar o ficheiro de dependências e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do teu código e dados para dentro do contentor
COPY src/ ./src/
COPY data/ ./data/

# O comando que o contentor vai executar quando arrancar (Corre o pipeline todo!)
CMD ["sh", "-c", "python src/extract.py && python src/transform.py && python src/load.py"]