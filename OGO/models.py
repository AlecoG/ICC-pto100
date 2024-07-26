from django.db import models

# Create your models here.

class interrupcione(models.Model):
    ot=models.IntegerField()
    fecha=models.DateField()
    descripcion=models.CharField(max_length=50)
    problema=models.CharField(max_length=50)
    unidad=models.CharField(max_length=20)
    usuario=models.CharField(max_length=20)
    
    #especialidad=models.CharField(max_length=20)
    defectado=models.CharField(max_length=20)
    solucionado=models.CharField(max_length=20)
    fecha=models.CharField(max_length=20)
    ubicacion=models.CharField(max_length=20)
    observaciones=models.CharField(max_length=20)
    

class entradaYSalidaDeMedio(models.Model):
    ot=models.IntegerField()
    equipo=models.CharField(max_length=20)
    lugar=models.CharField(max_length=50)
    marca=models.CharField(max_length=20)
    serie=models.CharField(max_length=20)
    sello=models.CharField(max_length=20)
    rotura=models.CharField(max_length=50)
# entrada a la unidad
    fecha_entrada = models.DateField()
    entrega_entrada = models.CharField(max_length=20)
    recibe_entrada = models.CharField(max_length=20)
    firma_entrada = models.BooleanField()
# entrega a reparacion 
    fecha_reparacion = models.DateField(null=False )
    entrega_reparacion = models.CharField(max_length=20)
    recibe_reparacion = models.CharField(max_length=20)
    firma_reparacion = models.BooleanField()
# entrega al usuario
    fecha_salida = models.DateField()
    entrega_salida = models.CharField(max_length=20, null=False, default="prueba" )
    recibe_salida = models.CharField(max_length=20)
    observacion = models.CharField(max_length=50) 

class resumenTrabajo(models.Model):
    informatica=models.CharField(max_length=5)    