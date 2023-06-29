from pathlib import Path
import shutil
import boto3
from botocore.client import Config
import re
import os


s3_client = boto3.client(
     's3',
     aws_access_key_id='AKIAVUJFRDVNRXAMFOH6',
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
                            return "Error al abrir el archivo en el bucket:", str(e)
                    else:
                        return "El archivo "+self.name+" no existe."
     except:
         return "Error al abrir el archivo"
                 