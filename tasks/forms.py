from django import forms


class EntryForm(forms.Form):
    url = forms.URLField()
    email = forms.EmailField()
    end_date = forms.DateField()

    keywords = forms.CharField(max_length=200)
