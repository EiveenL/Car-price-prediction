# Predicción de precios de vehículos — Aplicación web con Machine Learning

Aplicación web que estima el precio de mercado de un vehículo usado a partir de sus características, usando un modelo **Random Forest** entrenado sobre datos reales del mercado argentino. Pensada para que un asesor comercial obtenga una referencia de precio sin conocimiento técnico.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B)
![scikit--learn](https://img.shields.io/badge/scikit--learn-RandomForest-orange)
![Power BI](https://img.shields.io/badge/Power%20BI-dashboard-yellow)

**🔗 Aplicación en vivo:** https://car-price-prediction-itd.streamlit.app/
**📊 Dashboard Power BI:** [ver reporte](https://app.powerbi.com/view?r=eyJrIjoiY2JlY2Y0NjYtZmE5Yy00YmVlLTg3NzktOGRlMjM5ZGU2ZTI3IiwidCI6ImM0YTY2YzM0LTJiYjctNDUxZi04YmUxLWIyYzI2YTQzMDE1OCIsImMiOjR9)

<!-- SUGERENCIA: agrega aquí una captura de pantalla de la app -->
<!-- ![Captura de la aplicación](docs/screenshot.png) -->

---

## Del dato al producto

Este repositorio cierra el ciclo que empieza en
**[Car-price-DataAnalysis](https://github.com/EiveenL/Car-price-DataAnalysis)** (análisis exploratorio y comparación de modelos):

```
Dataset crudo  →  EDA y limpieza  →  Entrenamiento  →  Modelo serializado  →  App web  →  Dashboard
```

## Estructura

```
Car-price-prediction/
├── car_model.py              # Preparación de datos y entrenamiento del modelo
├── car_web.py                # Interfaz web en Streamlit
├── argentina_cars.csv        # Dataset de entrenamiento
├── random_forest_model.pkl   # Modelo entrenado y serializado
├── regression_model.pkl      # Modelo de regresión alternativo
├── requirements.txt
└── R.jpg
```

## Preparación de datos (`car_model.py`)

| Paso | Detalle |
|------|---------|
| Normalización de moneda | Conversión de pesos argentinos a USD (tipo de cambio de referencia 16/12/2022) |
| Extracción de cilindrada | Expresión regular sobre el campo `motor`, que venía como texto libre |
| Codificación categórica | `LabelEncoder` sobre color, combustible, transmisión y carrocería |
| Filtrado de outliers | Precio < 100.000 USD · Kilometraje < 250.000 km · Año ≥ 2000 |
| Escalado | `MinMaxScaler` sobre las variables predictoras |
| Partición | 75% entrenamiento / 25% prueba (`random_state=123`) |

## Modelo

**`RandomForestRegressor(max_depth=9, random_state=10)`**

Se evaluaron además SVR, Decision Tree, AdaBoost y K-Neighbors; Random Forest obtuvo el mejor desempeño.

**Métricas:** MSE, RMSE y R² sobre el conjunto de prueba.

<!-- COMPLETAR con los valores reales que imprime car_model.py -->
| Métrica | Valor |
|---------|-------|
| R² | — |
| RMSE | — |

## Variables de entrada en la aplicación

| Variable | Tipo | Rango / opciones |
|----------|------|------------------|
| Año | Numérico | 2000 – 2023 |
| Puertas | Numérico | 2 – 5 |
| Transmisión | Categórico | Automática, Manual |
| Color | Categórico | 14 opciones |
| Motor (cilindrada) | Numérico | 1.0 – 6.0 |
| Tipo de combustible | Categórico | Nafta, Diésel, Nafta/GNC, Híbrido/Nafta |
| Kilómetros | Numérico | ≥ 0 |

## Ejecución local

```bash
git clone https://github.com/EiveenL/Car-price-prediction.git
cd Car-price-prediction
pip install -r requirements.txt
streamlit run car_web.py
```

La aplicación se abre en `http://localhost:8501`.

Para reentrenar el modelo desde cero:

```bash
python car_model.py
```

## Stack

`Python` · `pandas` · `NumPy` · `scikit-learn` · `Streamlit` · `Matplotlib` · `Seaborn` · `Power BI`

## Mejoras pendientes

- [ ] Aplicar el mismo `MinMaxScaler` del entrenamiento en la inferencia de la app (serializarlo junto al modelo).
- [ ] Reutilizar los `LabelEncoder` entrenados en lugar de codificar por índice de lista.
- [ ] Actualizar el tipo de cambio o parametrizarlo como variable de entrada.
- [ ] Agregar validación cruzada y búsqueda de hiperparámetros.
- [ ] Mostrar un intervalo de confianza junto a la predicción puntual.

## Licencia

MIT
