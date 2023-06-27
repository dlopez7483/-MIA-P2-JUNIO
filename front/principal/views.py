from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import PrincipalForm

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

         if user == 'jorge' and password == '123':
             print(user, password)
             return redirect('venpri')

         else:
                 
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


    return render(request, 'ventana_principal.html', {'form':form})

def ventana(request):

    return render(request,'ventana_principal.html')
