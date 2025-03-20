from django import forms

class QRCodeForm(forms.Form):

    restaurant_name = forms.CharField(label='Restaurant Name',
    max_length=100,
    widget=forms.TextInput(attrs={
        'class': 'form-control ',
        'placeholder': 'Enter Restaurant Name'
        }))
    url = forms.URLField(label='URL',
    max_length=100,
    widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your menu url'
        }))