from flask import Flask, jsonify, request
from flask_cors import CORS
import boto3
from botocore.client import Config
from metodos import validar, cargar_archivo
from analizador import analisis
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def inicio():
 print("Hola mundo")
 return jsonify({"mensaje": "Bienvenido a la API de Python"})

@app.route('/login', methods=['POST'])
def login():
 usurio=request.json['usuario']
 contrasenia=request.json['contrasenia']
 if validar(usurio,contrasenia):
     return jsonify({"mensaje": "aceptado"})
 else:
     return jsonify({"mensaje": "rechazado"})


@app.route('/carga_archivo', methods=['POST'])
def carga():
 contenido = request.form.get('contenido')
 #ruta=request.json['ruta']
 if cargar_archivo(contenido):
     return jsonify({"mensaje": "archivo cargado"})
 else:
     return jsonify({"mensaje": "error al cargar el archivo"})  

@app.route('/linea', methods=['POST'])
def linea():
    linea = request.json['linea']
    a=analisis(linea)
    return jsonify({"linea": a.iniciar_comandos()})









if __name__ == "__main__":
 app.run(threaded=True, host="0.0.0.0", port=5000, debug=True)
