from django.urls import path
from .views import CreateAccountView
from .views import profile

app_name = 'user'

urlpatterns = [
    path(
        'create-account', 
        CreateAccountView.as_view(),
        name='createAccount'
    ),

    path('profile', profile, name='profile')
    #when we create profile in views.py, we did not create it as a 'view'
]