from django.urls import path
from django.http import HttpResponse
from django.conf.urls import url
from django.conf import settings as settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views



urlpatterns = [
    path('', lambda request: HttpResponse('Is the hiprovider index page')),
    path('prodotti/', views.products_list, name='productslist'),
    path('prodotti/<str:name>', views.single_product_list, name='single_product'),
    path('fornitori/', views.suppliers_list, name='suppliers'),
    path('fornitori/<str:name>', views.single_supplier_list, name='single_supplier'),
    path('produttori/', views.producers_list, name='producers'),
    path('produttori/<str:name>', views.single_producer_list, name='single_producer'),
    path('ingredienti/', views.ingredients_list, name='ingredients'),
    path('ingredienti/<str:name>', views.single_ingredient_list, name='single_ingredient'),

 
    
    #path('imagerecognition/(?P<action>\w+)/$', views.process, name='process'),

] 

# Serving the media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#else: urlpatterns += staticfiles_urlpatterns()
else: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

