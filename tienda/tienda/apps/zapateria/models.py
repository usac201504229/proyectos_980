from django.db import models

# Create your models here.

class Facturacion(models.Model):
    Nombre = models.CharField(max_length=25)
    Apellido = models.CharField(max_length=25)
    Direccion = models.CharField(max_length=35)
    Nit = models.CharField(max_length=8)

    def NombreCompleto(self):
        cadena = "{0}, {1}"
        return cadena.format(self.Apellido, self.Nombre)

    def __str__(self):
        return self.NombreCompleto()

class Zapato(models.Model):
    Zapatos = (('A', 'Adidas'), ('N', 'Nike'), ('Z', 'Zapato'))
    Zapatoss = models.CharField(max_length=1, choices=Zapatos, default='J')
    cantidad = models.PositiveSmallIntegerField()
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0}, ({1})".format(self.Zapatoss, self.cantidad)

class Tarjeta(models.Model):
    Nombre = models.CharField(max_length=25)
    Numero = models.CharField(max_length=15)
    Fecha = models.DateField()
    CVV = models.CharField(max_length=3)

    def NTarjeta(self):
        cadena2 = "{0}, {1}"
        return cadena2.format(self.Nombre, self.Numero)

    def __str__(self):
        return self.NTarjeta()

class Pedido(models.Model):
    Facturacion = models.ForeignKey(Facturacion, null=False, blank=False, on_delete=models.CASCADE)
    Zapato = models.ForeignKey(Zapato, null=False, blank=False, on_delete=models.CASCADE)
    Tarjeta = models.ForeignKey(Tarjeta, null=False, blank=False, on_delete=models.CASCADE)    
    Pedido = models.DateTimeField(auto_now=True)

    def __str__(self):
        cadena3 = "{0} => {1}"
        return cadena3.format(self.Facturacion, self.Zapato.Zapatoss)
