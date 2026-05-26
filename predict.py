import joblib
import pandas as pd

# Cargar modelo
modelo = joblib.load('mejor_modelo_titanic.pkl')

# Datos de ejemplo
nuevo_pasajero = pd.DataFrame([{
    'pclass': 3, 'sex': 'male', 'age': 25,
    'sibsp': 0, 'parch': 0, 'fare': 7.25,
    'embarked': 'S', 'alone': 1
}])

# Predecir
pred = modelo.predict(nuevo_pasajero)[0]
prob = modelo.predict_proba(nuevo_pasajero)[0][1]

print(f"Predicción: {'Sobrevive' if pred == 1 else 'No sobrevive'}")
print(f"Probabilidad: {prob:.2%}")