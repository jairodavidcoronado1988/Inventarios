from django.db import models

# Create your models here.


class Comercial(models.Model):
    
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField()
    pais = models.CharField(max_length=80)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
 
class Producto(models.Model):
    
    id_producto = models.CharField(primary_key=True, max_length=100)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    estado = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    
    nit = models.CharField(primary_key=True, max_length=100 )
    nombre = models.CharField(max_length=250)
    direccion = models.CharField(max_length=100)
    telefono_empresa = models.CharField(max_length=10)
    nombre_contact = models.CharField(max_length=80)
    tel_contact = models.CharField(max_length=80)
    email_contact = models.EmailField()
    comercial = models.ForeignKey(Comercial, on_delete=models.CASCADE, related_name="comerciallist")
    productos = models.ManyToManyField(Producto, related_name="productoslist")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
class Actualizacion(models.Model):
    
    fecha_actualizacion = models.DateField()
    descripcion = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,related_name="empresas")
    producto = models.ManyToManyField(Producto, related_name="productos")
    
    def __str__(self):
        return self.descripcion
    
class Ot(models.Model):
    
    Ot = models.CharField(max_length=10, primary_key=True)
    empresas = models.ForeignKey(Empresa, on_delete = models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

class Ciudad(models.Model):
    
    nom_ciudad = models.CharField(max_length=100)
    nom_municipio = models.CharField(max_length=100)
    nom_departamento = models.CharField(max_length=100)