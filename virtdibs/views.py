from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'virtdibs/base.html')

def index(request):
    return render(request,'virtdibs/index.html')
