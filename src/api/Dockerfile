# Usa a imagem oficial do Python
FROM python:3.9

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos necessários para o container
COPY src/api/requirements.txt ./
COPY src/api/app.py ./
COPY models/best_model.pkl ./models/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exposição da porta 5000
EXPOSE 5000

# Comando para rodar a API
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
