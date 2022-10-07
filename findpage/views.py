from django.shortcuts import render
from django.http import HttpResponse
from addcard import models
from .forms import filter_sidebar


def find_page(request):
    content = models.AddCard.objects.all()

    if request.method == 'POST':
        form = filter_sidebar(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['price'] == '':
                data.pop('price')
            elif data['price'] <= '6000':
                value = int(data['price'])
                data.pop('price')
                data['price__lt'] = value
            elif data['price'] > '6000':
                value = int(data['price'])
                data.pop('price')
                data['price__gt'] = value
            content = models.AddCard.objects.filter(**data)

            print(type(data['price__lt']))
    else:
        form = filter_sidebar

    context = {
        'content': content,
        'form': form,
    }
    return render(request, './find_page.html', context=context)
