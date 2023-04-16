from django.urls import path
from .views import MyView, RegisterUser, MyViewPage, LoginUser


urlpatterns = [
    path('',MyViewPage.as_view(), name='myprincipalindex'),
    path('Home/',MyView.as_view(), name='home'),
    path('Register/',RegisterUser.as_view(), name='register'),
    path('LogoutUser/',RegisterUser.logout_user, name='logout'),
    path('Login/',LoginUser.as_view(), name='login'),
]
