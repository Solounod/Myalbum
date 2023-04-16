from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Album(models.Model):
    name_album = models.CharField(max_length=128)
    name_user_album = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    datetime_creation = models.DateTimeField(auto_now_add=False, auto_now=True)
    update_datetime = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return f"{self.name_album} - {self.description} - {self.name_user_album}"

class MyPhoto(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="album")
    created_photo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.album} {self.created_photo}"


