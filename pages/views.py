from django.shortcuts import render



def home(request):
    return render(request, 'home.html')
def index_v(request):
    return render(request, 'index.html')
def about_v(request):
    return render(request, 'about.html')
def contact_v(request):
    return render(request, 'contact.html')
def quiz_v(request):
    return render(request, 'quiz.html')
def login_v(request):
    return render(request, 'login.html')



