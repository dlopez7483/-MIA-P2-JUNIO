import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import boto3
from botocore.client import Config
from analizador import analisis
from bitacora import lista_datos
from flask import jsonify
lista_usuarios = list()



s3_client = boto3.client(
     's3',
     aws_access_key_id='AKIAVUJFRDVNRXAMFOH6',
     aws_secret_access_key='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',
     config=Config(signature_version='s3v4')
     )





#------------------------------------validar_usuario------------------------------------

def desencriptar_contra(linea,llave):
 b64 = base64.b64encode(bytes.fromhex(linea)).decode()
 linea2 = base64.b64decode(b64)
        
 cipher = AES.new(llave.encode('utf-8'), AES.MODE_ECB)
 return unpad(cipher.decrypt(linea2),16)


def validar(x,y):
 leerarchivo()
 if x in lista_usuarios:
     print("Usuario Correcto")
     valor = lista_usuarios.index(x)
     contra = lista_usuarios[valor+1]
     contra_desenc = desencriptar_contra(contra,'miaproyecto12345')
     contra_desenc = contra_desenc.decode("utf-8", "ignore")

     if y == contra_desenc:
         print(y+" = "+contra_desenc)
         print("Contraseña Correcta")
         return True
          
            
     else:
         return False





def leerarchivo():
 archivo = s3_client.get_object(Bucket='bucket201907483', Key='miausuarios.txt')
    
 for linea in archivo['Body'].iter_lines():
     linea = linea.decode('utf-8')
     lista_usuarios.append(linea.replace("\n", ""))


#--------------------------------------------------------------------




#----------------------------------cargar archivo con instrucciones
def cargar_archivo(ruta):
 
 try: 
     #archivo = open(ruta, "r")
     archivo = ruta.split('\n')
     
     for linea in archivo:
         print("comando: ",linea)
         #a=analisis(linea.replace("\n", ""))
         a=analisis(linea)
         #a.iniciar_comandos()
        
         lista_datos.append(a.iniciar_comandos())
         #bb.lista_datos.append(jsonify({'message':a.iniciar_comandos()}))
     #archivo.close()
     return True
 except:
     return False

#------------------------------------------------------------