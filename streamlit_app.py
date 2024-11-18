import streamlit as st
import requests
import pandas as pd

st.title("Datos Recibidos del Webhook (Flask)")

# Endpoint de Flask para obtener los datos
flask_endpoint = "https://oc-webhook.onrender.com/get_data"

# Obtener los datos desde Flask
try:
    response = requests.get(flask_endpoint)
    if response.status_code == 200:
        data = response.json()

        if data:
            # Mostrar los datos en una tabla
            df = pd.DataFrame(data)
            st.dataframe(df)

            # Resumen interactivo
            st.write("Resumen:")
            st.write(df.describe(include='all'))
        else:
            st.info("Aún no se han recibido datos del webhook.")
    else:
        st.error("Error al conectar con el backend Flask.")
except Exception as e:
    st.error(f"Error al obtener los datos: {e}")
