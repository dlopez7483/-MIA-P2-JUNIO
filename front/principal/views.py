from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .forms import PrincipalForm
import requests

# Create your views here.

def home(request):
    return render(request,'home.html')



def login(request):

    if request.method == 'GET':
        return render(request,'login.html',{
            'form': AuthenticationForm
        })
    else:
         print(request.POST)
         user = request.POST['username']
         password = request.POST['password']

         datos = {
            'usurio': user,
            'contrasenia': password,}
         respuesta = requests.post('http://localhost:5000/login', json=datos)
         if respuesta == True:
             print(user, password)
             return redirect('venpri')

         elif respuesta == False:
                 
            return render(request,'login.html',{
                'form': AuthenticationForm,
                'error': 'Usuario y/o Contraseña incorrectos'
            })
         
         


def subirarchiv(request):
    form = PrincipalForm()
        
    if request.method == 'POST':
        if request.POST['consola_entrada'] != '' and request.POST['archivo'] == '':
            print(request.POST['consola_entrada'])

        elif request.POST['archivo'] != '':
            print(request.POST['archivo'])
            archivo = request.FILES['archivo']
            contenido = archivo.read().decode('utf-8')
            return render(request, 'ventana_principal.html', {'consola_entrada': contenido})


    return render(request, 'ventana_principal.html', {'form':form})

def abrir_archivo(request):
    if request.method == 'POST':
        archivo = request.FILES['archivo']
        contenido = archivo.read().decode('utf-8')
        return render(request, 'ventana_principal.html', {'contenido': contenido})
    else:
        return render(request, 'ventana_principal.html')    
    
def ejecutar(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido', '')
        print("ejecutando")
        return render(request, 'ventana_principal.html', {'contenido': contenido})      
    else:
       
        return render(request, 'ventana_principal.html')
    



