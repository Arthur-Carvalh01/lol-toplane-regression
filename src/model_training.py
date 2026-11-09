from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

def treinar_regressao(df):
    """Treina o modelo de Regressão Linear para prever Dano com base no Ouro."""
    X = df[['TotalGold']]
    y = df['DmgDealt']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    
    y_pred = modelo.predict(X_test)
    
    print("=== Resultados do Modelo ===")
    print(f"Peso do Ouro (Coeficiente): {modelo.coef_[0]:.2f}")
    print(f"R² (Poder de Explicação): {r2_score(y_test, y_pred):.2f}")
    print(f"Erro Médio Absoluto: {mean_absolute_error(y_test, y_pred):.2f}")
    
    return modelo