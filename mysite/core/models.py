from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Livraria(models.Model):
    titulo = models.CharField(max_length=50)
    nome_autor = models.CharField(max_kength=50)
    assunto = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    ISBN = models.IntegerField(max_length=15)
    ano_publicacao = models.DateField()

    def __str__(self):
        return self.titulo