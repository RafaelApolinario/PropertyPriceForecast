# Usa a imagem oficial do Python
FROM python:3.9

# Define o diretório de trabalho no container
WORKDIR /app

# Copia as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto para dentro do container
COPY src/ ./src/
COPY models/ ./models/
COPY data/ ./data/
COPY notebooks/ ./notebooks/

# Expõe as portas da API Flask e do Jupyter
EXPOSE 5000
EXPOSE 8888

# Comando que inicia JupyterLab + Flask API
CMD ["sh", "-c", "jupyter lab --notebook-dir=/app/notebooks --ip=0.0.0.0 --allow-root & python src/api/app.py"]
