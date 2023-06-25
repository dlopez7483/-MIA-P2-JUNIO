from pathlib import Path
from metodos import s3
class Create:
 def __init__(self,name,body,type,path):
     self.name=name
     self.body=body
     self.type=type
     self.path=path
     self.crear()
 
 def crear(self):
     if self.type=="Server":
         carpetas=self.path.split("/")
         cadena=str(Path.home()/'Archivos')+"/"
         for i in range(1,len(carpetas)-1):
             cadena+=carpetas[i]+"/"
             ruta=Path(cadena)
         print(cadena)
         if not (ruta.exists()):
             ruta.mkdir(parents=True)

         ruta_archivo=Path(cadena+self.name)
         try:
             archivo=open(ruta_archivo,'w')
             archivo.write(self.body)
         
             archivo.close()
         except:
             print("no se pudo crear el archivo")


     elif self.type=="Bucket":
         print("Creando en Bucket")

#c=Create("hola.txt","mundo","Server","/hola/")