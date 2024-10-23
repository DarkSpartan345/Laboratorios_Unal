from django.urls import path
from .views import lista_laboratorios,LaboratorioDetailView,crear_laboratorio

urlpatterns = [
    path('', lista_laboratorios, name='lista_laboratorios'),
    path('laboratorios/<int:pk>/', LaboratorioDetailView.as_view(), name='laboratorio_detail'),
    path('crear/', crear_laboratorio, name='crear_laboratorio'),
]