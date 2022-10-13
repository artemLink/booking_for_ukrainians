from django import forms
from django.forms import ModelForm
from .models import AddCard
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Ім'я користувача ", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль ", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Ім'я користувача ", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль ", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Підтвердження паролю ",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Пошта ", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(label="Номер телефону ", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta():
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')


class CardForm(ModelForm):
    class Meta():
        model = AddCard
        fields = ['title', 'description', 'content', 'photo', 'price', 'wifi', 'pool', 'parking', 'city', 'adress',
                  'single_rooms', 'double_rooms']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'description': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'content': forms.Textarea(attrs={'class': 'form-control form-control-sm'}),
            'price': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'adress': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'single_rooms': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'double_rooms': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }
