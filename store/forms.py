from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput())
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AddNewProductForm(forms.ModelForm):
    # name = forms.CharField(label='Name', widget=forms.TextInput())
    # price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2, widget=forms.NumberInput())
    # digits = forms.BooleanField(label='Available', widget=forms.NullBooleanSelect())
    # category = forms.Select()
    # image = forms.FileField(label='Image', widget=forms.FileInput())

    class Meta:
        model = Product
        fields = ('name', 'price', 'digital', 'image')
    widgets = {
        'name': forms.TextInput(),
        'price': forms.NumberInput(),
        'image': forms.FileInput(),
        'digital': forms.NullBooleanSelect()
    }