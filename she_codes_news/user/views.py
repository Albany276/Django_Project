from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.contrib.auth.decorators import login_required

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/createAccount.html'

@login_required
#This is a decorator that add functionality to our def, therefore the user needs to be logged in to access this view
def profile(request):

    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, request.FILES,  instance=request.user) #passing the instance so the details of the user are prepopulated

        if u_form.is_valid():
            u_form.save()
            #messages.sucess(request, f'Your account has been updated!')
            #return redirect('profile')

    else:
        u_form = CustomUserChangeForm(instance=request.user) #passing the instance so the details of the user are prepopulated
   
    context = {
        'u_form': u_form
    }
    return render(request, 'user/profile.html', context)
    
# class UserDetailView(generic.DetailView):
#     model = CustomUser
#     template_name = 'user/sort.html'
#     context_object_name = 'sort'


# Create your views here.
