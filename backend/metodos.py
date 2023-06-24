import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import boto3
from botocore.client import Config
lista_usuarios = list()









s3=boto3.resource('s3',aws_access_key_id='AKIAVUJFRDVN5ZXYPPVS',
                   aws_secret_access_key='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',
                   config=Config(signature_version='s3v4'))

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
 archivo = s3.list_objects(Bucket='bucket201907483', Prefix='Archivos/usuarios.txt')
    
 for linea in archivo['Body'].iter_lines():
     linea = linea.decode('utf-8')
     lista_usuarios.append(linea.replace("\n", ""))

 archivo.close()
#--------------------------------------------------------------------




#----------------------------------cargar archivo con instrucciones
def cargar_archivo(ruta):
 try: 
     archivo = open(ruta, "r")
     for linea in archivo:
         print(linea)

     archivo.close()
     return True
 except:
     return False

#------------------------------------------------------------