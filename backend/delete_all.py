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




class delete_all:
 def __init__(self,type):
     self.type=type
  
 def eliminar(self):
     if self.type=="Server":
         root=str(Path.home()/'Archivos/')
         try:
             for nombre_archivo in os.listdir(str(root)):
                    ruta_completa_origen = os.path.join(str(root), nombre_archivo)
                    if os.path.isfile(ruta_completa_origen):
                     os.remove(ruta_completa_origen)
                    else:
                     shutil.rmtree(ruta_completa_origen)
             return "Archivos del server eliminados con éxito."    
         except FileNotFoundError:
             return "La carpeta "+self.path+" no existe."
     elif self.type=="Bucket":
         response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos/")
         
         objetos = response.get('Contents', [])
         if objetos:
             for obj in objetos:
                 obj2=obj.get('Contents', [])
                 if obj2:
                     self.eliminar_carpeta_bucket("Archivos/"+obj['Key'])
                 else:
                     s3_client.delete_object(Bucket='bucket201907483', Key=obj['Key'])
         return "Archivos del bucket eliminados con éxito."

 def eliminar_carpeta_bucket(self,ruta):
     response = s3_client.list_objects(Bucket='bucket201907483', Prefix=ruta)
     objetos = response.get('Contents', [])
     if objetos:
         for obj in objetos:
             obj2=obj.get('Contents', [])
             if obj2:
                 self.eliminar_carpeta_bucket(ruta+obj['Key'])
             else:
                 s3_client.delete_object(Bucket='bucket201907483', Key=obj['Key'])

