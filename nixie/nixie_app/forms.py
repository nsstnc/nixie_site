from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "smallfield"}))
    email_address = forms.EmailField(max_length=150, widget=forms.TextInput(attrs={"class": "smallfield"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "bigfield"}),
                              max_length=2000)



