import os
import re
from pathlib import Path
class Modify:
 def __init__(self,body,type,path):
     self.body=body
     self.type=type
     self.path=path
     self.modificar()
 def modificar(self):
     if self.type=="Server":
         root=str(Path.home()/'Archivos')+self.path
         path_correcto=os.path.exists(root)
         if(path_correcto):
             if re.search(r"\.txt$",root, re.I):
                  with open(root, 'w') as archivo:
                     archivo.write(self.body)
             archivo.close()
         else:
              print("Error en el path")
     elif self.type=="Bucket":
         print("Modificando en Bucket")