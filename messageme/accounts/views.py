from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {"form": form})


def login_view(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('user')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def userprofile(request):
    myuser = profile.objects.all()
    return render(request, 'username.html', {'user': myuser})
