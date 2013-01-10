from django import template

register = template.Library()


@register.filter
def get_lat(value):
    tuple = value.split(',')
    return tuple[0] 
  
@register.filter
def get_lng(value):
    tuple = value.split(',')
    return tuple[1]