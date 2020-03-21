from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Sex = ((0,'Male'),(1,'Female'),(2,'Lets Keep it secret'))


class SignupForm(UserCreationForm):

    First_name = forms.CharField(max_length=50, required=True)
    Last_name = forms.CharField(max_length=50, required=True)
    Email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'First_name', 'Last_name',
                  'Email', 'password1', 'password2'
                  ]
