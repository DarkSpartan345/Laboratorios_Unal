from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import DetailView
from .models import Laboratorio
from .forms import LaboratorioForm

def lista_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorios/lista.html', {'laboratorios': laboratorios})

class LaboratorioDetailView(DetailView):
    model = Laboratorio
    template_name = 'laboratorios/laboratorio_detail.html'

def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_laboratorios')  # Redirige a la lista después de guardar
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorios/crear_laboratorio.html', {'form': form})
        
