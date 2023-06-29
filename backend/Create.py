from pathlib import Path
import boto3
from botocore.client import Config
from bitacora import bit 


s3_client = boto3.client(
     's3',
     aws_access_key_id='AKIAVUJFRDVNRXAMFOH6',
     aws_secret_access_key='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',
     config=Config(signature_version='s3v4')
     )

class Create:
    def __init__(self, name, body, type, path):
        self.name = name
        self.body = body
        self.type = type
        self.path = path
        

    def crear(self):
        if self.type == "Server":
         carpetas = self.path.split("/")
         cadena = str(Path.home() / 'Archivos') + "/"
         for i in range(1, len(carpetas) - 1):
             cadena += carpetas[i] + "/"
             ruta = Path(cadena)
             print(cadena)
             if not ruta.exists():
                 ruta.mkdir(parents=True)

         ruta_archivo = Path(cadena + self.name)
         try:
             archivo = open(ruta_archivo, 'w')
             archivo.write(self.body)
             archivo.close()
             bit.insertar_log("Archivo" + self.path + self.name + "creado")
             return "Archivo" + self.path + self.name + "creado"
         except Exception as e:
             bit.insertar_log("No se pudo crear el archivo")
             return "No se pudo crear el archivo:", str(e)

        elif self.type == "Bucket":
         ruta_archivo = "Archivos" + self.path + self.name
         try:
             s3_client.put_object(Body=self.body, Bucket='bucket201907483', Key=ruta_archivo)
             bit.insertar_log("Archivo" + self.path + self.name + "creado")
             return "Archivo" + self.path + self.name + "creado"
         except Exception as e:
             bit.insertar_log("No se pudo crear el archivo")
             return "No se pudo crear el archivo:", str(e)

