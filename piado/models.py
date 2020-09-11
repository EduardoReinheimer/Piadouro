from django.db import models
from django.contrib.auth.models import User


class Piado(models.Model):
    proprietario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='piados')
    curtidas = models.ManyToManyField(User, related_name='curtidas', blank=True)

    repiado_hospedeiro = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='repiados',
        blank=True,
        null=True)

    comentario_hospedeiro = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='comentarios',
        blank=True,
        null=True) 

    conteudo = models.CharField(max_length=400)
    data_criacao = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ['-data_criacao']
