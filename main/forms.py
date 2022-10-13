from django import forms


class index_form(forms.Form):
    city = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-check-label'}))
    date_from = forms.CharField(widget=forms.DateInput(attrs={'class':'form-check-label',
                                                              'type': 'date'}), )
    date_to = forms.CharField(widget=forms.DateInput(attrs={'class':'form-check-label',
                                                              'type': 'date'}))
