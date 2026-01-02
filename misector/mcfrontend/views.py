from django.shortcuts import render

# Create your views here.
def listaLugaresMap(request):
    return render(request, 'mcfrontend/barrio_base.html')