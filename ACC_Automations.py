import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

#Recupera as credenciais sem expor-las diretamente no código
acc_client_id = os.getenv('ACC_CLIENT_ID')
acc_client_secret = os.getenv('ACC_CLIENT_SECRET')
roboflow_api_key = os.getenv('ROBOFLOW_API_KEY')

print(f"O sistema está configurado para o Client ID: {client_id}")

