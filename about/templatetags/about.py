from django import template
from ..models import About

register = template.Library()

@register.simple_tag()
def get_about():
    obj = About.obkects.get(id=1)
    return obj