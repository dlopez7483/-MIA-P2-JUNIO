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
                     #rcontenido("Archivo eliminado con éxito.")
                     print("Archivo eliminado con éxito.")
                 else:
                     #rcontenido("El archivo no existe.")
                     print("El archivo no existe.")

             except:
                 #rcontenido("no se pudo eliminar el archivo")
                 print("no se pudo eliminar el archivo")   
         elif self.name=="":
             try:
                 if shutil.os.path.exists(root+self.path):
                      shutil.rmtree(root+self.path)
                      #rcontenido("Carpeta eliminada con éxito.")
                      print("Carpeta eliminada con éxito.")
                 else:
                     #rcontenido("La carpeta no existe.")
                     print("La carpeta no existe.")
                
             except FileNotFoundError:
                 #rcontenido("La carpeta no existe")
                 print("La carpeta no existe")
                
                     
     elif self.type=="Bucket":
            try:
                if self.name!="":
                 ruta_archivo = "Archivos"+self.path+self.name
                 s3_client.delete_object(Bucket='bucket201907483', Key=ruta_archivo)
                 #rcontenido("Archivo eliminado con éxito.")
                 print("Archivo eliminado con éxito.")
                else:
                     



                 ruta_archivo = "Archivos"+self.path



                 response = s3_client.list_objects(Bucket='bucket201907483', Prefix=ruta_archivo)
                 objetos = response.get('Contents', [])
                 if objetos:
                     for objeto in objetos:
                         s3_client.delete_object(Bucket='bucket201907483', Key=objeto['Key'])
        
                 s3_client.delete_object(Bucket='bucket201907483', Key=ruta_archivo)
                 #rcontenido("Carpeta" + self.path + "eliminada")
                 return "Carpeta" + self.path + "eliminada"
                     
            except:
             #rcontenido("no se pudo eliminar el archivo")
             print("no se pudo eliminar el archivo")
             

