from django import forms

class ListaRockFormulario(forms.Form):

    lista_rock = forms.CharField(max_length=40)
    Decada = forms.IntegerField()


class ListaPopFormulario(forms.Form):

    Lista_Pop = forms.CharField(max_length=40)
    Decada = forms.IntegerField()

class ListaJazzFormulario(forms.Form):

    Lista_Jazz = forms.CharField(max_length=40)
    Decada = forms.IntegerField()

class ListaTangoFormulario(forms.Form):

    Lista_Tango = forms.CharField(max_length=40)
    Decada = forms.IntegerField()