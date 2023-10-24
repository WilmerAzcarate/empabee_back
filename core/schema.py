from .types import *
        
class traerPaises(graphene.ObjectType):
    paises = graphene.List(PaisType)
    
    def resolve(self,info):
        paises = Pais.objects.all()
        return traerPaises(paises=paises)
    
class traerDepartamentos(graphene.ObjectType):
    departamentos = graphene.List(DepartamentoType)
    
    def resolve(self,info):
        departamentos = Departamento.objects.all()
        return traerDepartamentos(departamentos=departamentos)
    
class traerCiudades(graphene.ObjectType):
    ciudades = graphene.List(CiudadType)
    
    def resolve(self,info):
        ciudades = Ciudad.objects.all()
        return traerCiudades(ciudades=ciudades)