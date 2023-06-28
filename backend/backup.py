from pathlib import Path
import shutil
import boto3
from botocore.client import Config
import re
import os
from copiar import copiar
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
         if self.type_from=="Bucket" and self.type_to=="Server":
             ruta = Path(str(Path.home() / 'Archivos')+"/"+self.name+"/")
             if not ruta.exists():
                 ruta.mkdir(parents=True)
             self.copiar_bucket_server()
         elif self.type_from=="Server" and self.type_to=="Bucket":
             self.copiar_server_bucket()   
 
 def copiar_bucket_server(self):
     response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos/")
     existencia = response.get('Contents', [])
     root=str(Path.home()/'Archivos')
    
     ruta_archivo = Path(root+"/"+self.name+"/")
     response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos/")
    
     for obj in response['Contents']:
         s3_key = obj['Key']
         print(s3_key)
         local_file_path = os.path.join(ruta_archivo, s3_key[len("Archivos/"):])
        
         if not os.path.exists(os.path.dirname(local_file_path)):
             os.makedirs(os.path.dirname(local_file_path))
         try:
             s3_client.download_file('bucket201907483', s3_key, local_file_path)
         except Exception as e:
             print(e)
             

 def copiar_server_bucket(self):
     response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos/")
     existencia = response.get('Contents', [])
     root=str(Path.home()/'Archivos')
     ruta_archivo = Path(root)
     if ruta_archivo.exists() and existencia:
         for nombre_archivo in os.listdir(str(ruta_archivo)):
             ruta_completa_origen = os.path.join(str(ruta_archivo), nombre_archivo)
             if os.path.isfile(ruta_completa_origen):
                 s3_client.upload_file(str(ruta_completa_origen),'bucket201907483', 'Archivos/'+self.name+"/"+nombre_archivo)
             else:
                 self.carpetas(ruta_completa_origen,'Archivos/'+self.name+"/",nombre_archivo)
         
 def carpetas(self,ruta_completa_origen,to,nombre_archivo):
     print("entro")
     if os.path.isfile(ruta_completa_origen):
         s3_client.upload_file(str(ruta_completa_origen),'bucket201907483',to+nombre_archivo)
     else:
         print("aaaaa")
         for nombre_archivo2 in os.listdir(str(ruta_completa_origen)):
             ruta_completa_origen2 = os.path.join(str(ruta_completa_origen), nombre_archivo2)
             if os.path.isfile(ruta_completa_origen2):
                 s3_client.upload_file(str(ruta_completa_origen2),'bucket201907483',to+nombre_archivo+'/'+nombre_archivo2)
             else:
                 
                 self.carpetas(ruta_completa_origen2,to+nombre_archivo,nombre_archivo2)      
     

          
c=backup("Bucket","Server","","","champion")
     
     