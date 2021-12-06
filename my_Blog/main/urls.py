

from django.urls import path
from . import views



urlpatterns = [
    #path('admin/', admin.site.urls),
     path('',views.index),
    path('about',views.about),
    path('login',views.my_form, name='form'),
path('comanda',views.comanda,name='forms'),
#path(r'form', views.my_form, name='form')
]