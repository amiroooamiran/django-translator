from django import forms
from .widgets import TranslationEditor

class TranslationForm(forms.Form):
    content = forms.CharField(widget=TranslationEditor())