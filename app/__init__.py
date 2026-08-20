import os
from flask import Flask
from config import config_by_name
from app.models import db, User

def create_app(config_name=None):
    if not config_name or config_name == "default":
        config_name = os.getenv("FLASK_ENV", "prod")
    app = Flask(__name__)
    app.config.from_object(config_by_name.get(config_name, config_by_name["prod"]))

    # Inicializar o Banco de Dados (PostgreSQL / SQLite)
    db.init_app(app)

    # Registrar Blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.fornecedores import fornecedores_bp
    from app.routes.compras import compras_bp
    from app.routes.cotacoes import cotacoes_bp
    from app.routes.ongsys import ongsys_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(fornecedores_bp, url_prefix="/fornecedores")
    app.register_blueprint(compras_bp, url_prefix="/compras")
    app.register_blueprint(cotacoes_bp, url_prefix="/cotacoes")
    app.register_blueprint(ongsys_bp, url_prefix="/ongsys")

    # Inicialização das tabelas e criação do usuário fvier padrão
    with app.app_context():
        # Garantir diretório instance para SQLite local
        os.makedirs(app.instance_path, exist_ok=True)
        db.create_all()
        seed_fvier_user()

    return app

def seed_fvier_user():
    """Gera o usuário fvier com senha segura no banco de dados se não existir."""
    try:
        user = User.query.filter((User.username == "fvier") | (User.email == "fvier@cdc.org.br")).first()
        if not user:
            default_password = os.getenv("SEED_USER_PASSWORD", "cdc@adm2026")
            new_user = User(
                username="fvier",
                email="fvier@cdc.org.br",
                role="Administrador"
            )
            new_user.set_password(default_password)
            db.session.add(new_user)
            db.session.commit()
            print(f"[SEED] Usuário fvier criado com sucesso! (Senha: {default_password})")
    except Exception as e:
        db.session.rollback()
        print(f"[SEED WARNING] Falha ao verificar/criar usuário fvier: {e}")

app = create_app()
