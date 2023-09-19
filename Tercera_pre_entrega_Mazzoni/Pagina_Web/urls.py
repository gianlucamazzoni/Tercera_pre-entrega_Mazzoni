from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio, name="Inicio"),
    path('Lista-Rock/', Lista_Rock, name="Lista de Rock"),
    path('Lista-Pop/', Lista_Pop, name="Lista de Pop"),
    path('Lista-Jazz/', Lista_Jazz, name="Lista de Jazz"),
    path('Lista-Tango/', Lista_Tango, name="Lista de Tango"),
    path('ListaRockFormulario/', ListaRockFormulario, name="ListaRockFormulario"),
    path('ListaPopFormulario/', ListaPopFormulario, name="ListaPopFormulario"),
    path('ListaJazzFormulario/', ListaJazzFormulario, name="ListaJazzFormulario"),
    path('ListaTangoFormulario/', ListaTangoFormulario, name="ListaTangoFormulario"),
    path('busqueda_Banda_o_compositor_musical/', busqueda_Banda_o_compositor_musical, name="busqueda_Banda_o_compositor_musical"),
    path('Buscar/', Buscar, name="Buscar"),    
]
