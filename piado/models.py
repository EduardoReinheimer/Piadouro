from django.db import models
from pessoa.models import Perfil


class Piado(models.Model):
    usuario = models.ForeignKey(Perfil, on_delete=models.PROTECT, related_name='piados')
    curtidas = models.ManyToManyField(Perfil, related_name='curtidas', blank=True)
    repiados = models.ManyToManyField(Perfil, related_name='repiados', blank=True)
    
    piado_hospedeiro = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='comentarios',
        blank=True,
        null=True)
        
    conteudo = models.CharField(max_length=400)

    data_criacao = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ['-data_criacao']
