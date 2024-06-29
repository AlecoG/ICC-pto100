from django.db import models

# Create your models here.


class especialidades(models.Model):
    rama = models.CharField(max_length=20)
    
    def __str__(self):
        return self.rama

class agrupaciones(models.Model):
    unidad = models.CharField(max_length=20)
    
    def __str__(self):
        return self.unidad

class audiovisuale(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    agrupacion = models.ForeignKey(agrupaciones, on_delete=models.CASCADE)
    asignacion = models.CharField(max_length=50)
    equipo = models.CharField(max_length=50) 
    no_inventario = models.CharField(max_length=20, blank=True,null=True)
    no_serie = models.CharField(max_length=20, blank=True,null=True)
    sello = models.CharField(max_length=20, blank=True,null=True)
    fisico = models.CharField(max_length=50)
    precio = models.FloatField()
    observaciones = models.CharField(max_length=50)
    ultima_ubicacion = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    ultima_fecha = models.DateField()


class comunicacione(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    agrupacion = models.ForeignKey(agrupaciones, on_delete=models.CASCADE)
    asignacion = models.CharField(max_length=50)
    equipo = models.CharField(max_length=50) 
    no_inventario = models.CharField(max_length=20, blank=True,null=True)
    no_serie = models.CharField(max_length=20, blank=True,null=True)
    sello = models.CharField(max_length=20, blank=True,null=True)
    fisico = models.CharField(max_length=50)
    precio = models.FloatField()
    observaciones = models.CharField(max_length=50)
    ultima_ubicacion = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    ultima_fecha = models.DateField()
    
 
class informatica(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    agrupacion = models.ForeignKey(agrupaciones, on_delete=models.CASCADE)
    asignacion = models.CharField(max_length=50)
    equipo = models.CharField(max_length=50) 
    no_inventario = models.CharField(max_length=20, blank=True,null=True)
    no_serie = models.CharField(max_length=20, blank=True,null=True)
    sello = models.CharField(max_length=20, blank=True,null=True)
    fisico = models.CharField(max_length=50)
    precio = models.FloatField()
    observaciones = models.CharField(max_length=50)
    ultima_ubicacion = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    ultima_fecha = models.DateField()
    

class utilesYHerramienta(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    agrupacion = models.ForeignKey(agrupaciones, on_delete=models.CASCADE)
    asignacion = models.CharField(max_length=50)
    equipo = models.CharField(max_length=50) 
    no_inventario = models.CharField(max_length=20, blank=True,null=True)
    no_serie = models.CharField(max_length=20, blank=True,null=True)
    sello = models.CharField(max_length=20, blank=True,null=True)
    fisico = models.CharField(max_length=50)
    precio = models.FloatField()
    observaciones = models.CharField(max_length=50)
    ultima_ubicacion = models.CharField(max_length=50)
    lugar = models.CharField(max_length=50)
    ultima_fecha = models.DateField()
    
    
class cate(models.Model):
    no = models.PositiveIntegerField()
    especialidad = models.ForeignKey(especialidades, on_delete=models.CASCADE)
    noCATE = models.PositiveIntegerField(verbose_name="no CATE")
    fechaCATE = models.DateField(verbose_name="fecha CATE")
    tipo_de_medio = models.CharField(max_length=50)
    no_inventario = models.CharField(max_length=20, blank=True,null=True)
    no_serie = models.CharField(max_length=20, blank=True,null=True)
    sello = models.CharField(max_length=20, blank=True,null=True)
    usuario = models.CharField(max_length=20)
    defecto = models.CharField(max_length=50)
    fechaSalida = models.DateField(verbose_name="fecha de salida")
    
    