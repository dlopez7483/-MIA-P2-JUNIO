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



 def copiar_bucket_bucket(self):
     response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos"+self.to)
     existencia = response.get('Contents', [])
     response2 = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos"+self.desde)
     existencia2 = response.get('Contents', [])
    
     if existencia2 and existencia:
         try:
            if re.search(r"\.txt$", self.desde, re.I):
                 s3_client.copy_object(Bucket='bucket201907483', CopySource={'Bucket': 'bucket201907483', 'Key': 'Archivos'+self.desde}, Key='Archivos'+self.to)
            else:
             response = s3_client.list_objects_v2(Bucket='bucket201907483', Prefix='Archivos'+self.desde)
             for obj in response['Contents']:
                 ruta_objeto_origen = obj['Key']
                 ruta_objeto_destino = 'Archivos'+self.to + ruta_objeto_origen[len('Archivos'+self.desde):]
                 s3_client.copy_object(
                 CopySource={'Bucket':'bucket201907483', 'Key': ruta_objeto_origen},
                 Bucket='bucket201907483',
                 Key=ruta_objeto_destino
                 )
                 print("copiado exitosamente de bucket a bucket")
         except Exception as e:
             print("Error al copiar el archivo del bucket a bucket:", str(e))
          
             

 def copiar_server_bucket(self):
     response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos"+self.to)
     existencia = response.get('Contents', [])
     root=str(Path.home()/'Archivos')
     ruta_archivo = Path(root+self.desde)
     if ruta_archivo.exists() and existencia:
         if re.search(r"\.txt$", self.desde, re.I):
             division=self.desde.split("/")
             s3_client.upload_file(str(ruta_archivo),'bucket201907483',"Archivos"+self.to+division[len(division)-1])
          
             print("Archivo copiado exitosamente de local a bucket.")
         else:
             for nombre_archivo in os.listdir(str(ruta_archivo)):
                 ruta_completa_origen = os.path.join(str(ruta_archivo), nombre_archivo)
                 if os.path.isfile(ruta_completa_origen):
                     s3_client.upload_file(str(ruta_completa_origen),'bucket201907483', 'Archivos'+self.to+nombre_archivo)
                 else:
                     self.carpetas(ruta_completa_origen,'Archivos'+self.to,nombre_archivo)
                 

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
 
 
 
 def copiar_server_server(self):
     ruta=str(Path.home()/'Archivos')
     fro = ruta+ self.desde
     t = ruta+ self.to

     existencia_desde = os.path.exists(str(fro))
     existencia_to = os.path.exists(str(t))

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
             print(ruta)
         
         if not existencia_to:
             print("La ruta de destino no existe.")
             print(t)

 def copiar_bucket_server(self):
     response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos"+self.desde)
     existencia = response.get('Contents', [])
     root=str(Path.home()/'Archivos')
     ruta_archivo = Path(root+self.to)
     if ruta_archivo.exists() and existencia:
         try:
             if re.search(r"\.txt$", self.desde, re.I):
                 s3_client.download_file('bucket201907483',"Archivos"+self.desde,str(ruta_archivo))
                 print("Archivo copiado exitosamente del bucket a local.")
             else:
                 response = s3_client.list_objects(Bucket='bucket201907483', Prefix="Archivos"+self.desde)
    
                 for obj in response['Contents']:
                     s3_key = obj['Key']
                     local_file_path = os.path.join(ruta_archivo, s3_key[len("Archivos"+self.desde):])
        
                     if not os.path.exists(os.path.dirname(local_file_path)):
                         os.makedirs(os.path.dirname(local_file_path))
        
            
                     s3_client.download_file('bucket201907483', s3_key, local_file_path)
         except Exception as e:
             print("Error al copiar el archivo del bucket a local:", str(e))
    
         
c=copiar("/prueba1/","/carpeta1/","Server","Server")
c.copiar_()