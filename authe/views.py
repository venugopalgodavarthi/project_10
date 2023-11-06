from django.shortcuts import render, redirect
from authe.forms import register_form
from authe.models import register_model
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register_view(request):
    form = register_form()
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = register_form(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('/login')
    return render(request=request, template_name="register.html", context={'form': form})


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            print(user, user.email)
            login(request, user)
            return redirect('/authe/home')
    return render(request=request, template_name="login.html", context={'form': form})


def home_view(request):
    print(request.user.id)
    res = register_model.objects.get(id=request.user.id)
    return render(request=request, template_name="home.html", context={'res': res})


def logout_view(request):
    logout(request)
    return redirect('/authe/login')
