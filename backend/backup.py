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


class backup:
 def __init__(self,type_to,type_from,ip,port,name):
     self.type_to=type_to
     self.type_from=type_from
     self.ip=ip
     self.port=port
     self.name=name
     self.backup_()

 def backup_(self):
     if self.port=="" and self.ip=="":
         if self.type_from=="Server" and self.type_to=="Bucket":
                try:
                    ruta_archivo = Path(str(Path.home() / 'Archivos'))
                    if ruta_archivo.exists():
                        for nombre_archivo in os.listdir(str(ruta_archivo)):
                         ruta_completa_origen = os.path.join(str(ruta_archivo), nombre_archivo)
                         if os.path.isfile(ruta_completa_origen):
                             s3_client.upload_file(str(ruta_completa_origen),'bucket201907483', 'Archivos/'+self.name+'/'+nombre_archivo)
                         else:
                             self.server_bucket_propio_carpetas(ruta_completa_origen,nombre_archivo)

                    else:
                        print("El archivo no existe.")
                except:
                    print("no se pudo subir el archivo")
         elif self.type_from=="Bucket" and self.type_to=="Server":
                try:
                     response = s3_client.list_objects_v2(Bucket='bucket201907483', Prefix='Archivos/')
                     ruta=Path(str(Path.home() / +'Archivos'+"/"+self.name))
                     if not ruta.exists():
                         ruta.mkdir(parents=True)
                     for obj in response['Contents']:
                         ruta_archivo = Path(str(Path.home() / +'Archivos'+"/"+self.name)+obj['Key'])
                    
                         s3_client.download_file('bucket201907483', obj['Key'], str(ruta_archivo))
                except:
                    print("no se pudo descargar el archivo")


          
 def server_bucket_propio_carpetas(self,ruta_completa_origen,nombre_archivo):
     if os.path.isfile(ruta_completa_origen):
         s3_client.upload_file(str(ruta_completa_origen),'bucket201907483', 'Archivos/'+self.name+'/'+nombre_archivo)
     else:
         for nombre_archivo2 in os.listdir(str(ruta_completa_origen)):
             ruta_completa_origen2 = os.path.join(str(ruta_completa_origen), nombre_archivo2)
             if os.path.isfile(ruta_completa_origen2):
                 s3_client.upload_file(str(ruta_completa_origen2),'bucket201907483', 'Archivos/'+self.name+'/'+nombre_archivo+'/'+nombre_archivo2)
             else:
                 self.server_bucket_propio_carpetas(ruta_completa_origen2,nombre_archivo2)
     
     