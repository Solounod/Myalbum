from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class UserCreationFormStyle(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario",widget=forms.TextInput(attrs={'class':'form-control m-3', 'placeholder':'Nombre usuario'}))
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres, debe ser un email valido.", widget=forms.TextInput(attrs={'class':'form-control m-3'}))
    password1 = forms.CharField(label="Contraceña",widget=forms.PasswordInput(attrs={'class':'form-control m-3', 'placeholder':'Contraceña'}))
    password2 = forms.CharField(label="Repetir contraceña",widget=forms.PasswordInput(attrs={'class':'form-control m-3', 'placeholder':'Repetir contraceña'}))

    

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'El correo electronico ya esta registrado, por favor prueba otro.')
        return email


class AuthenticationFormStyle(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario",widget=forms.TextInput(attrs={'class':'form-control m-3', 'placeholder':'Nombre usuario'}))
    password = forms.CharField(label="Contraceña",widget=forms.PasswordInput(attrs={'class':'form-control m-3', 'placeholder':'Contraceña'}))