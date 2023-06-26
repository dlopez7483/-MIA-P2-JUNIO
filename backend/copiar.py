import shutil
import re
import os
import boto3
from pathlib import Path
from botocore.client import Config


s3_client = boto3.client(
    's3',
    aws_access_key_id='AKIAVUJFRDVN5ZXYPPVS',
    aws_secret_access_key='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',
    config=Config(signature_version='s3v4')
)





class copiar:
 def __init__(self,desde,to,type_to,type_from):
     self.desde=desde
     self.to=to
     self.type_to=type_to
     self.type_from=type_from
     self.copiar_()

 def copiar_(self):
     if(self.type_to=="Server" and self.type_from=="Server"):
         print("Copiando de local a local")
         self.copiar_server_server()
     elif(self.type_to=="Server" and self.type_from=="Bucket"):
         print("Copiando de Bucket a local")
         self.copiar_bucket_server()
     elif(self.type_to=="Bucket" and self.type_from=="Server"):
         print("Copiando de local a Bucket")
         self.copiar_server_bucket()
     elif(self.type_to=="Bucket" and self.type_from=="Bucket"):
         print("Copiando de Bucket a Bucket")
         self.copiar_bucket_bucket()

 def copiar_server_bucket(self):
     response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos"+self.to)
     existencia = response.get('Contents', [])
     root=str(Path.home()/'Archivos')
     ruta_archivo = Path(root+self.desde)
     if ruta_archivo.exists() and existencia:
         try:
             s3_client.upload_file(str(ruta_archivo),'bucket201907483',"Archivos"+self.to)
             print("Archivo copiado exitosamente de local al bucket.")
         except Exception as e:
             print("Error al copiar el archivo de local al bucket:", str(e))



 def copiar_server_server(self):
     ruta=str(Path.home()/'Archivos')
     fro = os.path.join(ruta, self.desde)
     t = os.path.join(ruta, self.to)
     existencia_desde = os.path.exists(fro)
     existencia_to = os.path.exists(t)

     if existencia_desde and existencia_to:
         if re.search(r"\.txt$", self.desde, re.I):
             shutil.copy(self.desde, self.to)
             print("El archivo ha sido copiado.")
                
         else:
             for root, dirs, files in os.walk(fro):
                 for file in files:
                     src_file = os.path.join(root, file)
                     rel_path = os.path.relpath(src_file, fro)
                     dst_file = os.path.join(t, rel_path)
                     os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                     shutil.copy2(src_file, dst_file)
                
     else:
         if not existencia_desde:
             print("La ruta de origen no existe.")
         
         if not existencia_to:
             print("La ruta de destino no existe.")

 def copiar_bucket_server(self):
     response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos"+self.desde)
     existencia = response.get('Contents', [])
     root=str(Path.home()/'Archivos')
     ruta_archivo = Path(root+self.to)
     if ruta_archivo.exists() and existencia:
         try:
             s3_client.download_file('bucket201907483',"Archivos"+self.desde,str(ruta_archivo))
             print("Archivo copiado exitosamente del bucket a local.")
         except Exception as e:
             print("Error al copiar el archivo del bucket a local:", str(e))
    
         
                     