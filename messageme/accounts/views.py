from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *
from django.contrib import messages

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            return HttpResponse('Looks like you have registed it')
            # user = form.save()

            # user.refresh_from_db()
            # user.profile.First_name = form.cleaned_data.get('First_name')
            # user.profile.Last_name = form.cleaned_data.get('Last_name')
            # user.profile.Email = form.cleaned_data.get('Email')
            # user.save()

            # messages.success(
            #     request, f'Account created for {user.profile.First_Name}!')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {"form": form})
