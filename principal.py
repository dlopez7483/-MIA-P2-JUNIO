import tkinter
from tkinter import messagebox
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad




lista_usuarios = list()
class Usuarios:
    def __init__(self, usuario, contrasenia):
        self.usuario = usuario
        self.contrasenia = contrasenia

global login
login = tkinter.Tk()
login.geometry("250x250")
login.state(newstate="normal")
login.resizable(0,0)
login.title("Login")
login.eval('tk::PlaceWindow . center')

label_p1 = tkinter.Label(login,text = " ",font= "Helvetica 15")
label_p1.grid(row=0,column=0)

label_user = tkinter.Label(login,text = "Usuario: ",font= "Helvetica 15")
label_user.grid(row=1,column=1)

label_p2 = tkinter.Label(login,text = " ",font="helvetica 10")
label_p2.grid(row=2,column=0)

texto_user = tkinter.Entry(login, font= "Helvetica 15")
texto_user.grid(row=2,column=1)

label_password = tkinter.Label(login,text = "Contraseña: ",font= "Helvetica 15")
label_password.grid(row=3,column=1)

texto_password = tkinter.Entry(login, font= "Helvetica 15",show="*")
texto_password.grid(row=4,column=1)

label_p = tkinter.Label(login,text = " ",font= "Helvetica 15")
label_p.grid(row=5,column=0)



#funcin para desencriptar la contraseña de usuario

def desencriptar_contra(linea,llave):
        b64 = base64.b64encode(bytes.fromhex(linea)).decode()
        linea2 = base64.b64decode(b64)
        
        cipher = AES.new(llave.encode('utf-8'), AES.MODE_ECB)
        return unpad(cipher.decrypt(linea2),16)

    
#Funcion login para guardar usuario y contra

def fun_login():
    print("Boton login")
    leerarchivo()
    textuser = texto_user.get()
    textcontra = texto_password.get()
    print('User: ' + textuser)
    print('Contra: ' + textcontra)
    
   
    validar(textuser,textcontra)

    #Funcion para validar usuario y contraseña correcta

def validar(x,y):
    
    if x in lista_usuarios:
        print("Usuario Correcto")
        valor = lista_usuarios.index(x)
        contra = lista_usuarios[valor+1]
        contra_desenc = desencriptar_contra(contra,'miaproyecto12345')
        contra_desenc = contra_desenc.decode("utf-8", "ignore")

        if y == contra_desenc:
            print(y+" = "+contra_desenc)
            print("Contraseña Correcta")
           
            abrirventana()
            
        else:
            messagebox.showwarning("Credenciales Invalidas", "Contraseña incorrecta")
            
       
       
        
    else:
        messagebox.showwarning("Credenciales Invalidas", "Usuario incorrecto")
        messagebox.askquestion()
       
    

def abrirventana():
    login.state(newstate="withdraw")
    #vp.principal()




def leerarchivo():
    archivo = open("Archivos/usuarios.txt")
    
    for linea in archivo:
        lista_usuarios.append(linea.replace("\n", ""))

    archivo.close()  
    

def cerrarsesion(ventana):
    login.state(newstate="normal")
    ventana.destroy()
    

boton_login = tkinter.Button(login, text="SIGN IN", bg="BLUE", command = fun_login ,width=10, height=3,foreground="white")
boton_login.grid(row=6,column=1)
login.mainloop()

