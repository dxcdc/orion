# Usar imagem oficial Python 3.11 Slim
FROM python:3.11-slim

# Definir variáveis de ambiente do Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5050

# Instalar pacotes de sistema necessários para compilação e PostgreSQL
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar dependências e instalar
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código-fonte da aplicação
COPY . /app/

# Expor a porta 5050
EXPOSE 5050

# Comando para iniciar o servidor WSGI Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5050", "--workers", "3", "app:app"]
