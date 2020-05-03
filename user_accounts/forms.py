from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

class UserSignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomerSignUpForm(forms.ModelForm):
    fullname = forms.CharField(max_length=254, widget=forms.TextInput(),label="Full Name")
    DOB = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Date of Birth")
    class Meta:
        model = Customer
        fields = ('fullname','DOB')

class AddressForm(forms.ModelForm):
    address = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows': 4, 'cols': 60}))
    city = forms.CharField(max_length=40)
    state = forms.CharField(max_length=25)
    country = forms.CharField(max_length=30)
    zipcode = forms.CharField(max_length=6)

    def clean_zipcode(self):
        zipcode = self.cleaned_data['zipcode']
        if not zipcode.isdigit():
            raise forms.ValidationError('Zipcode can only contain digits.')
        elif len(zipcode) != 6:
            raise forms.ValidationError('Length of zipcode must be 6 digits')
        return zipcode

        class Meta:
            model = Address
            fields = __all__
