from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Login(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('')
    template_name = 'login.html'

def index(request):
    return HttpResponse("Hello there, I got something !!")


def home_view(request):
    dist_var = {'any_key': "hello, this is a value for the key from view.py that can be used in index.html"}
    return render(request, 'home.html', context=dist_var)

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')