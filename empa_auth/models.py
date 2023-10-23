from django.db import models
from django.utils import timezone
from core.models import *
from .views import AuthUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class Persona(AbstractBaseUser,PermissionsMixin):
    primer_nombre = models.CharField(max_length=45)
    segundo_nombre = models.CharField(max_length=45, blank=True, null=True)
    primer_apellido = models.CharField(max_length=45)
    segundo_apellido = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=9,choices=Genero.choices)
    telefono = models.CharField(max_length=120)
    correo = models.CharField(max_length=120,null=True)
    n_identificacion = models.IntegerField(unique=True)
    ciudad_residencia = models.ForeignKey(Ciudad, models.DO_NOTHING,null=True,related_name='persona_residencia')
    ciudad_nacimiento = models.ForeignKey(Ciudad, models.DO_NOTHING,null=True,related_name='persona_nacimiento')
    tipo_identificacion = models.ForeignKey(TipoIdentificacion,models.DO_NOTHING,null=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AuthUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['primer_nombre','primer_apellido','n_identificacion']
    
    class Meta:
        managed = True
        db_table = 'persona'

    def __str__(self) -> str:
        p_nombre = self.p_nombre
        p_apellido = self.p_apellido
        return p_nombre+" "+p_apellido
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)