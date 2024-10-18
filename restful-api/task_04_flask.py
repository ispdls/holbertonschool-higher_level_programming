from flask import Flask, jsonify, request

# Instanciar la aplicación Flask
app = Flask(__name__)

# Diccionario para almacenar usuarios en memoria
users = {}

# Endpoint para la raíz
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint para obtener todos los usuarios
@app.route('/data', methods=['GET'])
def get_users():
    return jsonify(list(users.keys()))

# Endpoint para verificar el estado de la API
@app.route('/status', methods=['GET'])
def status():
    return "OK"

# Endpoint para obtener información de un usuario específico
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint para agregar un nuevo usuario
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    # Verificar que el nombre de usuario esté presente
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

# Ejecutar el servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
