from django.db import models
from django.db.models.query_utils import select_related_descend

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    nota = models.TextField()
    categoria = models.ForeignKey(Categoria, related_name="ingredientes", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
        
