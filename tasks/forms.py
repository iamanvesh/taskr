from django import forms


class EntryForm(forms.Form):
    url = forms.URLField()
    email = forms.EmailField()

    keywords = forms.CharField(max_length=200)
