from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_dizimistas(request):
    return HttpResponse("Página de Dizimistas")