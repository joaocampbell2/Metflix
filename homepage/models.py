from django.db import models

class Filme(models.model):
    nome = models.CharField('Nome', max_length=50)
    sinopse = models.CharField('Sinopse', max_length=300)
    duracao = models.IntegerField('Duração')
    categorias = [(),()]
    categoria = models.CharField('Categoria', choices=categorias, max_length=20)
    capa = models.ImageField('Capa')
    trailer = models.URLField('Link para Trailer', max_length=1000)
    lancamento = models.DateField('Data de Lançamento')