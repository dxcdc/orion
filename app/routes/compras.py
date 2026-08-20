from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash

compras_bp = Blueprint("compras", __name__)

@compras_bp.route("/requisicoes", methods=["GET"])
def requisicoes():
    """Renderiza a página visual de requisições de compras com dados completos."""
    pedidos = [
        {
            "id": "REQ-2026-001",
            "solicitante": "Setor Administrativo",
            "item": "Kit de Monitores LED 27\" & Periféricos TI",
            "centro_custo": "ADM - Suprimentos",
            "quantidade": 5,
            "prioridade": "Alta",
            "status": "EM_COTAÇÃO",
            "data": "2026-08-01"
        },
        {
            "id": "REQ-2026-002",
            "solicitante": "Manutenção & Infra",
            "item": "Nobreak 1200VA e Filtros de Linha",
            "centro_custo": "Infraestrutura",
            "quantidade": 3,
            "prioridade": "Urgente",
            "status": "EM_ANALISE",
            "data": "2026-08-03"
        },
        {
            "id": "REQ-2026-003",
            "solicitante": "Secretaria Geral",
            "item": "Lotes de Papel A4 e Cartuchos de Impressora",
            "centro_custo": "Secretaria",
            "quantidade": 20,
            "prioridade": "Normal",
            "status": "HOMOLOGADO",
            "data": "2026-07-28"
        },
        {
            "id": "REQ-2026-004",
            "solicitante": "Serviços Gerais",
            "item": "Kits de Produtos de Higiene e Desinfecção",
            "centro_custo": "Operacional",
            "quantidade": 15,
            "prioridade": "Normal",
            "status": "HOMOLOGADO",
            "data": "2026-07-25"
        },
        {
            "id": "REQ-2026-005",
            "solicitante": "Infraestrutura CDC",
            "item": "Manutenção Preventiva de Ar Condicionado",
            "centro_custo": "Infraestrutura",
            "quantidade": 1,
            "prioridade": "Alta",
            "status": "EM_COTAÇÃO",
            "data": "2026-08-02"
        },
        {
            "id": "REQ-2026-006",
            "solicitante": "TI & Dados",
            "item": "Servidor de Armazenamento NAS 4-Bay",
            "centro_custo": "TI & Sistemas",
            "quantidade": 1,
            "prioridade": "Urgente",
            "status": "EM_ANALISE",
            "data": "2026-08-02"
        },
        {
            "id": "REQ-2026-007",
            "solicitante": "Eventos & Capacitação",
            "item": "Material Didático & Apostilas Impressas",
            "centro_custo": "Treinamentos",
            "quantidade": 200,
            "prioridade": "Normal",
            "status": "EM_COTAÇÃO",
            "data": "2026-08-03"
        },
        {
            "id": "REQ-2026-008",
            "solicitante": "TI & Segurança",
            "item": "Licenças de Antivírus Corporativo (50 nós)",
            "centro_custo": "TI & Sistemas",
            "quantidade": 50,
            "prioridade": "Alta",
            "status": "HOMOLOGADO",
            "data": "2026-07-30"
        }
    ]
    return render_template("compras_requisicoes.html", pedidos=pedidos)

@compras_bp.route("/criar-form", methods=["POST"])
def criar_pedido_form():
    item = request.form.get("item", "Item Genérico")
    quantidade = request.form.get("quantidade", 1)
    flash(f"Requisição para '{item}' (Qtd: {quantidade}) enviada para cotação com sucesso!", "success")
    return redirect(url_for("compras.requisicoes"))

@compras_bp.route("/", methods=["GET"])
def listar_pedidos():
    return jsonify({
        "status": "sucesso",
        "total": 8,
        "pedidos": [
            {"id": "REQ-2026-001", "solicitante": "Setor Administrativo", "item": "Kits de Informática", "quantidade": 5, "status": "EM_COTACAO", "data": "2026-08-01"}
        ]
    })
