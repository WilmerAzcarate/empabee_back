import graphene
import graphql_jwt
from django.views.decorators.csrf import csrf_exempt
from graphql_jwt.decorators import login_required

from core.types import *
from empa_auth.types import *

class Query(graphene.ObjectType):
    paises = graphene.List(PaisType)
    departamentos = graphene.List(DepartamentoType)
    ciudades = graphene.List(CiudadType)
    user = graphene.Field(PersonaType,token=graphene.String(required=True))
    
    @login_required
    def resolve_user(self, info,**kwargs):
        return info.context.user
        
    @csrf_exempt
    def resolve_paises(self, info):
        return Pais.objects.all()
    
    @csrf_exempt
    def resolve_departamentos(self, info):
        return Departamento.objects.all()
    
    @csrf_exempt
    def resolve_ciudades(self, info):
        return Ciudad.objects.all()

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)