import graphene
from .models import *
from graphene_django import DjangoObjectType

class PaisType(DjangoObjectType):
    class Meta:
        model = Pais
        departamentos = graphene.Field(graphene.List('path.to.Departamento'))
        fields = ("__all__")

class DepartamentoType(DjangoObjectType):
    class Meta:
        model = Departamento
        pais = graphene.Field('path.to.Pais')
        ciudades = graphene.Field(graphene.List('path.to.Ciudad'))
        fields = ("__all__")

class CiudadType(DjangoObjectType):
    class Meta:
        model = Ciudad
        departamento = graphene.Field('path.to.Departamento')
        fields = ("__all__")
