from django.http import response
from django.test import TestCase, SimpleTestCase

from .models import Catalogue
from django.urls import reverse

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

class ElibraryURLsTest(SimpleTestCase):

    "Test the catalogue URLs"

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    
