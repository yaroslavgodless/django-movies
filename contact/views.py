from django import forms
from django.db import models
from .models import Contact
from .forms import ContactForm
from .models import Contact
from django.views.generic import CreateView

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"