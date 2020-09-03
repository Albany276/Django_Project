from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/createAccount.html'

@login_required
#This is a decorator that add functionality to our def, therefore the user needs to be logged in to access this view
def profile(request):
    return render(request, 'user/profile.html')
# class UserDetailView(generic.DetailView):
#     model = CustomUser
#     template_name = 'user/sort.html'
#     context_object_name = 'sort'


# Create your views here.
