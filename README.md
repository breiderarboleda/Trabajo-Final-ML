# Proyecto Titanic: Predicción de Supervivencia

## Descripción del Proyecto
Este proyecto aplica la metodología **CRISP-DM** para predecir si un pasajero del Titanic sobrevivió o no al naufragio.

**Objetivo:** Predecir la variable 'survived' usando técnicas de Machine Learning.
**Dataset:** `sns.load_dataset('titanic')` de Seaborn.

## Estructura del Proyecto
*   `Trabajo_final_ML.ipynb`: Notebook de Jupyter con todo el análisis, limpieza y modelado.
*   `mejor_modelo_titanic.pkl`: Archivo del modelo final entrenado (Árbol de Decisión).
*   `predict.py`: Script de ejemplo para cargar el modelo y hacer predicciones.
*   `requirements.txt`: Lista de librerías necesarias.

## Cómo Ejecutar el Proyecto
1.  Clona el repositorio.
2.  Instala las dependencias: `pip install -r requirements.txt`
3.  Explora el notebook o ejecuta `predict.py` para ver el modelo en acción.

## Resultados del Modelo (Resumen)
*   **Mejor Modelo:** Árbol de Decisión (según Recall).
*   **Recall en prueba:** 0.7246.
*   **Accuracy en prueba:** 0.7989.
