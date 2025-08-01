from django.test import TestCase
from .models import Livro


# Create your tests here.
class LivroModelTest(TestCase):
    def test_criacao_livro(self):
        livro = Livro.objects.create(
            titulo="Django para Iniciantes",
            autor="João Sanchez",
            publicado_em="2020-01-01",
        )
        self.assertEqual(str(livro), "Django para Iniciantes")
