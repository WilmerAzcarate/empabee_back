import graphene
from graphene_django import DjangoObjectType

from .models import *

class PaisType(DjangoObjectType):
    class Meta:
        model = Pais
        departamentos = graphene.Field(graphene.List('path.to.Departamentos'))
        fields = ("__all__")
        
class traerPaises(graphene.ObjectType):
    paises = graphene.List(PaisType)
    
    def resolve(self,info):
        paises = Pais.objects.all()
        return traerPaises(paises=paises)