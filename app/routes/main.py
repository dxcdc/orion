from flask import Blueprint, render_template, session, redirect, url_for, jsonify

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def landing():
    """Renderiza a Landing Page oficial do CDC Orion."""
    return render_template("landing.html")

@main_bp.route("/dashboard")
def dashboard():
    """Renderiza o Painel Geral de Preservação pós-login."""
    if not session.get("user"):
        session["user"] = "fvier"
    return render_template("dashboard.html", active_page="dashboard")

@main_bp.route("/checkins")
def checkins():
    """Renderiza o Módulo de Check-ins de Rotina."""
    if not session.get("user"):
        session["user"] = "fvier"
    items = [
        {"codigo": "CHK-9041", "evento": "Confirmação de Rotina Diária — Manhã", "horario": "08:30:00", "status": "Confirmado"},
        {"codigo": "CHK-9042", "evento": "Sinal de Presença & Acompanhamento", "horario": "12:15:00", "status": "Ativo"},
        {"codigo": "CHK-9043", "evento": "Check-in de Segurança Intermediário", "horario": "16:00:00", "status": "Confirmado"},
        {"codigo": "CHK-9044", "evento": "Confirmação de Perímetro Seguro", "horario": "18:45:00", "status": "Sincronizado"},
    ]
    return render_template("modulo_preservacao.html", 
                           title="Check-ins de Rotina", 
                           subtitle="Acompanhamento periódico de bem-estar com linguagem neutra",
                           icon="ri-user-heart-line",
                           active_page="checkins",
                           items=items)

@main_bp.route("/perimetro")
def perimetro():
    """Renderiza o Módulo de Perímetro de Conforto."""
    if not session.get("user"):
        session["user"] = "fvier"
    items = [
        {"codigo": "PER-102", "evento": "Verificação de Zona Residencial Segura", "horario": "07:00:00", "status": "Zona Livre"},
        {"codigo": "PER-103", "evento": "Monitoramento de Rota de Deslocamento", "horario": "11:30:00", "status": "Sem Desvios"},
        {"codigo": "PER-104", "evento": "Validação de Perímetro de Trabalho", "horario": "14:20:00", "status": "Verificado"},
        {"codigo": "PER-105", "evento": "Check de Proximidade & Segurança", "horario": "17:50:00", "status": "Protegido"},
    ]
    return render_template("modulo_preservacao.html", 
                           title="Perímetro de Conforto", 
                           subtitle="Monitoramento de áreas de segurança e zonas de deslocamento",
                           icon="ri-compass-3-line",
                           active_page="perimetro",
                           items=items)

@main_bp.route("/tutores")
def tutores():
    """Renderiza a Rede de Tutores & Parceiros."""
    if not session.get("user"):
        session["user"] = "fvier"
    items = [
        {"codigo": "TUT-01", "evento": "Tutor de Acolhimento Alpha — Contato Direto", "horario": "Disponível 24/7", "status": "Conectado"},
        {"codigo": "TUT-02", "evento": "Rede de Apoio Local — Agente de Ligação", "horario": "Ativo", "status": "Habilitado"},
        {"codigo": "TUT-03", "evento": "Central de Resposta Rápida — Equipe Bravo", "horario": "Em Prontidão", "status": "Sincronizado"},
    ]
    return render_template("modulo_preservacao.html", 
                           title="Rede de Tutores & Suporte", 
                           subtitle="Contatos habilitados e equipe de acolhimento sob codinomes neutros",
                           icon="ri-contacts-book-2-line",
                           active_page="tutores",
                           items=items)

@main_bp.route("/canais-apoio")
def canais_apoio():
    """Renderiza os Canais de Apoio Silencioso."""
    if not session.get("user"):
        session["user"] = "fvier"
    items = [
        {"codigo": "CAN-801", "evento": "Linha Direta Encriptada — Atendimento Discreto", "horario": "Canal Aberto", "status": "Ativo"},
        {"codigo": "CAN-802", "evento": "Sinalização Silenciosa em 1-Clique", "horario": "Standby", "status": "Pronto"},
        {"codigo": "CAN-803", "evento": "Canal Integrado de Chamados Neutros", "horario": "Ativo", "status": "Protegido"},
    ]
    return render_template("modulo_preservacao.html", 
                           title="Canais Silenciosos de Apoio", 
                           subtitle="Interface de comunicação camuflada sem emissores sonoros ou alertas denunciantes",
                           icon="ri-chat-shield-line",
                           active_page="canais_apoio",
                           items=items)

