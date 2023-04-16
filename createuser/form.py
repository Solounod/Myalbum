from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class UserCreationFormStyle(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario",widget=forms.TextInput(attrs={'class':'form-control m-3', 'placeholder':'Nombre usuario'}))
    password1 = forms.CharField(label="Contraceña",widget=forms.PasswordInput(attrs={'class':'form-control m-3', 'placeholder':'Contraceña'}))
    password2 = forms.CharField(label="Repetir contraceña",widget=forms.PasswordInput(attrs={'class':'form-control m-3', 'placeholder':'Repetir contraceña'}))


class AuthenticationFormStyle(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario",widget=forms.TextInput(attrs={'class':'form-control m-3', 'placeholder':'Nombre usuario'}))
    password = forms.CharField(label="Contraceña",widget=forms.PasswordInput(attrs={'class':'form-control m-3', 'placeholder':'Contraceña'}))