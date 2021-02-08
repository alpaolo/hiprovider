from django.template.defaulttags import register
from django import template
from django.template.defaultfilters import stringfilter
import urllib

register = template.Library()

@register.filter
@stringfilter
def lower(value):
    return value.lower()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_elements_for_key_value(list, args):
    result = None   
    key, value = args.split(',') 
    print("key", key,"value", value)
    for element in list:
        if element[key]==value:
            result =  element
            break
    return result

@register.filter
def urlizespace(string):
    return string.replace(" ","_")


@register.filter
def capitalize(string):
    return string.title()

@register.filter
def test(list):
   return list