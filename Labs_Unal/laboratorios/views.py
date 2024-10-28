from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import DetailView
from .models import Laboratorio
from .forms import LaboratorioForm,UpdateLaboratorioForm
from django.db.models import Case, When

id_order = [6,7,8,5,1,2,3,4]
def lista_laboratorios(request):
    laboratorios = Laboratorio.objects.filter(id__in=id_order).order_by(
    Case(*[When(id=id, then=pos) for pos, id in enumerate(id_order)]))
    return render(request, 'laboratorios/index.html', {'laboratorios': laboratorios})

class LaboratorioDetailView(DetailView):
    model = Laboratorio
    template_name = 'laboratorios/laboratorio_detail.html'

def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            laboratorio = form.save(commit=False)
            if 'imagen' in request.FILES:
                laboratorio.imagen = request.FILES['imagen']
            laboratorio.save()
            return redirect('laboratorio_detail', pk=laboratorio.id)
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorios/crear_laboratorio.html', {'form': form})

def update_laboratorio(request, lab_id):
    laboratorio = get_object_or_404(Laboratorio, id=lab_id)
    if request.method == 'POST':
        form = UpdateLaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            laboratorio = form.save(commit=False)
            if 'imagen' in request.FILES:
                laboratorio.imagen = request.FILES['imagen']
            laboratorio.save()
            return redirect('laboratorio_detail', pk=laboratorio.id)
    else:
        form = UpdateLaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorios/Modificar_laboratorio.html', {'form': form})
        
