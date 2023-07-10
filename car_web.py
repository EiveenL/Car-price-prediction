import streamlit as st
import pickle
import numpy as np

# Cargar el modelo entrenado desde el archivo .pkl
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

# Cargar y mostrar la imagen como decoración
image = "R.jpg"  

# Definir las opciones para las variables categóricas
color_options = ['Plateado', 'Blanco', 'Gris oscuro', 'Gris', 'Negro', 'Naranja',
                 'Beige', 'Rojo', 'Azul', 'Dorado', 'Marrón', 'Verde', 'Violeta',
                 'Celeste']
fuel_type_options = ['Nafta', 'Diésel', 'Nafta/GNC', 'Híbrido/Nafta']
gear_options = ['Automática', 'Manual']

# Estilos CSS
css = """
<style>
.container {
    max-width: 600px;
    padding: 20px;
    margin: 0 auto;
    text-align: center;
}

.title {
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 30px;
}

.image {
    margin-bottom: 30px;
}

.form {
    margin-bottom: 20px;
}

.button {
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    background-color: #008080;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.button:hover {
    background-color: #005959;
}

.result {
    font-size: 24px;
    font-weight: bold;
    margin-top: 30px;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# Mostrar la sección de la página
st.markdown('<div class="container">', unsafe_allow_html=True)

# Mostrar el título
st.markdown('<h1 class="title">Predicción de Precio de Carros</h1>', unsafe_allow_html=True)

# Mostrar la imagen de decoración
st.image(image, use_column_width=True, caption='Imagen de decoración')

# Mostrar el formulario para ingresar las características
st.markdown('<div class="form">', unsafe_allow_html=True)
year = st.number_input('Año', min_value=2000, max_value=2023, step=1)
door = st.number_input('Puertas', min_value=2, max_value=5, step=1)
gear = st.selectbox('Transmisión', gear_options)
color = st.selectbox('Color', color_options)
motor = st.number_input('Motor', min_value=1.0, max_value=6.0, step=0.1)
fuel_type = st.selectbox('Tipo de Combustible', fuel_type_options)
kilometres = st.number_input('Kilómetros', min_value=0)
st.markdown('</div>', unsafe_allow_html=True)

# Realizar la predicción al hacer clic en el botón
if st.button('Predecir'):
    # Función para realizar la predicción
    def make_prediction(year, door, gear, color, motor, fuel_type, kilometres):
        # Codificar las características categóricas
        color_encoded = color_options.index(color)
        fuel_type_encoded = fuel_type_options.index(fuel_type)
        gear_encoded = gear_options.index(gear)

        # Crear el vector de características
        features = np.array([[year, door, gear_encoded, color_encoded, motor, fuel_type_encoded, kilometres]])

        # Hacer la predicción utilizando el modelo
        prediction = model.predict(features)

        return prediction[0]

    # Realizar la predicción utilizando las características ingresadas
    prediction = make_prediction(year, door, gear, color, motor, fuel_type, kilometres)

    # Mostrar el resultado de la predicción
    st.markdown('<div class="result">El precio estimado del carro es: ${}</div>'.format(prediction), unsafe_allow_html=True)

# Cerrar la sección de la página
st.markdown('</div>', unsafe_allow_html=True)
