from flask import Blueprint, jsonify, request
from app.services.ongsys_api import ONGSYSService

ongsys_bp = Blueprint("ongsys", __name__)

@ongsys_bp.route("/status", methods=["GET"])
def status_ongsys():
    service = ONGSYSService()
    return jsonify({
        "status": "online",
        "api_url": service.base_url,
        "modulos_integrados": ["fornecedores", "orçamentos", "financeiro"]
    })

@ongsys_bp.route("/fornecedores", methods=["GET"])
def buscar_fornecedores_ongsys():
    service = ONGSYSService()
    resultado = service.get_fornecedores()
    return jsonify(resultado)

@ongsys_bp.route("/sincronizar-cotacao", methods=["POST"])
def sincronizar_cotacao():
    dados = request.get_json() or {}
    service = ONGSYSService()
    resultado = service.sync_cotacao(dados)
    return jsonify(resultado)
