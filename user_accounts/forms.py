from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from virtdibs.models import Customer

class UserSignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomerSignUpForm(forms.ModelForm):
    fullname = forms.CharField(max_length=254, widget=forms.TextInput())
    DOB = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Customer
        fields = ('fullname','DOB')
