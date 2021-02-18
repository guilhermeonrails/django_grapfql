from  graphene import ObjectType, List, Field, String, Schema
from graphene_django import DjangoObjectType
from receitas.models import Categoria, Ingrediente

class CategoriaType(DjangoObjectType):
    class Meta:
        model = Categoria
        fields = '__all__'

class IngredienteType(DjangoObjectType):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nome', 'nota', 'categoria')

class Query(ObjectType):
    todos_ingredientes = List(IngredienteType)
    categoria_por_nome = Field(CategoriaType, nome = String(required=True))

    def resolve_todos_ingredientes(root, info):
        return Ingrediente.objects.select_related("categoria").all()

    def resolve_categoria_por_nome(root, info, nome):
        try:
            return Categoria.objects.get(nome=nome)
        except Categoria.DoesNotExist:
            return None

schema = Schema(query=Query)
