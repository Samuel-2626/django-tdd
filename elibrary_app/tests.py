from django.test import TestCase

from .models import Catalogue

class CatalogueModelTests(TestCase):

    "Test the catalogue model"

    def setUp(self):
        self.c = Catalogue(
            title = 'First Title',
            isbn = '978-3-16-148410-0',
            author = 'Samuel Torimiro',
            price = '9.99',
            availability = 'True'
        )
        
    def test_create_catalogue(self):
        self.assertIsInstance(self.c, Catalogue)

    def test_str_representation(self):
        self.assertEquals(str(self.c), "First Title")

    