@main_bp.route("/registros")
def registros():
    """Renderiza o Cofre de Registros & Evidências."""
    if not session.get("user"):
        session["user"] = "fvier"
    items = [
        {"codigo": "REG-3001", "evento": "Registro Criptografado de Ocorrência #102", "horario": "2026-08-20 10:15", "status": "Cofre Seguro"},
        {"codigo": "REG-3002", "evento": "Backup de Provas & Histórico com Carimbo do Tempo", "horario": "2026-08-20 14:00", "status": "Indexado"},
        {"codigo": "REG-3003", "evento": "Sincronização de Hash de Evidência", "horario": "2026-08-20 16:45", "status": "Protegido"},
    ]
    return render_template("modulo_preservacao.html", 
                           title="Cofre de Registros & Atividades", 
                           subtitle="Histórico encriptado de ocorrências e logs com validade jurídica",
                           icon="ri-shield-flash-line",
                           active_page="registros",
                           items=items)

@main_bp.route("/documentos")
def documentos():
    """Renderiza a Documentação Protegida."""
    if not session.get("user"):
        session["user"] = "fvier"
    items = [
        {"codigo": "DOC-701", "evento": "Diretrizes Judiciais de Proteção Pessoal", "horario": "Vigente", "status": "Protegido"},
        {"codigo": "DOC-702", "evento": "Termo de Sigilo e Acolhimento CDC", "horario": "Assinado", "status": "Válido"},
        {"codigo": "DOC-703", "evento": "Ficha de Identidade Preservada", "horario": "Atualizado", "status": "Criptografado"},
    ]
    return render_template("modulo_preservacao.html", 
                           title="Documentação Protegida", 
                           subtitle="Repositório seguro de pareceres, termos e ordens de proteção",
                           icon="ri-folder-shield-2-line",
                           active_page="documentos",
                           items=items)

@main_bp.route("/protocolos")
def protocolos():
    """Renderiza os Protocolos de Contingência."""
    if not session.get("user"):
        session["user"] = "fvier"
    items = [
        {"codigo": "PROT-A", "evento": "Protocolo de Evacuação Preventiva", "horario": "Revisado", "status": "Ativo"},
        {"codigo": "PROT-B", "evento": "Protocolo de Troca de Perímetro Residencial", "horario": "Pronto", "status": "Homologado"},
        {"codigo": "PROT-C", "evento": "Plano de Acionamento da Central de Emergências", "horario": "Automático", "status": "Testado"},
    ]
    return render_template("modulo_preservacao.html", 
                           title="Protocolos & Diretrizes", 
                           subtitle="Manuais de contingência e planos de ação para situações de risco",
                           icon="ri-file-list-3-line",
                           active_page="protocolos",
                           items=items)

@main_bp.route("/apis-painel")
def apis_painel():
    """Renderiza o Painel do Ecossistema de APIs."""
    if not session.get("user"):
        session["user"] = "fvier"
    return render_template("apis_painel.html", active_page="apis")

@main_bp.route("/relatorios")
def relatorios():
    """Renderiza o Painel de Relatórios & Indicadores Administrativos."""
    if not session.get("user"):
        session["user"] = "fvier"
    return render_template("relatorios.html", active_page="relatorios")

@main_bp.route("/admin-guia")
def admin_guia():
    """Renderiza o Guia Admin & Autenticação 2FA."""
    if not session.get("user"):
        session["user"] = "fvier"
    items = [
        {"codigo": "ADM-01", "evento": "Configuração de Token TOTP / 2FA Corporativo", "horario": "Ativo", "status": "Habilitado"},
        {"codigo": "ADM-02", "evento": "Políticas de Acesso & Controle de Sessões Admin", "horario": "Sincronizado", "status": "Válido"},
        {"codigo": "ADM-03", "evento": "Auditoria de Credenciais & Rotatividade de Chaves", "horario": "Automático", "status": "Protegido"},
    ]
    return render_template("modulo_preservacao.html", 
                           title="Guia Admin & 2FA", 
                           subtitle="Parâmetros de segurança, controle de acesso e autenticação em dois fatores",
                           icon="ri-settings-5-line",
                           active_page="admin_guia",
                           items=items)

@main_bp.route("/central-testes")
def central_testes():
    """Renderiza a Central de Testes & Simulação de Sinais."""
    if not session.get("user"):
        session["user"] = "fvier"
    items = [
        {"codigo": "TST-101", "evento": "Simulação de Disparo de Sinal Silencioso", "horario": "Último Teste: OK", "status": "Sucesso"},
        {"codigo": "TST-102", "evento": "Validação de Webhook com Central de Apoio", "horario": "Último Teste: OK", "status": "Verificado"},
        {"codigo": "TST-103", "evento": "Teste de Notificação Camuflada por E-mail", "horario": "Último Teste: OK", "status": "Entregue"},
    ]
    return render_template("modulo_preservacao.html", 
                           title="Central de Testes & Simulação", 
                           subtitle="Ambiente de validação segura para rotinas de emergência e sinais de suporte",
                           icon="ri-flask-line",
                           active_page="central_testes",
                           items=items)

@main_bp.route("/api-info")
def api_info():
    return jsonify({
        "sistema": "CDC Orion - Plataforma de Preservação & Governança",
        "versao": "1.0.0",
        "status": "online",
        "stealth_mode": "active"
    })
