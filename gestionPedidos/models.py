from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=10)

    def __str__(self):
        return 'El nombre es: %s, la direccion es: %s, el email es: %s, y el telefono es: %s' %(self.nombre, self.direccion, self.email, self.telefono)


class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    
    def __str__(self):
        return 'El nombre es: %s, la seccion es: %s, el precio es: %s' %(self.nombre, self.seccion, self.precio)



class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

    def __str__(self):
        return 'El numero es: %s, la fecha es: %s, esta entregado: %s' %(self.numero, self.fecha, self.entregado)
