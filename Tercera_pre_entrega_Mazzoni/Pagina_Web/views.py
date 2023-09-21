from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Lista_Jazz, Lista_Pop, Lista_Rock, Lista_Tango
from .forms import RockFormulario, PopFormulario, JazzFormulario, TangoFormulario

# Create your views here.
def Banda_o_compositor_musical(req, BandaoCompositorMusical, Decada):

    Banda_o_compositor_musical = Lista_Rock(nombre=BandaoCompositorMusical, Decada=Decada)
    Banda_o_compositor_musical.save()

    Banda_o_compositor_musical = Lista_Pop(nombre=BandaoCompositorMusical, Decada=Decada)
    Banda_o_compositor_musical.save()

    Banda_o_compositor_musical = Lista_Jazz(nombre=BandaoCompositorMusical, Decada=Decada)
    Banda_o_compositor_musical.save()

    Banda_o_compositor_musical = Lista_Tango(nombre=BandaoCompositorMusical, Decada=Decada)
    Banda_o_compositor_musical.save()


def Inicio(req):

    return render(req, "Inicio.html")
    
def ListaJazz(req):

   return render(req, "Lista_Jazz.html")

def ListaRock(req):

    return render(req, "Lista_Rock.html")

def ListaPop(req):

   return render(req, "Lista_Pop.html")

def ListaTango(req):

    return render(req, "Lista_Tango.html")




def RockFormulario(req,):
    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':

            Banda_o_compositor_musical = Lista_Rock(Banda_o_compositor_musical=req.POST["banda o compositor musical"], Decada=req.POST["Decada"])
            Banda_o_compositor_musical.save()

            return render(req, "Inicio.html")         
    else:
        return render(req, "RockFormulario.html")   




def PopFormulario(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        
        Banda_o_compositor_musical = Lista_Pop(Banda_o_compositor_musical=req.POST["banda o compositor musical"], Decada=req.POST["Decada"])
        Banda_o_compositor_musical.save()
    
        return render(req, "Inicio.html") 
        
    else:
    
        return render(req, "PopFormulario.html")   





def JazzFormulario(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':

        Banda_o_compositor_musical = Lista_Jazz(Banda_o_compositor_musical=req.POST["banda o compositor musical"], Decada=req.POST["Decada"])
        Banda_o_compositor_musical.save()

        return render(req, "Inicio.html") 
        
    else:
        return render(req, "JazzFormulario.html")   






def TangoFormulario(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':

        Banda_o_compositor_musical = Lista_Tango(Banda_o_compositor_musical=req.POST["banda o compositor musical"], Decada=req.POST["Decada"])
        Banda_o_compositor_musical.save()

        return render(req, "Inicio.html") 
        
    else:
        return render(req, "TangoFormulario.html")   
    


def BusquedaBandas(req):
     return render(req, "BusquedaBandas.html")


def Buscar(req):

    return HttpResponse(f"Buscando la banda {req.GET['Banda o compositor musical']}")