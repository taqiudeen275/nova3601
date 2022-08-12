from django.urls import path
from .views import *



app_name = 'account'
urlpatterns = [
    path('', loginView, name='login'),
    path('signup/', signupView , name='register'),
    path('logout/', logoutView, name='logout'),
    path('profile/', profile, name='profile'),
    
]
