from django.urls import path
from .views import viewgrid, updategrid
urlpatterns = [
    path('', viewgrid, name='viewgrid'),
    path('updategrid', updategrid, name='updategrid'),
]
