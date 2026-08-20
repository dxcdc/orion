import requests
from flask import current_app

class ONGSYSService:
    """
    Serviço responsável por encapsular a comunicação via API REST com o sistema ONGSYS.
    Gerencia a autenticação, requisições de fornecedores, lançamentos e orçamentos.
    """
    
    def __init__(self, base_url=None, token=None, timeout=None):
        self.base_url = base_url or current_app.config.get("ONGSYS_API_BASE_URL")
        self.token = token or current_app.config.get("ONGSYS_API_TOKEN")
        self.timeout = timeout or current_app.config.get("ONGSYS_TIMEOUT", 30)

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_fornecedores(self, page=1, limit=50):
        """Busca lista de fornecedores cadastrados no ONGSYS."""
        if not self.token:
            return {"status": "mock", "data": [], "message": "ONGSYS_API_TOKEN não configurado. Retornando dados em modo simulação."}
        
        try:
            url = f"{self.base_url}/fornecedores"
            response = requests.get(url, headers=self._headers(), params={"page": page, "limit": limit}, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": True, "message": f"Falha na comunicação com ONGSYS: {str(e)}"}

    def sync_cotacao(self, cotacao_data):
        """Sincroniza um mapa de cotação finalizado com o módulo financeiro do ONGSYS."""
        if not self.token:
            return {"status": "mock", "success": True, "message": "Simulação: Cotação sincronizada no ONGSYS."}
            
        try:
            url = f"{self.base_url}/compras/cotacoes"
            response = requests.post(url, headers=self._headers(), json=cotacao_data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": True, "message": f"Erro ao sincronizar cotação no ONGSYS: {str(e)}"}
