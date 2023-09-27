# Use a imagem base do Python
FROM python:3.8-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o seu código, requirements.txt e o modelo para o contêiner
COPY . .

# Instale a biblioteca libgomp1
RUN apt-get update && apt-get install -y libgomp1

# Instale as dependências Python especificadas no requirements.txt
RUN pip install -r requirements.txt

# Execute a sua aplicação FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
