from django import forms
from django.contrib.auth.models import User
from .models import Contract, Customer, Contact

class ContractForm(forms.ModelForm):
    rut = forms.CharField(max_length=12)
    name = forms.CharField(max_length=100)
    departure_date = forms.DateField(widget=forms.SelectDateWidget())
    return_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Contract
        fields = ['rut', 'name', 'destination', 'departure_date', 'return_date']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['rut', 'name']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'country', 'city', 'message']