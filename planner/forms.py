from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'email', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

        