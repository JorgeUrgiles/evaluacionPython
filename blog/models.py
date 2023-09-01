from django.db import models
from django.utils.timezone import now
# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=50, verbose_name="Nombre")
    created=models.DateTimeField( auto_now=False, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

class Meta:
    verbose_name="Categoria"
    verbose_name_plural="Categorias"
    ordering=["name"]

def __str__(self):
    return self.name

class Blog(models.Model):
    title=models.CharField(max_length=100, verbose_name="Titulo")
    content=models.TextField(verbose_name="Contenido")
    published=models.DateTimeField(verbose_name="Fecha de publicacion",default=now)
    image=models.ImageField(verbose_name="Image",upload_to="blog")
    author=models.CharField(max_length=100,verbose_name="Autor")
    categories=models.CharField(max_length=100,verbose_name="Categoria")
    created=models.DateTimeField( auto_now=False, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")