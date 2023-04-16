from django.shortcuts import render, redirect, get_object_or_404
from .form import MyAlbumForm, MyPhotoForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.views.generic import View
from django.contrib.auth.models import User
from .models import Album, MyPhoto
from django.urls import reverse_lazy


# Create your views here.
@method_decorator(login_required, name='dispatch')
class CreateAlbum(View):
    def get(self, request):
        form = MyAlbumForm
        if request.method == "GET":
            return render(request, 'albumphoto/createalbum.html', {"form":form})
    def post(self, request):
        form = MyAlbumForm(request.POST)
        if form.is_valid():
            new_album = form.save(commit=False)
            new_album.name_user_album = request.user
            new_album.save()
           
            return redirect('displayalbum')

@method_decorator(login_required, name='dispatch')
class UpLoadPhoto(View):

    def get(self, request):
        user_instance = request.user
        if request.method == "GET":
            return render(request, 'albumphoto/uploadphoto.html', {"form":MyPhotoForm(user=user_instance)})
        
    def post(self, request):
        user_instance = request.user
        #albums = Album.objects.filter(user=user_instance)
        form = MyPhotoForm(request.POST, request.FILES, user=user_instance)
        if form.is_valid():
            form.save()

            return redirect('displayalbum')


def display_album(request):

    user_instance = request.user
    albums = Album.objects.filter(name_user_album_id=user_instance)
    return render(request, 'albumphoto/displayalbum.html', {"albums":albums, "user_instance":user_instance})


def display_photos(request, id):
    album = get_object_or_404(Album, id=id)

    photos = MyPhoto.objects.filter(album=album)
    return render(request, 'albumphoto/displayphoto.html', {"album":album, "photos":photos})


class DeletePhoto(DeleteView):
    model = MyPhoto
    success_url = reverse_lazy('displayalbum')

