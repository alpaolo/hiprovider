from django.template.defaulttags import register
from django import template

from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def lower(value):
    return value.lower()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)