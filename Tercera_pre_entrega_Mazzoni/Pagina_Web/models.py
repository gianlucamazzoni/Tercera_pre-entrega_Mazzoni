from django.db import models

# Create your models here.
class Lista_Jazz(models.Model):
    Banda_o_compositor_musical = models.CharField(max_length=40)
    Decada = models.IntegerField()

    def __str__(self):
        return f'{self.Banda_o_compositor_musical} - {self. Decada}'


class Lista_Rock(models.Model):
    Banda_o_compositor_musical = models.CharField(max_length=40)
    Decada = models.IntegerField()

    def __str__(self):
        return f'{self.Banda_o_compositor_musical} - {self. Decada}'

class Lista_Pop(models.Model):
    Banda_o_compositor_musical = models.CharField(max_length=40) 
    Decada = models.IntegerField()

    def __str__(self):
        return f'{self.Banda_o_compositor_musical} - {self. Decada}'

class Lista_Tango(models.Model):
    Banda_o_compositor_musical = models.CharField(max_length=40)
    Decada = models.IntegerField()

    def __str__(self):
        return f'{self.Banda_o_compositor_musical} - {self. Decada}'