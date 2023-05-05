from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "field"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "field"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "field"}))
    address = forms.CharField(max_length=250, widget=forms.TextInput(attrs={"class": "field"}))
    postal_code = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "field"}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code']
