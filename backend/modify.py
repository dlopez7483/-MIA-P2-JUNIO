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






class Modify:
 def __init__(self,body,type,path):
     self.body=body
     self.type=type
     self.path=path
     self.modificar()
 def modificar(self):
     if self.type=="Server":
         root=str('Archivos')+self.path
         path_correcto=os.path.exists(root)
         if(path_correcto):
             if re.search(r"\.txt$",root, re.I):
                  with open(root, 'w') as archivo:
                     archivo.write(self.body)
                     #rcontenido("Archivo Modificado")
             archivo.close()
             return "Archivo"+self.path+" modificado con éxito."
         else:
             return "El archivo "+self.path+" no existe."
     elif self.type=="Bucket":
            response = s3_client.list_objects_v2(Bucket='bucket201907483', Prefix='Archivos'+self.path)
            existencia = response.get('Contents', [])
            if existencia:
                try:
                 s3_client.delete_object(Bucket='bucket201907483', Key='Archivos'+self.path)
                 s3_client.put_object(Body=self.body, Bucket='bucket201907483', Key='Archivos'+self.path)
                 return "Archivo "+self.path+" modificado con éxito."
                except Exception as e:
                 return "Error al modificar el archivo en el bucket:", str(e)
            else:
             return "El archivo "+self.path+" no existe."

