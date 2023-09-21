from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio, name="Inicio"),
    path('Lista-Rock/', ListaRock, name="Lista de Rock"),
    path('Lista-Pop/', ListaPop, name="Lista de Pop"),
    path('Lista-Jazz/', ListaJazz, name="Lista de Jazz"),
    path('Lista-Tango/', ListaTango, name="Lista de Tango"),
    path('RockFormulario/', RockFormulario, name="RockFormulario"),
    path('PopFormulario/', PopFormulario, name="PopFormulario"),
    path('JazzFormulario/', JazzFormulario, name="JazzFormulario"),
    path('TangoFormulario/', TangoFormulario, name="TangoFormulario"),
    path('Busqueda-Bandas/', BusquedaBandas, name="BusquedaBandas"),
    path('Buscar/', Buscar, name="Buscar"),
    
]
