import os
import requests
from dotenv import load_dotenv

caminho_env = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(caminho_env)

API_KEY = os.getenv("RIOT_API_KEY")

if not API_KEY:
    print("ERRO LOCAL: Chave não encontrada no .env!")
    exit()

# Roteamento global para contas e partidas na região das Américas
REGION_AMERICAS = "https://americas.api.riotgames.com"

def obter_puuid(game_name, tag_line):
    """Busca o identificador único da conta."""
    url = f"{REGION_AMERICAS}/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    headers = {"X-Riot-Token": API_KEY}
    resposta = requests.get(url, headers=headers)
    if resposta.status_code == 200:
        return resposta.json()['puuid']
    return None

def obter_ultimas_partidas(puuid, quantidade=15):
    """Busca a lista de IDs das últimas partidas jogadas."""
    # O start=0 pega a partir da mais recente
    url = f"{REGION_AMERICAS}/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={quantidade}"
    headers = {"X-Riot-Token": API_KEY}
    resposta = requests.get(url, headers=headers)
    if resposta.status_code == 200:
        return resposta.json()
    return []

def extrair_meus_dados_top(match_id, meu_puuid):
    """Abre a partida, encontra o jogador e extrai Ouro e Dano se for Top Lane."""
    url = f"{REGION_AMERICAS}/lol/match/v5/matches/{match_id}"
    headers = {"X-Riot-Token": API_KEY}
    resposta = requests.get(url, headers=headers)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        
        # Percorre os 10 jogadores da partida
        for participante in dados['info']['participants']:
            if participante['puuid'] == meu_puuid:
                # Verifica se a rota sorteada/jogada foi o TOP
                if participante['teamPosition'] == 'TOP':
                    return {
                        'campeao': participante['championName'],
                        'ouro_total': participante['goldEarned'],
                        'dano_causado': participante['totalDamageDealtToChampions'],
                        'vitoria': participante['win']
                    }
    return None

if __name__ == "__main__":
    meu_nick = "EL TOURO"
    minha_tag = "069"
    
    print(f"Buscando PUUID para {meu_nick}#{minha_tag}...")
    meu_puuid = obter_puuid(meu_nick, minha_tag)
    
    if meu_puuid:
        print("Buscando as últimas 15 partidas...")
        match_ids = obter_ultimas_partidas(meu_puuid, quantidade=15)
        
        minhas_partidas_top = []
        for match_id in match_ids:
            dados_top = extrair_meus_dados_top(match_id, meu_puuid)
            if dados_top:
                minhas_partidas_top.append(dados_top)
        
        print(f"\nEncontradas {len(minhas_partidas_top)} partidas recentes jogando no TOP.")
        print("-" * 50)
        for p in minhas_partidas_top:
            resultado = "Vitória" if p['vitoria'] else "Derrota"
            print(f"[{resultado}] {p['campeao']} | Ouro Total: {p['ouro_total']} | Dano Causado: {p['dano_causado']}")
        print("-" * 50)