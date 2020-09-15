from django import template 
from piado.models import Piado

register = template.Library()

@register.filter
def already_repiado(user, piado):
    return Piado.objects.filter(proprietario=user, repiado_hospedeiro=piado).exists()