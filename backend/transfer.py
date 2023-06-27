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
 def transfer(self):
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
 def transfer_server_server(self):
        try:
            ruta_archivo = Path(str(Path.home() / 'Archivos') + self.to)
            ruta_archivo2 = Path(str(Path.home() / 'Archivos') + self.desde)
            if ruta_archivo.exists():
             if re.search(r"\.txt$", self.desde, re.I):
                 if ruta_archivo2.exists():
                     nombre=self.desde.split("/")
                     nombre_ar=nombre[len(nombre)-1].split(".")
                     nombre_base=nombre_ar[0]
                
                     contador = 1
                     
                     while True:
                         extension="."+nombre_ar[1]
                         nuevo_nombre_archivo = f"{nombre_base}_{contador}{extension}"
                         ruta_completa_destino = os.path.join(str(Path.home() / 'Archivos') + self.to, nuevo_nombre_archivo)
                         if not os.path.exists(ruta_completa_destino):
                             break
                         contador += 1
                 shutil.copy2(ruta_completa_origen, ruta_completa_destino)
                 for nombre_archivo in os.listdir(str(ruta_archivo)):
                     ruta_completa_origen = os.path.join(str(ruta_archivo), nombre_archivo)
                     ruta_completa_destino = os.path.join(str(ruta_archivo2), nombre_archivo)
                     if os.path.isfile(ruta_completa_origen):
                         if os.path.exists(ruta_completa_destino):
                
                             contador = 1
                             nombre_base, extension = os.path.splitext(nombre_archivo)
                             while True:
                                 nuevo_nombre_archivo = f"{nombre_base}_{contador}{extension}"
                                 ruta_completa_destino = os.path.join(str(Path.home() / 'Archivos') + self.to, nuevo_nombre_archivo)
                                 if not os.path.exists(ruta_completa_destino):
                                     break
                                 contador +=1
                     shutil.copy2(ruta_completa_origen, ruta_completa_destino) 
                    
            else:
             print("El archivo no existe")
        except Exception as e:
            print("Error al copiar el archivo:", str(e))
 def transfer_bucket_server(self):
        
        try:
         response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos"+self.desde)
         existencia = response.get('Contents', [])
         root=str(Path.home()/'Archivos')
         ruta_archivo = Path(root+self.to)
         if ruta_archivo.exists() and existencia:
             if re.search(r"\.txt$", self.desde, re.I):
                 nombre=self.desde.split("/")
                 if Path(root+self.to+nombre[len(nombre)-1]).exists():
                     nombre=self.desde.split("/")
                     nombre_ar=nombre[len(nombre)-1].split(".")
                     nombre_base=nombre_ar[0]
                
                     contador = 1
                     while True:
                         extension=nombre_ar[1]
                         extension="."+nombre_ar[1]
                         nuevo_nombre_archivo = f"{nombre_base}_{contador}{extension}"
                         ruta_completa_destino = os.path.join(str(Path.home() / 'Archivos') + self.to, nuevo_nombre_archivo)
                         if not os.path.exists(ruta_completa_destino):
                             break
                         contador += 1
                     s3_client.download_file('bucket201907483',self.desde, ruta_completa_destino)
                
                
             else:
                 for root, dirs, files in os.walk(root+self.desde):
                     for file in files:
                         ruta_archivo_local = os.path.join(root, file)
                         ruta_archivo_bucket = os.path.join('Archivos'+self.to, os.path.relpath(ruta_archivo_local,root+self.desde))
                         try:
                             s3_client.download_file('bucket201907483', ruta_archivo_bucket, ruta_archivo_local)
                             print("Archivo copiado exitosamente de bucket a local.")
                         except Exception as e:
                             print(str(e))
         else:
             print("El archivo no existe")
        except Exception as e:
            print("Error al copiar el archivo del bucket a local:", str(e))
