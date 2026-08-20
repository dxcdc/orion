from flask import Blueprint, jsonify, render_template

cotacoes_bp = Blueprint("cotacoes", __name__)

@cotacoes_bp.route("/mapa", methods=["GET"])
def mapa():
    """Renderiza a visualização do Mapa Comparativo de Cotações."""
    return render_template("cotacoes_mapa.html")

@cotacoes_bp.route("/", methods=["GET"])
def listar_cotacoes():
    return jsonify({
        "status": "sucesso",
        "cotacoes": [
            {"id": "COT-2026-089", "pedido_id": "REQ-2026-001", "status": "SUPERVISAO_AUTOMATIZADA", "propostas_recebidas": 3}
        ]
    })
