from pathlib import Path
import shutil
import boto3
from botocore.client import Config
import re
import os
from bitacora import bit 
s3_client = boto3.client(
     's3',
     aws_access_key_id='AKIAVUJFRDVNRXAMFOH6',
     aws_secret_access_key='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',
     config=Config(signature_version='s3v4')
     )


class renombrar:
 def __init__(self, path, name, type):
     self.name = name
     self.type = type
     self.path = path


 def renombrar_(self):
     if self.type=="Server":
         ruta=str(os.getcwd()/'Archivos')+self.path
         existencia_path = os.path.exists(ruta)
         if(existencia_path):
             if re.search(r"\.txt$",ruta, re.I):
                 try:
                     nombre_directorio, nombre_archivo = os.path.split(ruta)

                     nombre_base, extension = os.path.splitext(nombre_archivo)

                     nuevo_nombre_archivo = self.name
    
                     nueva_ruta = os.path.join(nombre_directorio, nuevo_nombre_archivo)
                
                     os.rename(ruta, nueva_ruta)
                     bit.insertar_log("Archivo "+self.path+" renombrado con éxito como "+self.name+".")
                     return "Archivo "+self.path+" renombrado con éxito como "+self.name+"."
                 except:
                     bit.insertar_log("Error al renombrar el archivo." )
                     return "Error al renombrar el archivo."  
             else:
                 try:
                     carpetas=ruta.split("/")
                     cadena=""
                     for c in range(len(carpetas)-2):
                         cadena+=carpetas[c]+"/"
                     cadena+=carpetas[len(carpetas)-2]
            
                     nombre_directorio, nombre_carpeta = os.path.split(cadena)
            
                     nuevo_directorio = os.path.join(nombre_directorio,self.name)
               
                     os.rename(ruta, nuevo_directorio)
                 except:
                      bit.insertar_log("Error al renombrar el archivo." )
                      return "Error al renombrar el archivo."
     elif self.type=="Bucket":
         try:
             div=self.path.split("/")
             cadena=""
             for c in range(len(div)-1):
                 cadena+=div[c]+"/"
              

             s3_client.copy_object(Bucket='bucket201907483', CopySource={'Bucket': 'bucket201907483', 'Key': 'Archivos'+self.path}, Key='Archivos'+cadena+self.name)
             s3_client.delete_object(Bucket='bucket201907483', Key='Archivos'+self.path)
             bit.insertar_log("Archivo "+self.path+" renombrado con éxito como "+self.name+".")
             return "Archivo "+self.path+" renombrado con éxito como "+self.name+"."
         except Exception as e:
             bit.insertar_log("Error al renombrar el archivo en el bucket" )
             return "Error al renombrar el archivo en el bucket:", str(e)
            
