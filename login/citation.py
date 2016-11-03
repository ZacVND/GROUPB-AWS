#files.py
import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class CitationForm(forms.Form):

    title = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("title") )
    # link = forms.EmaField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    # notes = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))

    link = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),label=_("link"))
    notes = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),label=_("notes"))
           # title = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })


    def clean(self):
        return self.cleaned_data