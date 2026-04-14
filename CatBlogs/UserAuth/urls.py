from django.urls import path
from .views import registerUser, loginUser, additional, profile

urlpatterns = [
    path('login', loginUser, name='loginUser'),
    path('register', registerUser, name='registerUser'),
    path('finishing_up  ', additional, name='additionalInfo'),
    path('profile', profile, name='profile'),
]
