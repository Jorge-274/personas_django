from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')


def despedirse(request):
    return HttpResponse('Despedirse desde Django')


def contactar(request):
    return HttpResponse('Contactos'
                        'Telefono: 0971214665'
                        'Email: Laalsdfjs@adslkflsa.com'
                        'Eso es todo')


