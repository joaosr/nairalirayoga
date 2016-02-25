from datetime import datetime

from django.test import TestCase
from nairalirayoga.core.models import Horario

class HorarioModelTest(TestCase):
    def setUp(self):
        self.obj = Horario(
            dia_semana='Segunda-feira',
            horario='19:00',
            local='oiam',
            descricao='Aula de yoga'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Horario.objects.exists())

    def test_created_at(self):
        """ Horario must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Segunda-feira', str(self.obj))