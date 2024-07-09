from django import forms
from .models import AthleteData
from django.contrib.auth.models import User
import fontawesome as fa


class AthleteForm(forms.ModelForm):
    class Meta:
        model = AthleteData
        fields = ['name', 'gender', 'age', 'height', 'weight', 'duration','heart_rate', 'body_temp']
        
        


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')