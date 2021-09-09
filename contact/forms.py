from django import forms
from django.db import models
from django.forms import fields, widgets
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("email", )
        widgets = {
            "email": forms.TextInput(attrs={"class": "editContent", "placeholder": "Your Email:"})
        }

        labels= {
            "email": ''
        }