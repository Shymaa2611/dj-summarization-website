from django import forms
from .models import summarize_data

class textForm(forms.ModelForm):
    text=forms.Textarea()
    class Meta:
        model=summarize_data
        fields=('text',)
    

