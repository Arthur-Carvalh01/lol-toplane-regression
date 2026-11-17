import pandas as pd
import warnings
from data_processing import carregar_e_limpar_dados
from model_training import treinar_regressao

# Ignora avisos bobos do Pandas no terminal
warnings.filterwarnings('ignore')

print("Treinando a Inteligência Artificial com os 104 mil jogos globais...")
df_pronto = carregar_e_limpar_dados('data/raw/MatchStatsTbl.csv')
modelo = treinar_regressao(df_pronto)

minhas_partidas = [
    {'campeao': 'Mordekaiser', 'ouro': 16822, 'dano_real': 44941, 'vitoria': True},
    {'campeao': 'Mordekaiser', 'ouro': 10155, 'dano_real': 19239, 'vitoria': False},
    {'campeao': 'Mordekaiser', 'ouro': 12696, 'dano_real': 27739, 'vitoria': False},
    {'campeao': 'Mordekaiser', 'ouro': 7941,  'dano_real': 15738, 'vitoria': False},
    {'campeao': 'Mordekaiser', 'ouro': 7727,  'dano_real': 18636, 'vitoria': True},
    {'campeao': 'Mordekaiser', 'ouro': 9496,  'dano_real': 21043, 'vitoria': False},
    {'campeao': 'Mordekaiser', 'ouro': 14894, 'dano_real': 53913, 'vitoria': True}
]

print("\n" + "="*50)
print("AVALIAÇÃO DO SEU DESEMPENHO (MODELO VS REALIDADE)")
print("="*50)

for i, p in enumerate(minhas_partidas, 1):
    # O modelo do Scikit-Learn exige um DataFrame de 2 dimensões para prever
    entrada_ia = pd.DataFrame([{'TotalGold': p['ouro']}])
    
    # A IA prevê o dano matemático baseada no seu ouro
    dano_esperado = modelo.predict(entrada_ia)[0]
    
    # Compara a realidade com a matemática
    diferenca = p['dano_real'] - dano_esperado
    
    if diferenca > 0:
        status = f"CARREGOU (+{int(diferenca)} acima da média global)"
    else:
        status = f"PESOU ({int(diferenca)} abaixo da média global)"
        
    resultado = "VITÓRIA" if p['vitoria'] else "DERROTA"
    
    print(f"Partida {i} [{resultado}]: {p['campeao']}")
    print(f"Ouro Acumulado: {p['ouro']}")
    print(f"Dano Esperado (IA): {int(dano_esperado)}")
    print(f"Dano Real Causado: {p['dano_real']}")
    print(f"Veredito: {status}\n")