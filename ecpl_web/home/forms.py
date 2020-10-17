from django import forms
from . import models


class QuickContact(forms.ModelForm):
    class Meta:
        model=models.QuickContact
        fields=['name','email','phone','message']

class Contactform(forms.ModelForm):
    class Meta:
        model=models.Contactform
        fields=['name','email','message','is_inbound','is_outbound']
