from django import template 

register = template.Library()

@register.filter
def exists(profile, profile_list):
    return profile_list.filter(pk=profile.pk).count() == 1