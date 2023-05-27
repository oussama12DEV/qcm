from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import Creetulisateur
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def index(request):
   form=Creetulisateur()               
   if request.method=='POST':
        form=Creetulisateur(request.POST)
        if form.is_valid():
             form.save()
             user=form.cleaned_data.get('username')
             messages.success(request,'le compt et creer avec succes pour ' +user)
            #  return redirect('acces')
   contexet={'form':form}
   return render(request,'compt/inscription.html',contexet)

def acces(request):
    if request.method=='POST':
        usr=request.POST.get('username')
        pas=request.POST.get('password')
        user=authenticate(request,username=usr,password=pas)
        if user is not None:
          login(request,user)
          return redirect('inscription')
        else:
            messages.info(request,"il y a une erreur dans le nom d'utilisateur et mode passe")
    return render(request,'compt/login.html')