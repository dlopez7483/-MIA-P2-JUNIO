from flask import Flask, jsonify, request
from flask_cors import CORS
import boto3
from botocore.client import Config

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def inicio():
 print("Hola mundo")
 return jsonify({"mensaje": "Bienvenido a la API de Python"})

if __name__ == "__main__":
 app.run(threaded=True, host="0.0.0.0", port=5000, debug=True)
