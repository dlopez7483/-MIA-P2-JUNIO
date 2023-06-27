from pathlib import Path
import shutil
import boto3
from botocore.client import Config


s3_client = boto3.client(
    's3',
    aws_access_key_id='AKIAVUJFRDVN5ZXYPPVS',
    aws_secret_access_key='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',
    config=Config(signature_version='s3v4')
)

class delete:
 def __init__(self,path,name,type):
     self.path=path
     self.name=name
     self.type=type
   
 def eliminar(self):
     if self.type=="Server":
         root=str(Path.home()/'Archivos')
         if self.name!="":
             try:
                 ruta_archivo = Path(root+self.path+self.name)
                 if ruta_archivo.exists():
                     ruta_archivo.unlink()
                     print("Archivo eliminado con éxito.")
                 else:
                     print("El archivo no existe.")

             except:
                 print("no se pudo eliminar el archivo")   
         elif self.name=="":
             try:
                 if shutil.os.path.exists(root+self.path):
                      shutil.rmtree(root+self.path)
                      print("Carpeta eliminada con éxito.")
                 else:
                     print("La carpeta no existe.")
                
             except FileNotFoundError:
                 print("La carpeta no existe")
                
                     
     elif self.type=="Bucket":
            try:
                if self.name!="":
                 ruta_archivo = "Archivos"+self.path+self.name
                 response = s3_client.list_objects(Bucket='bucket201907483', Prefix=ruta_archivo)
                 objetos = response.get('Contents', [])
                 if objetos:
                     for objeto in objetos:
                         s3_client.delete_object(Bucket='bucket201907483', Key=objeto['Key'])
                     

               
                 print("Archivo eliminado con éxito.")
                else:
                     



                 ruta_archivo = "Archivos"+self.path



                 response = s3_client.list_objects(Bucket='bucket201907483', Prefix=ruta_archivo)
                 objetos = response.get('Contents', [])
                 if objetos:
                     for objeto in objetos:
                         s3_client.delete_object(Bucket='bucket201907483', Key=objeto['Key'])
        
                 s3_client.delete_object(Bucket='bucket201907483', Key=ruta_archivo)
                     
            except:
             print("no se pudo eliminar el archivo")
             


d=delete("/p/p1/","hola3.txt","Bucket")
d.eliminar()