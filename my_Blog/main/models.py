from django.db import models
class Book(models.Model):
     title=models.CharField("Denumire",max_length=50)
     autor=models.CharField("Autor",max_length=20)
     description=models.TextField("Descriere")
     price=models.IntegerField("Pret")

     def __str__(self):
          return self.title

class User(models.Model):
     first_name = models.CharField("FirstName", max_length=20)
     last_name = models.CharField("LastName", max_length=20)
     #password = models.IntegerField("Password", max_length=10)
class Comentariu(models.Model):
     comentariu=models.CharField("Comentariu", max_length=200)
