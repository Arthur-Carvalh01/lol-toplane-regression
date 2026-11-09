import pandas as pd

def carregar_e_limpar_dados(caminho_arquivo):
    """Carrega o dataset e filtra apenas os Top Laners válidos."""
    df = pd.read_csv(caminho_arquivo)
    
    # Filtra a Top Lane
    df_top = df[df['Lane'].astype(str).str.upper() == 'TOP'].copy()
    
    # Remove anomalias (AFKs)
    df_limpo = df_top.dropna(subset=['TotalGold', 'MinionsKilled', 'DmgDealt'])
    df_limpo = df_limpo[(df_limpo['TotalGold'] > 0) & (df_limpo['DmgDealt'] > 0)]
    
    return df_limpo