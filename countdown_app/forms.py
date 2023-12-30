from django import forms
from .models import Timer

class TimerForm(forms.ModelForm):
    class Meta:
        model = Timer
        fields = ['title', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }
