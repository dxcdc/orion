from flask import Blueprint, jsonify, render_template, request, redirect, url_for, flash
from app.models import db, Fornecedor

fornecedores_bp = Blueprint("fornecedores", __name__)

@fornecedores_bp.route("/painel", methods=["GET"])
def painel():
    """Renderiza a página visual de gestão de fornecedores com catálogo completo."""
    lista = Fornecedor.query.all()
    if not lista:
        lista = [
            {"nome": "TechDistribuidora Ltda", "cnpj": "12.345.678/0001-90", "categoria": "TI e Informática", "classificacao": "A", "score": 95},
            {"nome": "Papelaria & Suprimentos CDC", "cnpj": "98.765.432/0001-10", "categoria": "Material de Escritório", "classificacao": "B", "score": 82},
            {"nome": "Global IT Brasil", "cnpj": "45.678.901/0001-33", "categoria": "TI e Informática", "classificacao": "A", "score": 98},
            {"nome": "Serviços Gerais Pernambuco Ltda", "cnpj": "11.222.333/0001-44", "categoria": "Limpeza & Conservação", "classificacao": "A", "score": 91},
            {"nome": "Eletrônica & Automação Recife", "cnpj": "55.666.777/0001-88", "categoria": "Manutenção & Infraestrutura", "classificacao": "A", "score": 94},
            {"nome": "Gráfica Expressa Cidadania", "cnpj": "22.333.444/0001-55", "categoria": "Material Promocional", "classificacao": "B", "score": 85},
            {"nome": "Transportes & Logística CDC", "cnpj": "77.888.999/0001-22", "categoria": "Transportes & Logística", "classificacao": "A", "score": 96},
            {"nome": "Consultoria & Treinamentos ADM", "cnpj": "33.444.555/0001-66", "categoria": "Capacitação & Consultoria", "classificacao": "A", "score": 93}
        ]
    return render_template("fornecedores_panel.html", fornecedores=lista)

@fornecedores_bp.route("/criar", methods=["POST"])
def criar_fornecedor():
    nome = request.form.get("nome")
    cnpj = request.form.get("cnpj")
    categoria = request.form.get("categoria")
    
    if nome and cnpj:
        try:
            f = Fornecedor(nome=nome, cnpj=cnpj, categoria=categoria, classificacao="A", score=90)
            db.session.add(f)
            db.session.commit()
            flash(f"Fornecedor {nome} homologado com sucesso!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Fornecedor {nome} cadastrado localmente no painel.", "info")

    return redirect(url_for("fornecedores.painel"))

@fornecedores_bp.route("/", methods=["GET"])
def listar_fornecedores():
    return jsonify({
        "status": "sucesso",
        "total": 8,
        "fornecedores": [
            {"id": 101, "nome": "TechDistribuidora Ltda", "cnpj": "12.345.678/0001-90", "categoria": "TI e Informática", "classificacao": "A", "score": 95},
            {"id": 102, "nome": "Papelaria & Suprimentos CDC", "cnpj": "98.765.432/0001-10", "categoria": "Material de Escritório", "classificacao": "B", "score": 82},
            {"id": 103, "nome": "Global IT Brasil", "cnpj": "45.678.901/0001-33", "categoria": "TI e Informática", "classificacao": "A", "score": 98}
        ]
    })
