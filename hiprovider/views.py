from django.shortcuts import render

# Create your views here.
import os
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings as conf_settings
from pathlib import Path
from .data.data import get_commodities, get_producers, get_suppliers, get_products





# This views satisfy any kind of url with appropriate view and template but is confused
args = {}
args ={'section':'ai', 'title': 'Image recognition'}

def index(request):
    return HttpResponse("Hello, world. Is upload section")


def producers_list(request, name=''): # va tutto spostato in models
    print(name)
    data = get_producers()
    result = data
    result = get_element(data,name)
    args['items'] = result
    return render(request, 'list.html', args)
    
    
def suppliers_list(request, name=''): # va tutto spostato in models
    data = get_suppliers()
    result = data
    args['items'] = result
    return render(request, 'list.html', args)
    return HttpResponse("\n"+ result) 

def commodities_list(request, name=''): # va tutto spostato in models
    data = get_commodities()
    result = data
    args['items'] = result
    return render(request, 'list.html', args)
    return HttpResponse("\n"+ bytes(result, "utf-8").decode("unicode_escape")) 

def products_list(request, name=''): # va tutto spostato in models
    args['products'] = get_products()
    args['producers'] = get_producers()
    args['product']  = get_element(args['products'],name)
    args['producer'] = get_element(args['producers'], 1)
    return render(request, 'product_list.html', args)

def get_element(data, value):
    result = None
    for items in data:
        for i in items:
            if value in items[i].lower():
                result = items
                print(items)
                #result = ""+json.dumps(items, indent = 4)
                break
        #[items[x] for x in items]
    return result