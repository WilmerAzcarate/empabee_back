import graphene
from graphene_django import DjangoObjectType
from .models import *

class PersonaType(DjangoObjectType):
    class Meta:
        model = Persona
        fields = ("__all__")
    