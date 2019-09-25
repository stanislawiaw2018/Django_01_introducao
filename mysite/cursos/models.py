from django.db import models

# Create your models here.
class Curso(models.Model):
    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Apreviação")
    description = models.TextField("Descrição")
    start_date = models.DateField("Data de Inicio", null=True, blank=True)
    image = models.ImageField(upload_to='cursos/images', verbose_name="Imagem", null=True, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['name']