from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .forms import PrincipalForm
import requests

# Create your views here.

def home(request):
    
    return render(request,'home.html')

def otra_pagina_view(request):
    return render(request,'login.html',{
            'form': AuthenticationForm
        })

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
         #'http://52.15.136.186:5000'

        
         resp = respuesta.json()
         mensaje = resp['bandera_log']
         
         if mensaje == True:
             print(user, password)
             return render(request, 'ventana_principal.html')

         elif mensaje == False:
                 
            return render(request,'login.html',{
                'form': AuthenticationForm,
                'error': 'Usuario y/o Contraseña incorrectos'
            })
         
         


""" def subirarchiv(request):
    form = PrincipalForm()
        
    if request.method == 'POST':
        if request.POST['consola_entrada'] != '' and request.POST['archivo'] == '':
            print(request.POST['consola_entrada'])

        elif request.POST['archivo'] != '':
            print(request.POST['archivo'])
            archivo = request.FILES['archivo']
            contenido = archivo.read().decode('utf-8')
            return render(request, 'ventana_principal.html', {'consola_entrada': contenido})


    return render(request, 'ventana_principal.html', {'form':form}) """

def abrir_archivo(request):
    if request.method == 'POST':
        archivo = request.FILES['archivo']
        contenido = archivo.read().decode('utf-8')
        return render(request, 'ventana_principal.html', {'contenido': contenido})
    else:
        return render(request, 'ventana_principal.html')    
    
def ejecutar(request):
    if request.method == 'POST':
        texto = request.POST.get('contenido_entrada', '')
        print("ejecutando")
        #print(texto)
        url_flask = 'http://localhost:5000/carga_archivo'
        #'http://localhost:5000/carga_archivo'
        response = requests.post(url_flask, data={'contenido': texto})    
        return redirect('venpri')
    
       
    
    return render(request, 'ventana_principal.html')
    

def guardar_datos(request):
    if request.method == 'POST':
        datos = request.POST.get('datos', '')
        # Guardar los datos en el contexto
        context = {'datos_guardados': datos}
        return render(request, 'formulario.html', context)
    return render(request, 'formulario.html')

