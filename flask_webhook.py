from flask import Flask, request, jsonify
import threading
import os
import json

app = Flask(__name__)

# Variable global para almacenar los datos del webhook
webhook_data = []

@app.route('/webhook', methods=['POST'])
def webhook_optimo_camino():
    global webhook_data

    # Verificamos si se proporcionó un JSON en el cuerpo de la solicitud
    if not request.json:
        return jsonify({"error": "No se proporcionó JSON en la solicitud"}), 400

    # Verificamos si el JSON contiene los campos necesarios
    required_fields = ['token', 'par_id', 'par_confirmada', 'fecha_hora', 'par_notas', 'par_notas_chofer']
    for field in required_fields:
        if field not in request.json:
            return jsonify({"error": f"Falta el campo '{field}' en el JSON"}), 400

    # Capturamos y procesamos el JSON
    data = request.json
    webhook_data.append(data)  # Agregamos los datos a la lista global

    print("JSON recibido de OptimoCamino:", data)

    return jsonify({"message": "JSON procesado exitosamente"}), 200

@app.route('/get_data', methods=['GET'])
def get_data():
    # Proporcionamos los datos en formato JSON para que Streamlit pueda acceder
    return jsonify(webhook_data)

def run_streamlit():
    os.system("streamlit run streamlit_app.py --server.port 8501")

if __name__ == '__main__':
    # Iniciar Streamlit en un hilo aparte
    threading.Thread(target=run_streamlit).start()

    # Ejecutar el servidor Flask
    app.run(host='0.0.0.0', port=80, debug=True)
