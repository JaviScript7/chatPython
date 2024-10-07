# chatPython
### Aplicacion de Chat con Flask y Socket.IO

Este es un proyecto de chat en tiempo real desarrollado con Flask y Socket.IO, utilizando MongoDB para almacenar los usuarios y los mensajes.

## Características

- Registro de usuarios con contraseña.
- Inicio de sesión.
- Envío y recepción de mensajes en tiempo real.
- Almacenamiento de mensajes en MongoDB.

## Tecnologías Utilizadas

- **Flask**: Framework web para Python.
- **Flask-SocketIO**: Extensión para Flask que facilita la comunicación en tiempo real.
- **Flask-PyMongo**: Extensión que permite interactuar fácilmente con MongoDB.
- **bcrypt**: Biblioteca para el hashing de contraseñas.
- **MongoDB**: Base de datos NoSQL para almacenar datos.
- **Docker**: Se utilizo contenedores para garantizar la compatibilidad

## Requisitos

- Python 3.7 o superior
- MongoDB
- Docker | Docker compose -> Si no cuentas con docker tambien lo puedes ejecutar en un entorno virtual de python
- Dependencias de Python:
  - Flask
  - Flask-SocketIO
  - Flask-PyMongo
  - bcrypt
  - eventlet
## Instalación con Docker
El objetivo de usar docker es garantizar la compatibilidad a si mismo sea mas fácil

1. Clona el repositorio:

   ```bash
   git clone https://github.com/JaviScript7/chatPython.git
   cd chatPython
2. Construir y ejecutar el contenedor
   Esto iniciará tanto la aplicación Flask como una instancia de MongoDB.
    ```bash
    docker-compose up -d --build


3. La aplicacion estará disponible en: **http://localhost:5000**

## Instalación sin Docker (opcional)

1. Clona el repositorio:

   ```bash
   git clone https://github.com/JaviScript7/chatPython.git
   cd chatPython

2. Crear un entorno virtual para python con virtualenv
    ```bash
    pip install virtualenv (esto puede varias segun el sistema operativo)
    virutalenv python3 --python=python3
    source python3/bin/activate  (Sistema UNIX)
    
3. Instalar las dependencias
    ```bash
    pip install -r requirements.txt

4. Asegurate que este corriendo mongoDB

5. Ejecuta la aplicacion
    ```bash
    python app.py




