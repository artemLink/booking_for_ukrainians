from django import forms


class filter_sidebar(forms.Form):
    book_of_choices = [(2000,'Бюджет до 2000 грн'),
                       (4000, 'Бюджет до 4000 грн'),
                       (6000,'Бюджет до 6000 грн'),
                       (6001, 'Бюджет більше 6000 грн')]
    price = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-label'}), choices=book_of_choices, required=False, label='Оберіть '
                                                                                                       'бюджет за '
                                                                                                       'одну ніч')
    wifi = forms.BooleanField(label='wifi', required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-label'}))
    pool = forms.BooleanField(label='Басейн', required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-label'}))
    parking = forms.BooleanField(label='Парковка', required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-label'}))
