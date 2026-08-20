import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key-cdc-adm-change-in-production")
    
    # Configuração de Banco de Dados PostgreSQL (com fallback SQLite para testes fora do Docker)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", 
        "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), "instance", "cdc_adm.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configurações de integração de APIs de sistemas externos
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.cdc.org.br/v1")
    API_TOKEN = os.getenv("API_TOKEN", "")
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "default": DevelopmentConfig
}
