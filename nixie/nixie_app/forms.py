from django import forms
from .models import Review


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "smallfield"}))
    email_address = forms.EmailField(max_length=150, widget=forms.TextInput(attrs={"class": "smallfield"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "bigfield"}),
                              max_length=2000)


class ReviewForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "smallfield"}))
    surname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "smallfield"}))
    review_text = forms.CharField(widget=forms.Textarea(attrs={"class": "bigfield"}),
                                  max_length=2000)

    class Meta:
        model = Review
        fields = ['name', 'surname', 'review_text']
