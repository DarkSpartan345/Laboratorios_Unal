from django.test import TestCase
from .models import Laboratorio

class LaboratorioModelTest(TestCase):

    def setUp(self):
        Laboratorio.objects.create(
            titulo="Codificador Binario a Hexadecimal",
            descripcion="Implementación de un codificador binario a hexadecimal con un display de 7 segmentos y PSoC.",
            fecha="2024-10-01"
        )

    def test_laboratorio_creation(self):
        laboratorio = Laboratorio.objects.get(titulo="Codificador Binario a Hexadecimal")
        self.assertEqual(laboratorio.descripcion, "Implementación de un codificador binario a hexadecimal con un display de 7 segmentos y PSoC.")
        self.assertEqual(str(laboratorio), "Codificador Binario a Hexadecimal")

    def test_laboratorio_count(self):
        count = Laboratorio.objects.count()
        self.assertEqual(count, 1)
