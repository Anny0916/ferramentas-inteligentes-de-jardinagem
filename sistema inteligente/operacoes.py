from config import *
from monitoramento import analisar_condicoes

def operar_regador(ativar: bool) -> str:
    """Controla o regador automático"""
    if ativar:
        return f"✅ Regador ativado por {DURACAO_REGAGEM} minutos"
    return "❌ Regador desativado"

def operar_sombreamento(ativar: bool) -> str:
    """Controla o sistema de sombreamento"""
    if ativar:
        return "✅ Sombreamento ativado para reduzir temperatura"
    return "❌ Sombreamento desativado"

def operar_luzes(ativar: bool) -> str:
    """Controla luzes suplementares"""
    if ativar:
        return f"✅ Luzes suplementares ativadas (intensidade: {INTENSIDADE_LUZ} lux)"
    return "❌ Luzes suplementares desativadas"

def executar_acoes(dados_sensores: dict) -> list:
    """Executa ações com base na análise das condições"""
    acoes = analisar_condicoes(dados_sensores)
    resultados = [
        operar_regador(acoes["regar"]),
        operar_sombreamento(acoes["sombrear"]),
        operar_luzes(acoes["luz_suplementar"])
    ]
    return resultados