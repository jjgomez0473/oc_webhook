from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para procesar el JSON enviado por OptimoCamino
@app.route('/webhook/optimo_camino', methods=['POST'])
def webhook_optimo_camino():
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

    # Aquí puedes realizar cualquier operación que desees con los datos JSON capturados
    # Por ejemplo, imprimirlos
    print("JSON recibido de OptimoCamino:", data)

    # Dependiendo del valor de 'par_confirmada', puedes realizar acciones específicas
    if data['par_confirmada'] == 'confirmada':
        # Realizar acciones cuando se confirma la parada
        pass
    elif data['par_confirmada'] == 'cancelada':
        # Realizar acciones cuando se cancela la parada
        pass

    return jsonify({"message": "JSON procesado exitosamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)
