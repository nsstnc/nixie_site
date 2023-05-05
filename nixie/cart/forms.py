from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(required=1, initial=1, widget=forms.HiddenInput)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
