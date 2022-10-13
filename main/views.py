from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from addcard.forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from addcard.models import AddCard
from django.contrib.auth import login, logout
from .forms import index_form


def index(request):
    print(request.user.id)
    form = index_form
    context = {
        'form':form
    }
    return render(request, './main/index.html', context= context)


def about(request):
    return render(request, './main/sample.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вітаємо з реєстрацією!')
            return redirect('user_login')
        else:
            messages.error(request, 'Помилка реєстрації')
    else:
        form = UserRegisterForm()
    return render(request, './main/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, './main/user_login.html', {'form': form})


def user_logout(request):
    logout(request)

    return redirect('user_login')


def view_card(request, card_id):
    card_item = AddCard.objects.get(pk=card_id)
    content = {
        'item': card_item
    }
    try:
        content['date_from'] = request.POST.__getitem__('date_from')
        content['date_to'] = request.POST.__getitem__('date_to')
    except:
        pass

    return render(request, './main/card_page.html', context=content)
