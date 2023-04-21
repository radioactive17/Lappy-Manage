from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import LaptopO, LaptopD
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']


class LaptopDForm(ModelForm):
    class Meta:
        model = LaptopD
        exclude = ('laptop', )

class AddLaptopO(ModelForm):
    class Meta:
        model = LaptopO
        fields = '__all__'

class AddLaptopD(ModelForm):
    class Meta:
        model = LaptopD
        fields = '__all__'