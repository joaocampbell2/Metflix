from django.shortcuts import render

# Create your views here.

def index(request):
    if str(request.user) == 'AnonymousUser':
        return render(request,'welcome.html')
    else:
        return render(request,'homepage.html')

def homepage(request):
    return render(request,'homepage.html')

def login(request):
    return render(request,'login.html')