from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(50), default="Administrador")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Fornecedor(db.Model):
    __tablename__ = "fornecedores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    cnpj = db.Column(db.String(20), unique=True, nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    classificacao = db.Column(db.String(5), default="A")
    score = db.Column(db.Integer, default=95)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Cotacao(db.Model):
    __tablename__ = "cotacoes"

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    item = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default="SUPERVISAO_AUTOMATIZADA")
    melhor_proposta = db.Column(db.String(150), nullable=True)
    valor_total = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
