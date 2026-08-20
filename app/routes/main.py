from flask import Blueprint, render_template, session, redirect, url_for, jsonify

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def landing():
    """Renderiza a Landing Page limpa do setor administrativo."""
    return render_template("landing.html")

@main_bp.route("/dashboard")
def dashboard():
    """Renderiza o Painel Geral pós-login."""
    if not session.get("user"):
        session["user"] = "fvier"
    return render_template("dashboard.html")

@main_bp.route("/apis-painel")
def apis_painel():
    """Renderiza o Painel do Ecossistema de APIs."""
    return render_template("apis_painel.html")

@main_bp.route("/relatorios")
def relatorios():
    """Renderiza o Painel de Relatórios & Indicadores Administrativos."""
    return render_template("relatorios.html")

@main_bp.route("/api-info")
def api_info():
    return jsonify({
        "sistema": "CDC ADM - Gestão Administrativa & Suprimentos",
        "versao": "1.0.0",
        "status": "online"
    })
