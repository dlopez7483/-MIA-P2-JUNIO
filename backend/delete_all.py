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




class delete_all:
 def __init__(self,type):
     self.type=type
     self.eliminar()
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
            
         except FileNotFoundError:
             print("La carpeta no existe")
     elif self.type=="Bucket":

