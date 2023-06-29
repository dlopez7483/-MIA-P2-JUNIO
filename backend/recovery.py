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




class recovery:
 def __init__(self,type_to,type_from,ip,port,name):
     self.type_to=type_to
     self.type_from=type_from
     self.ip=ip
     self.port=port
     self.name=name
     
 def recovery_(self):
     if self.port=="" and self.ip=="":
         if self.type_from=="Server" and self.type_to=="Bucket":
                try:
                 ruta_archivo = Path(str(os.getcwd() / 'Archivos')+"/"+self.name+"/")
                 if ruta_archivo.exists():
                     for nombre_archivo in os.listdir(str(ruta_archivo)):
                         ruta_completa_origen = os.path.join(str(ruta_archivo), nombre_archivo)
                         if os.path.isfile(ruta_completa_origen):
                             s3_client.upload_file(str(ruta_completa_origen),'bucket201907483', 'Archivos')
                             return "Recover "+self.name+" realizado exitosamente en el Bucket"
                         else:
                             self.server_bucket_propio_carpetas(ruta_completa_origen,nombre_archivo)
                 else:
                     return "El archivo "+self.name+" no existe."
                except:
                    return "No se pudo realizar el recover en el Bucket"

         elif self.type_from=="Bucket" and self.type_to=="Server":
             response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos/"+self.name+"/")
             existencia = response.get('Contents', [])
             root=str(os.getcwd()/'Archivos')
    
             ruta_archivo = Path(root)
             response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos/"+self.name+"/")
             for obj in response['Contents']:
                 s3_key = obj['Key']
                 print(s3_key)
                 local_file_path = os.path.join(ruta_archivo, s3_key[len("Archivos/"+self.name+"/"):])
        
        
                 if not os.path.exists(os.path.dirname(local_file_path)):
                      os.makedirs(os.path.dirname(local_file_path))
                 try:
                     s3_client.download_file('bucket201907483', s3_key, local_file_path)
                     return "Recover "+self.name+" realizado exitosamente en el Servidor"
                 except:
                     return "No se pudo realizar el recovery en el Servidor"
           




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