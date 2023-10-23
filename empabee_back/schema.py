import graphene
import graphql_jwt
from django.views.decorators.csrf import csrf_exempt

from core.schema import *

@csrf_exempt
def say_hello():
    return graphene.String(default_value="Hi!")

class Query(graphene.ObjectType):
    hello = say_hello()
    paises = graphene.List(PaisType)
    
    @csrf_exempt
    def resolve_paises(self, info):
        return Pais.objects.all()
    
   
    
    
class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query,mutation=Mutation)