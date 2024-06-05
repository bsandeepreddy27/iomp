# myapp/forms.py

from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['name', 'category', 'judge', 'estimated_time_to_close']
