from django.shortcuts import render
from django.http import HttpResponse
from addcard import models
from .forms import filter_sidebar
from main.forms import index_form


def find_page(request):

    if request.method == 'POST':
        form = filter_sidebar(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            main_form = index_form(request.POST)
            if main_form.is_valid():
                main_data = main_form.cleaned_data
                print(main_form.cleaned_data)
                date_from = main_data['date_from']
                date_to = main_data['date_to']
                if main_data['city'] != '':
                    data['city'] = main_data['city']
            print(data)
            data['is_publish'] = True
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

            for dat in list(data):
                if not data[dat]:
                    data.pop(dat)

            content = models.AddCard.objects.filter(**data)


    else:
        form = filter_sidebar

        content = models.AddCard.objects.filter(**{'is_publish': True})
    context = {
        'content': content,
        'form': form,

    }
    try:
        content['date_from'] = date_from
        content['date_to'] = date_to
    except:
        pass
    return render(request, './find_page.html', context=context)
