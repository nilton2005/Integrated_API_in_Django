from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha de registro', auto_now=True)
    icon = models.ImageField(max_length=200, blank=True, null=True)
    icon_class = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6,decimal_places=2) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('fecha de registro')
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre
    
