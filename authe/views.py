from django.shortcuts import render, redirect
from authe.forms import register_form
from authe.models import register_model
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import random
import time
from django.contrib import messages

# Create your views here.


def register_view(request):
    form = register_form()
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = register_form(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            send_mail(subject="welcome to myproject",
                      message=f"Hello {form.cleaned_data['first_name']}", from_email=settings.EMAIL_HOST_USER, recipient_list=[form.cleaned_data['email'],])
            messages.success("Registration process is success")
            return redirect('/authe/login')
    return render(request=request, template_name="register.html", context={'form': form})


user_id = None
otp_confirm = None


def login_view(request):
    global user_id, otp_confirm
    form = AuthenticationForm()
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            if user:
                data = random.randrange(100000, 900000)
                send_mail(subject="welcome to myproject",
                          message=f"""haii otp sent to {user.email}
                        current otp: {data}
                        thank you""", from_email=settings.EMAIL_HOST_USER, recipient_list=[user.email])
                user_id = user
                otp_confirm = data
                messages.success(request, "otp sent")
                return redirect('/authe/otp')
            else:
                messages.error(request, "Invalid login")
    return render(request=request, template_name="login.html", context={'form': form})


def otp_view(request):
    if request.method == 'POST':
        if str(request.POST['otp']) == str(otp_confirm):
            login(request, user_id)
            messages.success(request, "Login success")
            return redirect('/authe/home')
        else:
            messages.warning(request, "otp incorrect")
            return redirect('/authe/otp')
    return render(request=request, template_name='otp.html')


@login_required(login_url='/authe/login')
def home_view(request):
    res = register_model.objects.get(id=request.user.id)
    return render(request=request, template_name="home.html", context={'res': res})


@login_required(login_url='/authe/login')
def logout_view(request):
    logout(request)
    return redirect('/authe/login')
