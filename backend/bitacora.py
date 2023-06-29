from datetime import date, datetime
from pathlib import Path
import time
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad




class bitacora:
 def __init__(self):
     self.fecha=date.today()
     self.crear_bitacora()
     


 def crear_bitacora(self):
     ruta="./documento/logs/"
     
     
    
     ruta_acciones=ruta+"log_archivos.txt"
     try:
         archivo=open(ruta_acciones,'w')
         archivo.close()
     except:
         print("no se pudo crear la bitacora")


 def insertar_log(self,accion):
    
     ruta="./documento/logs/log_archivos.txt"
     

     try:
              
             archivo=open(ruta,'a')
             archivo.write(accion+"\n")
             archivo.close()
     except:
         print("no se pudo agregar el proceso a la bitacora")


bit = bitacora()







