from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'virtdibs/home.html')

def signupin(request):
    return render(request,'virtdibs/login_signup.html')
