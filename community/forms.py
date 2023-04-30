from django import forms
from .models import *
 


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['user', 'content']

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }