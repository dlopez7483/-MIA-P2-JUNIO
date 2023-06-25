import os
import re
from pathlib import Path
class renombrar:
 def __init__(self, path, name, type):
     self.name = name
     self.type = type
     self.path = path
     self.renombrar()


 def renombrar(self):
     if self.type=="Server":
         ruta=str(Path.home()/'Archivos')+self.path
         existencia_path = os.path.exists(ruta)
         if(existencia_path):
             if re.search(r"\.txt$",ruta, re.I):
                 try:
                     nombre_directorio, nombre_archivo = os.path.split(ruta)

                     nombre_base, extension = os.path.splitext(nombre_archivo)

                     nuevo_nombre_archivo = self.name
    
                     nueva_ruta = os.path.join(nombre_directorio, nuevo_nombre_archivo)
                
                     os.rename(ruta, nueva_ruta)
                 except:
                     print("Error")  
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
                      print("Error carpeta ya existe")
     elif self.type=="Bucket":
         print("Renombrando en Bucket")