from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import Creetulisateur


# Create your views here.
def index(request):
   form=Creetulisateur()               
   if request.method == 'POST':
        form=Creetulisateur(request.POST)
        if form.is_valid():
             form.save()
             return redirect('acces')
   contexet={'form':form}
   return render(request,'compt/inscription.html',contexet)

def acces(request):
    return render(request,'compt/login.html')