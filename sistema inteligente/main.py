from monitoramento import ler_sensores
from operacoes import executar_acoes

def main():
    print("📊 SISTEMA DE JARDINAGEM AUTÔNOMA - INICIADO\n")
    
    # Coletar dados dos sensores
    dados = ler_sensores()
    print("📈 DADOS DOS SENSORES:")
    for chave, valor in dados.items():
        print(f"- {chave}: {valor}")
    
    # Executar ações necessárias
    print("\n⚙️ AÇÕES EXECUTADAS:")
    resultados = executar_acoes(dados)
    for res in resultados:
        print(f"- {res}")
    
    print("\n🔚 SISTEMA FINALIZADO")

if __name__ == "__main__":
    main()