from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Sex = ((0,'Male'),(1,'Female'),(2,'Lets Keep it secret'))


class SignupForm(UserCreationForm):
    Email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', "Email", 'password1', 'password2'
                  ]
