from flask import Flask, render_template, request, redirect, session, url_for
from flask_socketio import SocketIO, emit
from flask_pymongo import PyMongo
import bcrypt
from bson import ObjectId

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['MONGO_URI'] = 'mongodb://monguito:password@db_monguito:27017/chat_db?authSource=admin'
mongo = PyMongo(app)
socketio = SocketIO(app)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('chat.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = mongo.db.users.find_one({'username': username})
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            session['username'] = username
            return redirect(url_for('index'))
        return 'Usuario o contraseña incorrectos', 400
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        mongo.db.users.insert_one({'username': username, 'password': hashed})
        return redirect(url_for('login'))
    return render_template('registro.html')

@socketio.on('send_message')
def handle_message(data):
    print(f"Received data: {data}")  # Imprimir para depurar
    message_data = {
        'username': data['username'],
        'message': data['message'],
        # No generamos un nuevo ObjectId aquí
    }

    mongo.db.messages.insert_one(message_data)  # Guardar en MongoDB
    message_data['_id'] = str(mongo.db.messages.find_one({'username': data['username'], 'message': data['message']})['_id'])

    print(f"Message data to send: {message_data}")  # Imprimir para depurar

    try:
        emit('receive_message', message_data, broadcast=True)
    except Exception as e:
        print(f"Error while emitting message: {e}")

@socketio.on('connect')
def handle_connect():
    username = session.get('username', 'Anonimo')
    emit('message', {'username': username, 'message': f"{username} se ha unido al chat."}, broadcast=True)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
