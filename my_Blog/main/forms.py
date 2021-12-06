from.models import Book
from .models import User

from .models import Comentariu
from django.forms import ModelForm
from django import forms
class ComentariuForm(forms.ModelForm):
  class Meta:
    model = Comentariu
    fields = ["comentariu"]
    labels = {'comentariu': "Comentariu"}

class MyForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ["first_name", "last_name"]
    labels = {'first_name': "Name", "last_name": "Last Name"}