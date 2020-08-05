from django import template 

register = template.Library()

@register.filter
def exists(user, user_list):
    return user_list.filter(usuario__username=user.username).count() == 1