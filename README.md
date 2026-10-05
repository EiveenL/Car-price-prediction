# Análisis de datos y modelos predictivos — Concesionaria de vehículos

Análisis exploratorio y modelado predictivo sobre un dataset de vehículos usados del mercado argentino. Cubre el ciclo completo de analítica: extracción, limpieza, EDA, entrenamiento comparativo de modelos de regresión, segmentación por clustering y visualización ejecutiva en Power BI.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![Power BI](https://img.shields.io/badge/Power%20BI-dashboard-yellow)
![Jupyter](https://img.shields.io/badge/Jupyter-notebook-F37626)

---

## Objetivo

Determinar qué variables explican el precio de un vehículo usado y construir un modelo capaz de estimarlo a partir de sus características, entregando además una vista de negocio para la toma de decisiones comerciales.

## Estructura del repositorio

```
Car-price-DataAnalysis/
├── Data/
│   ├── argentina_cars.csv      # Dataset original
│   └── data_dashboard.csv      # Dataset procesado para el dashboard
├── Main/
│   ├── main.ipynb              # EDA, limpieza y preparación
│   ├── model.ipynb             # Entrenamiento y evaluación de modelos
│   ├── DecisionTree_regressor.pkl
│   ├── KNeighbors_regressor.pkl
│   ├── random_forest_model.pkl
│   ├── modelo_clustering.pkl
│   └── em.png
└── Presentation/
    └── dashboard.pbix          # Dashboard de Power BI
```

## Proceso

### 1. Preparación de datos

- **Normalización de moneda:** el dataset mezcla precios en pesos argentinos y dólares. Se unificaron a USD con el tipo de cambio de referencia del 16/12/2022.
- **Extracción de cilindrada:** el campo `motor` venía como texto libre; se aplicó una expresión regular para extraer el valor numérico.
- **Codificación de categóricas:** `LabelEncoder` sobre color, tipo de combustible, transmisión y tipo de carrocería.
- **Tratamiento de outliers:** se acotó el dataset a precios < 100.000 USD, kilometraje < 250.000 km y año ≥ 2000.
- **Escalado:** `MinMaxScaler` sobre las variables numéricas.

### 2. Análisis exploratorio (EDA)

Distribución de precios, relación entre antigüedad, kilometraje y valor de reventa, y análisis de correlación entre variables.

### 3. Modelos entrenados

Se entrenaron y compararon varios algoritmos de regresión:

| Modelo | Archivo |
|--------|---------|
| Random Forest Regressor | `random_forest_model.pkl` |
| Decision Tree Regressor | `DecisionTree_regressor.pkl` |
| K-Neighbors Regressor | `KNeighbors_regressor.pkl` |
| Clustering (segmentación) | `modelo_clustering.pkl` |

**División de datos:** 75% entrenamiento / 25% prueba (`random_state=123`).

**Métricas de evaluación:** MSE, RMSE y R².

<!-- COMPLETAR: reemplaza los guiones con los valores reales que arroja model.ipynb -->
| Modelo | R² | RMSE |
|--------|-----|------|
| Random Forest | — | — |
| Decision Tree | — | — |
| K-Neighbors | — | — |

### 4. Visualización

El dashboard en Power BI (`Presentation/dashboard.pbix`) presenta los hallazgos del análisis en formato de negocio, partiendo del dataset procesado `data_dashboard.csv`.

## Cómo reproducirlo

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook Main/main.ipynb
```

Ejecuta primero `main.ipynb` (limpieza y EDA) y luego `model.ipynb` (entrenamiento).

## Proyecto relacionado

El modelo Random Forest de este análisis se desplegó como aplicación web interactiva en
**[Car-price-prediction](https://github.com/EiveenL/Car-price-prediction)**.

## Licencia

MIT
