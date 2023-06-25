from flask import Flask, jsonify, request
from flask_cors import CORS
import boto3
from botocore.client import Config
from metodos import validar, cargar_archivo

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
 ruta=request.json['ruta']
 if cargar_archivo(ruta):
     return jsonify({"mensaje": "archivo cargado"})
 else:
     return jsonify({"mensaje": "error al cargar el archivo"})  


@app.route('/create', methods=['POST'])
def create():
 name=request.json['name']
 body=request.json['body']
 path=request.json['path']
 type=request.json['type']



@app.route('/delete', methods=['DELETE'])
def delete():
 path=request.json['path']
 name=request.json['name']
 type=request.json['type']




@app.route('/copy', methods=['POST'])
def copiar():
 from_=request.json['from']
 to=request.json['to']
 type_to=request.json['type_to']
 type_from=request.json['type_from']


@app.route('/transfer', methods=['POST'])
def transferir():
 from_=request.json['from']
 to=request.json['to']
 type_to=request.json['type_to']
 type_from=request.json['type_from']


@app.route('/Rename', methods=['PUT'])
def rename():
 path=request.json['path']
 name=request.json['name']
 type=request.json['type']


@app.route('/modify', methods=['PUT'])
def modify():
 path=request.json['path']
 type=request.json['type']
 body=request.json['body']


@app.route('/backup', methods=['POST'])
def backup():
 type_to=request.json['type_to']
 type_from=request.json['type_from']
 ip=request.json['ip']
 port=request.json['port']


@app.route('/Recovey', methods=['POST'])
def recovey():
 type_to=request.json['type_to']
 type_from=request.json['type_from']
 ip=request.json['ip']
 port=request.json['port']
 name=request.json['name']

@app.route('/delete_all', methods=['DELETE'])
def delete_all():
 type=request.json['type']

@app.route('/open', methods=['POST'])
def abrir():
 type=request.json['type']
 ip=request.json['ip']
 port=request.json['port']
 name=request.json['name']









if __name__ == "__main__":
 app.run(threaded=True, host="0.0.0.0", port=5000, debug=True)
