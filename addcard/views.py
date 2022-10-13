from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CardForm
from django.contrib import messages


def addcard(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            # img_obj = form.instance
            form = CardForm()
            return redirect('index')
            # return render(request, './addcard/addcard.html', {'img_obj': img_obj})
        else:
            print(form.errors)
            return redirect('index')


    else:
        print('lol')
        form = CardForm()

        return render(request, './addcard/addcard.html', {'form': form})
