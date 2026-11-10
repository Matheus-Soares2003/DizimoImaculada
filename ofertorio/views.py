from django.shortcuts import render

# Create your views here.
def ofertorios(request):
    return render(request, 'ofertorio.html')