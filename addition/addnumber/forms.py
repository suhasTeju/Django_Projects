from django import forms
from .models import Number


class NumberForm(forms.ModelForm):
    class Meta:
        model=Number
        fields=['number1','number2']
