from src.data_processing import carregar_e_limpar_dados
from src.model_training import treinar_regressao

if __name__ == "__main__":
    print("Iniciando pipeline de dados...")
    
    # 1. Carrega e limpa os dados
    caminho_csv = 'data/raw/MatchStatsTbl.csv'
    df_pronto = carregar_e_limpar_dados(caminho_csv)
    print(f"Dados limpos com sucesso. Total de partidas válidas: {df_pronto.shape[0]}")
    
    # 2. Treina o modelo
    print("\nTreinando o modelo de Regressão Linear...")
    modelo_treinado = treinar_regressao(df_pronto)