# 🏢 CDC ADM - Sistema de Gestão Administrativa, Compras & Cotações

> **Ferramenta Especializada para o Setor Administrativo do CDC**
> 
> O **CDC ADM** é a solução centralizada do setor administrativo projetada para otimizar e governar os processos de gestão de **fornecedores**, **compras**, **cotações de preços** e **classificação de fornecedores**. O sistema conta com **supervisão de processos automatizada** para agilizar a triagem operacional e integra-se diretamente através de **APIs de sistemas externos**.

---

## 🎯 Objetivos do Sistema

- **Gestão Integral de Fornecedores**: Cadastro, homologação e classificação contínua baseada em desempenho, prazos e histórico de entregas.
- **Requisições de Compras**: Fluxo padronizado de solicitações com controle de aprovação e rastreabilidade.
- **Cotações Inteligentes**: Mapeamento e comparação automática de propostas comerciais com **supervisão de processos automatizada**.
- **Supervisão Automatizada**: Algoritmos de triagem de cotações, qualificação contínua de fornecedores (Vendor Rating) e verificação de preços.
- **Ecossistema de APIs**: Consumo e sincronização de dados via APIs REST com plataformas corporativas e sistemas legados.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.11+
- **Framework Web**: [Flask](https://flask.palletsprojects.org/)
- **Servidor WSGI**: Gunicorn
- **Supervisão & Automação**: Motores de regras operacionais e supervisão automatizada de processos
- **Integração Externa**: APIs REST (`requests`)
- **Controle de Versão**: Git & GitHub (`git@github.com:dxcdc/adm.git`)

---

## 🏗️ Estrutura do Repositório

```text
ADM/
├── README.md                  # Documentação principal do projeto
├── .gitignore                 # Arquivos omitidos pelo Git
├── requirements.txt           # Dependências do projeto Python/Flask
├── config.py                  # Configurações de ambiente (Dev/Prod, API Keys)
├── app.py                     # Ponto de entrada do aplicativo Flask
├── app/                       # Código-fonte da aplicação
│   ├── __init__.py            # Application Factory
│   ├── routes/                # Endpoints e Blueprints RESTful
│   │   ├── main.py            # Rota principal e health check
│   │   ├── fornecedores.py    # Rotas de cadastro e classificação
│   │   ├── compras.py         # Rotas de pedidos de compras
│   │   ├── cotacoes.py        # Mapa de cotações e supervisão automatizada
│   │   └── api_externa.py     # Integração e consumo de APIs externas
│   └── services/              # Serviços de negócios e integrações
│       ├── automacao_service.py # Motor de supervisão automatizada de processos
│       └── api_service.py     # Cliente de consumo de APIs externas
├── docs/                      # Documentação técnica e governança
│   └── arquitetura.md         # Detalhamento arquitetural dos fluxos
└── Templates/                 # Modelos de interfaces visuais e dashboards
```

---

## 🚀 Como Executar o Projeto Localmente

### 1. Pré-requisitos
- Python 3.10 ou superior
- Git e chave SSH configurada no GitHub

### 2. Passo a Passo

```bash
# Entrar no diretório do projeto
cd /home/vier/Documentos/Code/CDC/ADM

# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação em modo de desenvolvimento
python app.py
```

A aplicação estará acessível em: `http://localhost:5000` ou `http://localhost:5050`

---

## 📄 Licença e Governança

Mantido pela equipe CDC. Para diretrizes de contribuição e padrões editoriais, consulte as normas de governança do CDC Receitas.
