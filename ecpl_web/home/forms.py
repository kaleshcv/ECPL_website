from django import forms
from . import models


class QuickContact(forms.ModelForm):
    class Meta:
        model=models.QuickContact
        fields=['name','email','phone','message']

