from django import forms
from django.forms import ModelForm
from .models import Album, MyPhoto

class MyAlbumForm(ModelForm):
    name_album = forms.CharField(label="Nombre album",widget=forms.TextInput(attrs={'class':'form-control m-3', 'placeholder':'Nombre del álbum'}))
    description = forms.CharField(label="Descripcion",widget=forms.TextInput(attrs={'class':'form-control m-3', 'placeholder':'Descripción del álbum'}))
    
    class Meta:
        model = Album
        fields = ('name_album', 'description')


class MyPhotoForm(ModelForm):
    album = forms.ModelChoiceField(label="Seleccionar album",widget=forms.Select(attrs={'class': 'form-control m-3'}),queryset=None)
    photo = forms.ImageField(label="Seleccionar archivo de imagen",widget=forms.ClearableFileInput(attrs={'class': 'form-control m-3', 'multiple': True}))
    
    class Meta:
        model = MyPhoto
        fields = ('album', 'photo')


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['album'].queryset = Album.objects.filter(name_user_album_id=user)