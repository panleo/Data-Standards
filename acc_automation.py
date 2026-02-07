import os
import requests
from dotenv import load_dotenv

# 1. Carregar as credenciais do cofre
load_dotenv()

CLIENT_ID = os.getenv('ACC_CLIENT_ID')
CLIENT_SECRET = os.getenv('ACC_CLIENT_SECRET')

def obter_token_acesso():
    """
    Se conecta à Autodesk e pede uma 'chave temporária' (token)
    para podermos operar no sistema.
    """
    url = "https://developer.api.autodesk.com/authentication/v2/token"
    
    # Dados necessários para o login (conforme documentação APS)
    dados = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials',
        'scope': 'data:read data:write' # Permissão para ler e escrever dados
    }
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    print("🔑 Tentando autenticar na Autodesk...")
    resposta = requests.post(url, data=dados, headers=headers)
    
    if resposta.status_code == 200:
        print("✅ Autenticação bem-sucedida!")
        return resposta.json()['access_token']
    else:
        print(f"❌ Erro na autenticação: {resposta.status_code}")
        return None

if __name__ == "__main__":
    token = obter_token_acesso()
    if token:
        print(f"Seu token temporário começa com: {token[:10]}...")