from django import forms
from datetime import datetime


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField()
    price = forms.DecimalField(decimal_places=2, max_digits=10)
    quantity = forms.IntegerField()
    adding_date = forms.DateTimeField(initial=datetime.now())
    picture = forms.ImageField()
