from django.urls import path
from django.http import HttpResponse
from django.conf.urls import url
from django.conf import settings as settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views



urlpatterns = [
    path('', lambda request: HttpResponse('Is the hiprovider index page')),
    path('prodotti/<str:name>', views.products_list, name='productslist'),
    path('produttori/<str:name>', views.producers_list, name='producerslist'),
    path('fornitori/<str:name>', views.suppliers_list, name='supplierslist'),
    path('materieprime/<str:name>', views.commodities_list, name='commoditieslist'),

 
    
    #path('imagerecognition/(?P<action>\w+)/$', views.process, name='process'),

] 

# Serving the media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#else: urlpatterns += staticfiles_urlpatterns()
else: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

