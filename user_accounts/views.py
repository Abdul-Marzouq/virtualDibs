from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import CustomerSignUpForm, UserSignUpForm,AddressForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def password_reset_email(request):
    return render(request,'registration/password_reset_form.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")@login_required

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserSignUpForm(data=request.POST)
        customer_form = CustomerSignUpForm(data=request.POST)
        if user_form.is_valid(): #and customer_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user=User.objects.create_user(username=username, password=password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            registered = True
        else:
            print(user_form.errors,customer_form.errors,)
    else:
        user_form = UserSignUpForm()
        customer_form = CustomerSignUpForm()
    return render(request,'virtdibs/register.html',
                          {'user_form':user_form,
                          'customer_form':customer_form,
                           'registered':registered})

def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print(user)
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'virtdibs/login.html', {})
