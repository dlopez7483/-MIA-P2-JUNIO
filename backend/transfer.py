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


class transfer:
 def __init__(self, desde, to, type_to, type_from):
     self.desde = desde
     self.to = to
     self.type_to = type_to
     self.type_from = type_from
     self.transfer_()
 def transfer_(self):
     try:
         if(self.type_to=="Server" and self.type_from=="Server"):
             print("Transfiriendo de local a local")
             self.transfer_server_server()
         elif(self.type_to=="Server" and self.type_from=="Bucket"):
             print("Transfiriendo de Bucket a local")
             self.transfer_bucket_server()
         elif(self.type_to=="Bucket" and self.type_from=="Server"):
             print("Transfiriendo de local a Bucket")
             self.transfer_server_bucket()
         elif(self.type_to=="Bucket" and self.type_from=="Bucket"):
             print("Transfiriendo de Bucket a Bucket")
             self.transfer_bucket_bucket()
     except:
         print("No se pudo transferir el archivo")
 
 
 def transfer_server_bucket(self):
     response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos"+self.to)
     existencia = response.get('Contents', [])
     root=str(Path.home()/'Archivos')
     ruta_archivo = Path(root+self.desde)
     if ruta_archivo.exists() and existencia:
         if re.search(r"\.txt$", self.desde, re.I):
             division=self.desde.split("/")
             s3_client.upload_file(str(ruta_archivo),'bucket201907483',"Archivos"+self.to+division[len(division)-1])
             ruta_archivo.unlink()
             print("Archivo copiado exitosamente de local a bucket.")
         else:
             for nombre_archivo in os.listdir(str(ruta_archivo)):
                 ruta_completa_origen = os.path.join(str(ruta_archivo), nombre_archivo)
                 if os.path.isfile(ruta_completa_origen):
                     s3_client.upload_file(str(ruta_completa_origen),'bucket201907483', 'Archivos'+self.to+nombre_archivo)
                     os.remove(ruta_completa_origen)
                 else:
                     self.carpetas(ruta_completa_origen,'Archivos'+self.to,nombre_archivo)
                     shutil.rmtree(ruta_completa_origen)
                 

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

 def transfer_server_server(self): 
     ruta=str(Path.home()/'Archivos')
     fro = ruta+ self.desde
     t = ruta+ self.to

     existencia_desde = os.path.exists(str(fro))
     existencia_to = os.path.exists(str(t))

     if existencia_desde and existencia_to:
         if re.search(r"\.txt$", self.desde, re.I):
             shutil.copy(self.desde, self.to)
             ruta_archivo = Path(fro)
             ruta_archivo.unlink()
             
                
         else:
             for root, dirs, files in os.walk(fro):
                 for file in files:
                     src_file = os.path.join(root, file)
                     rel_path = os.path.relpath(src_file, fro)
                     dst_file = os.path.join(t, rel_path)
                     os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                     shutil.copy2(src_file, dst_file)
                     rut=Path(src_file)
                     rut.unlink()
                 
                     
            
     else:
         if not existencia_desde:
             print("La ruta de origen no existe.")
             print(ruta)
         
         if not existencia_to:
             print("La ruta de destino no existe.")
             print(t)

t=transfer("/prueba1/","/prueba2/","Server","Server")