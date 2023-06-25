from pathlib import Path
import shutil
class delete:
 def __init__(self,path,name,type):
     self.path=path
     self.name=name
     self.type=type
     self.eliminar()
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
         print("Eliminando en Bucket")  


#d=delete("/hola/","","Server")