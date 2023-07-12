from django.urls import path
from .views import MyView, RegisterUser, MyViewPage, LoginUser
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',MyViewPage.as_view(), name='myprincipalindex'),
    path('Home/',MyView.as_view(), name='home'),
    path('Register/',RegisterUser.as_view(), name='register'),
    path('LogoutUser/',RegisterUser.logout_user, name='logout'),
    path('Login/',LoginUser.as_view(), name='login'),
    path('reset_password/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_send/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
