from django.db import models
from django.utils import timezone

# Create your models here.
class Genero(models.TextChoices):
    MASCULINO = 'M', 'Masculino'
    FEMENINO = 'F', 'Femenino'

class Pais(models.Model):
    codigo = models.SmallIntegerField()
    iso3166a1 = models.CharField(max_length=2)
    iso3166a2 = models.CharField(max_length=6)
    nombre = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'pais'

    def __str__(self) -> str:
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
        
class Departamento(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.IntegerField()
    pais = models.ForeignKey(Pais, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'departamento'

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=535)
    codigo = models.IntegerField()
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'ciudad'

    def __str__(self) -> str:
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
        
class TipoIdentificacion(models.Model):
    nombre = models.CharField(max_length=45)
    diminutivo = models.CharField(max_length=3,null=True)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_identificacion'

    def __str__(self):
        return self.nombre+" ("+self.diminutivo+")"
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)