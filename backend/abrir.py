from pathlib import Path
import shutil
import boto3
from botocore.client import Config
import re
import os
s3_client = boto3.client(
    's3',
    aws_access_key_id='AKIAVUJFRDVN5ZXYPPVS',
    aws_secret_access_key='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',
    config=Config(signature_version='s3v4')
)



class abrir:
 def __init__(self,type,ip,port,name):
     self.type=type
     self.ip=ip
     self.port=port
     self.name=name
 def abrir_(self):
     try:
         if self.ip=="" and self.port=="":
             if self.type=="Server":
                 with open(str(Path.home() / 'Archivos/') + self.name, 'r') as archivo:
                     contenido = archivo.read().decode('utf-8')
                     print(contenido)
                     return contenido
             elif self.type=="Bucket":
                    response = s3_client.list_objects_v2(Bucket='bucket201907483', Prefix='Archivos/'+self.name)
                    existencia = response.get('Contents', [])
                    if existencia:
                        try:
                            objeto = s3_client.get_object(Bucket='bucket201907483', Key='Archivos/'+self.name)
                            contenido = objeto['Body'].read().decode('utf-8')
                            print(contenido)
                            return contenido
                        except Exception as e:
                            print("Error al descargar el archivo en el bucket:", str(e))
                    else:
                        print("Error en el path")
     except:
         print("no se pudo abrir el archivo")
                 