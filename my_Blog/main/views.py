from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.template import loader
from .models import Book
from django.shortcuts import render
from .models import User
from .models import Comentariu
from .forms import ComentariuForm
from .forms import MyForm

# Create your views here.

def index(request):
    book=Book.objects.all()
    # template = loader.get_template('index.html', {'title': 'Basik page' , 'price': book})  # getting our template
    # return HttpResponse(template.render())  # rendering the template in HttpResponse
    return render(request,'index.html', {'title': 'Basik page' , 'books': book})
def about(request):
    return render(request,'About.html')
def login(request):
    return render(request,'Login.html')

def comanda(request):
        form_class = ComentariuForm
        # if request is not post, initialize an empty form
        form = form_class(request.POST or None)
        if request.method == 'POST':

            if form.is_valid():
                current_user = form.save(commit=False)
                current_user.comentariu = form.cleaned_data['comentariu']
                current_user.save()
        return render(request, 'comanda.html', {'form': form})

def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      current_user = form.save(commit=False)
      current_user.first_name = form.cleaned_data['first_name']
      current_user.last_name = form.cleaned_data['last_name']

      current_user.save()
  else:
      form = MyForm()
  return render(request, 'cv-form.html', {'form': form})