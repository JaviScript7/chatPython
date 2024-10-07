from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://monguito:password@db_monguito:27017/chat_db?authSource=admin'  # Ajusta según tu configuración

mongo = PyMongo(app)

@app.route('/test_connection', methods=['GET'])
def test_connection():
    try:
        mongo.db.command('ping')  # Este comando verifica la conexión
        return "Conexión exitosa a MongoDB", 200
    except Exception as e:
        return f"Error al conectar a MongoDB: {str(e)}", 500


@app.route('/insert', methods=['POST'])
def insert_document():
    # Datos de ejemplo que deseas insertar
    document = {
        "message": "¡Hola desde Flask!",
        "author": "Usuario"
    }
    
    # Inserta el documento en la colección 'messages'
    mongo.db.messages.insert_one(document)
    
    return "Documento insertado con éxito", 201

@app.route('/fetch', methods=['GET'])
def fetch_documents():
    # Recupera todos los documentos de la colección 'messages'
    messages = mongo.db.messages.find()
    
    # Crea una lista para almacenar los resultados
    results = []
    for msg in messages:
        results.append({"message": msg["message"], "author": msg["author"]})

    return {"messages": results}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
