from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', curso, name = 'curso'),
    re_path(r'^(?P<pk>\d+)/$', detalhe, name = 'detalhe'),
   
   
]