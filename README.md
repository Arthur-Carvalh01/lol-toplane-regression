# 🎮 Predição de Eficiência de Combate na Top Lane (League of Legends)

Este projeto de Ciência de Dados utiliza **Regressão Linear** para analisar o impacto do acúmulo de ouro no dano final causado por jogadores da rota do topo (Top Lane) no League of Legends. O objetivo é provar matematicamente o efeito "snowball" utilizando dados reais de partidas competitivas e validá-los em tempo real consumindo dados de jogadores.

## 📊 O Problema de Negócio (Gameplay)
O acúmulo de recursos (farm) na Top Lane realmente se converte em impacto nas lutas de equipe, ou é possível gerar grandes quantias de dano mesmo estando atrás no ouro? A hipótese deste modelo testa a eficiência de conversão de ouro em dano.

## 🛠️ Stack Tecnológica
- **Linguagem:** Python 3.10+
- **Análise e Limpeza de Dados:** Pandas
- **Machine Learning:** Scikit-Learn (Regressão Linear)
- **Integração de API:** Requests, python-dotenv (Riot Games API)
- **Visualização:** Matplotlib & Seaborn
- **Versionamento & Arquitetura:** Git, Modularização (Clean Code)

## 📈 Resultados da Análise Exploratória
Após filtrar um dataset de mais de 732 mil registros para isolar **104.169 instâncias exclusivas de Top Laners** (Patch 25.19+), os cálculos de correlação (Pearson) revelaram:
- Correlação Ouro x Dano Causado: **0.80** (Associação linear muito forte).
- Correlação Minions Abatidos x Dano Causado: **0.07** (Inexistente, indicando que farm passivo sem participação ativa em abates/objetivos não gera impacto no combate).

## 🤖 O Modelo Preditivo
O modelo de Regressão Linear extraiu os seguintes parâmetros matemáticos do comportamento do jogo:
- **Coeficiente Angular (Peso do Ouro): 2.95.** (Cada 1 unidade de ouro acumulado converte-se em quase 3 de dano adicional).
- **Coeficiente de Determinação (R²): 0.65.** (O acúmulo de ouro explica, sozinho, 65% de todo o dano causado pelo jogador).

## 🔌 Inferência em Tempo Real (Riot Games API)
O projeto conta com um módulo de integração direta com a **Riot Games API**. Um script extrai o histórico de partidas recentes de um jogador específico (via PUUID) e utiliza o modelo treinado globalmente para avaliar se o desempenho individual ficou acima ou abaixo do esperado matematicamente.
- **Validação Prática:** Em testes reais avaliando o campeão *Mordekaiser*, o modelo projetou um dano esperado de 33.7k para um acúmulo de 14.8k de ouro. O dano real entregue pelo jogador foi de 53.9k, demonstrando a capacidade da IA de isolar anomalias e atuações *outliers* (+20 mil de dano acima da média global).

## 📂 Como reproduzir este projeto
1. Clone este repositório: `git clone https://github.com/Arthur-Carvalh01/lol-toplane-regression.git`
2. Crie um ambiente virtual: `python -m venv venv` e ative-o.
3. Instale as dependências congeladas: `pip install -r requirements.txt`
4. Baixe o dataset **League of Legends(LoL) Matches Patch 25.19+** do Kaggle e insira-o em `data/raw/`.
5. **Configuração da API:** Crie um arquivo `.env` na raiz do projeto e insira sua chave de desenvolvedor (Riot Games): `RIOT_API_KEY=RGAPI-sua-chave-aqui`.
6. Execute o treinamento do modelo e a avaliação do histórico:
   - `python main.py` (Orquestração e modelagem global)
   - `python src/meu_desempenho.py` (Inferência individual via API)