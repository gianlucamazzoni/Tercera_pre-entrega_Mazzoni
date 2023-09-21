from django import forms

class RockFormulario(forms.Form):

    lista_rock = forms.CharField(max_length=40)
    Decada = forms.IntegerField()


class PopFormulario(forms.Form):

    Lista_Pop = forms.CharField(max_length=40)
    Decada = forms.IntegerField()

class JazzFormulario(forms.Form):

    Lista_Jazz = forms.CharField(max_length=40)
    Decada = forms.IntegerField()

class TangoFormulario(forms.Form):

    Lista_Tango = forms.CharField(max_length=40)
    Decada = forms.IntegerField()