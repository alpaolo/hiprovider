from django.shortcuts import render

# Create your views here.
import os
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings as conf_settings
from pathlib import Path
from .data.data import get_ingredients, get_producers, get_suppliers, get_articles





# This views satisfy any kind of url with appropriate view and template but is confused
args = {}
args ={'section':'ai', 'title': 'Image recognition'}

def index(request):
    return HttpResponse("Hello, world. Is upload section")


def producers_list(request): #***** va tutto spostato in models e usate le query per non caricare ol data base in memoria
    args['producers'] = get_producers()
    return render(request, 'producers_list.html', args)

def single_producer_list(request, name=''): #***** va tutto spostato in models e usate le query per non caricare ol data base in memoria
    print(name)
    data = get_producers()
    result = data
    result = get_element(data,name)
    args['producer'] = result
    return render(request, 'single_producer_list.html', args)
    
    

def suppliers_list(request): #***** va tutto spostato in models e usate le query per non caricare ol data base in memoria
    args['suppliers'] = get_suppliers()
    return render(request, 'list.html', args)
    return HttpResponse("\n"+ result) 

def single_supplier_list(request, name=''): #***** va tutto spostato in models e usate le query per non caricare ol data base in memoria
    name = name.replace("_"," ")
    args['products'] = get_articles()
    args['producers'] = get_producers()
    args['ingredients'] = get_ingredients()
    args['suppliers'] = get_suppliers()
    args['supplier'] = get_element( args['suppliers'], lambda x: x['nome'].lower() == name.lower())
    args['supplier_ingredients'] = get_elements(args['ingredients'], lambda x: x['id_fornitore'] == args['supplier']['id'])
    return render(request, 'single_supplier_list.html', args)
    return HttpResponse("\n"+ result) 


def ingredients_list(request): ##***** va tutto spostato in models e usate le query per non caricare ol data base in memoria
    data = get_ingredients()
    result = data
    args['ingredients'] = result
    return render(request, 'list.html', args)
    return HttpResponse("\n"+ bytes(result, "utf-8").decode("unicode_escape")) 

def single_ingredient_list(request, name=''): #***** va tutto spostato in models e usate le query per non caricare ol data base in memoria
    data = get_ingredients()
    result = data
    args['ingredient'] = result
    return render(request, 'list.html', args)
    return HttpResponse("\n"+ bytes(result, "utf-8").decode("unicode_escape")) 

def products_list(request): #***** va tutto spostato in models e usate le query per non caricare ol data base in memoria
    args['products'] = get_articles()
    return render(request, 'products_list.html', args)


def single_product_list(request, name=''): #***** va tutto spostato in models e usate le query per non caricare ol data base in memoria
    name = name.replace("_"," ")
    args['products'] = get_articles()
    args['producers'] = get_producers()
    args['ingredients'] = get_ingredients()
    args['suppliers'] = get_suppliers()
    args['product']  = get_element(args['products'], lambda x: x['articolo'].lower() == name)
    args['producer'] = get_element(args['producers'], lambda x: x['id'] == args['product']['id_produttore'])
    args['article_ingredients'] = get_elements(args['ingredients'], lambda x: x['id_prodotto'] == args['product']['id'])
    return render(request, 'single_product_list.html', args)




def get_element(list, filter):
    for x in list:
        print (x)
        if filter(x):
            return x
    return False

def get_elements(list, filter):
    result = []
    for x in list:
        if filter(x):
            result.append(x)
    return result

 