import random
import datetime
from config import *

def ler_sensores() -> dict:
    """Simula leitura de sensores de umidade, temperatura e luz"""
    dados = {
        "data_hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "umidade_solo": round(random.uniform(10, 60), 2),
        "temperatura_ar": round(random.uniform(15, 40), 2),
        "nivel_luz": round(random.uniform(200, 1000), 2)
    }
    return dados

def analisar_condicoes(dados_sensores: dict) -> dict:
    """Analisa dados e define ações necessárias"""
    acoes = {
        "regar": dados_sensores["umidade_solo"] < LIMITE_UMIDADE_SOLO,
        "sombrear": dados_sensores["temperatura_ar"] > LIMITE_TEMPERATURA,
        "luz_suplementar": dados_sensores["nivel_luz"] < LIMITE_LUZ
    }
    return acoes