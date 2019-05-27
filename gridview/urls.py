from django.urls import path
from .views import viewgrid, updategrid, highestbond
urlpatterns = [
    path('', viewgrid, name='viewgrid'),
    path('updategrid', updategrid, name='updategrid'),
    path('highestbond', highestbond, name='highestbond')
]
