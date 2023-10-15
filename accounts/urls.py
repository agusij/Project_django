from django.urls import path
from accounts.views import login, register, edit_profile, ChangePassword
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/edit/password', ChangePassword.as_view(), name='edit_pass'),


]
