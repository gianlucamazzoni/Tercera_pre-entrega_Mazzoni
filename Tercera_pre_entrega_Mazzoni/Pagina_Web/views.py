from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from Pagina_Web.models import Lista_Jazz, Lista_Pop, Lista_Rock, Lista_Tango
from .forms import ListaPopFormulario, ListaRockFormulario, ListaJazzFormulario, ListaTangoFormulario
# Create your views here.

def Inicio(request):

    return HttpResponse('vista de Inicio')

def Lista_Jazz(request):

    return HttpResponse('vista Jazz')

def Lista_Rock(request):

    return HttpResponse('vista Rock')

def Lista_Pop(request):

    return HttpResponse('vista Pop')

def Lista_Tango(request):

    return HttpResponse('vista tango')




def Inicio(req):

    return render(req, "Inicio.html")
    

def Lista_Jazz(req):

   return render(req, "Lista_Jazz.html")

def Lista_Rock(req):

    return render(req, "Lista_Rock.html")

def Lista_Pop(req):

   return render(req, "Lista_Pop.html")

def Lista_Tango(req):

    return render(req, "Lista_Tango.html")




def ListaRockFormulario(req):

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':

        miFormulario = ListaRockFormulario(req.POST)
        
        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            Lista = Lista_Rock(Banda_o_compositor_musical=data["Lista_Rock"], Decada = data["Decada"])
            Lista.save()

        return render(req, "Inicio.html")
    else:
        miFormulario = ListaRockFormulario(req.POST)
        return render(req, "ListaRockFormulario.html", {"miFormulario": miFormulario})

    
    
def ListaPopFormulario(req):

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':
    
        miFormulario = ListaPopFormulario()

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data    
            Lista = Lista_Pop(Banda_o_compositor_musical=data["Lista_Pop"], Decada = data["Decada"])
            Lista.save()

            return render(req, "Inicio.html")
    else:
        miFormulario = ListaPopFormulario()
        return render(req, "ListaPopFormulario.html", {"miFormulario": miFormulario})
    
def ListaJazzFormulario(req):


    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':
    
        miFormulario = ListaJazzFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data    
            Lista = Lista_Jazz(Banda_o_compositor_musical=data["Lista_Jazz"], Decada = data["Decada"])
            Lista.save()

            return render(req, "Inicio.html")
    else:
        miFormulario = ListaJazzFormulario()
        return render(req, "ListaJazzFormulario.html", {"miFormulario": miFormulario})
    
def ListaTangoFormulario(req):

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':
    
        miFormulario = ListaTangoFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data    
            Lista = Lista_Tango(Banda_o_compositor_musical=data["Lista_Tango"], Decada = data["Decada"])
            Lista.save()

            return render(req, "Inicio.html")
    else:
        miFormulario = ListaTangoFormulario()
        return render(req, "ListaTangoFormulario.html", {"miFormulario": miFormulario})
    
def busqueda_Banda_o_compositor_musical(req):

    return render(req, "busqueda_Banda_o_compositor_musical.html")

def Buscar(req: HttpRequest):

    if req.GET["Decada"]:
        Decada = req.GET["Decada"]
        lista = Lista_Rock.objects.filter, Lista_Jazz.objects.filter, Lista_Pop.object.filter, Lista_Tango.object.filter(Decada__icontains= Decada)
        return render(req, "resultadosBusqueda.html", {"banda": lista})
    else:    
        return HttpResponse(f'aun buscando la banda')