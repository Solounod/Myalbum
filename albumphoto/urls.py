from django.urls import path
from .views import CreateAlbum, UpLoadPhoto, DeletePhoto ,display_album, display_photos



urlpatterns = [
    path('Form_album/',CreateAlbum.as_view(), name='formalbum'),
    path('Form_photo/',UpLoadPhoto.as_view(), name='formphoto'),
    path('Home/albums/',display_album, name='displayalbum'),
    path('Home/photo/<int:id>',display_photos, name='displayphoto'),
    path('delete/<int:pk>',DeletePhoto.as_view(), name='delete_photo'),
    
    
]
