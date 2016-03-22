from datetime import datetime

from django.test import TestCase
from nairalirayoga.core.models import Horario, Preco, Professor, Imagem

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

class PrecoModelTest(TestCase):
    def setUp(self):
        self.obj = Preco(
            valor=130.0,
            dias='3x por semana',
            atividade='aula de yoga',
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Preco.objects.exists())

    def test_create_at(self):
        """ Horario must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

class ProfessorModelTest(TestCase):
    def setUp(self):
        self.obj = Professor(
            nome='Naira',
            sobrenome='Lira',
            descricao='Ótima professora',
            foto='naira_lira.png',
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Professor.objects.exists())

    def test_create_at(self):
        """ Horario must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

class ImagesModelTest(TestCase):
    def setUp(self):
        self.obj = Imagem(
            titulo='Yoga',
            descricao='faz bem',
            foto='naira_lira.png',
            carrosel=True
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Imagem.objects.exists())

    def test_create_at(self):
        """ Horario must have an auto created at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)