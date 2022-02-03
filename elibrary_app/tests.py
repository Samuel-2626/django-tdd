from django.test import TestCase, SimpleTestCase
from django.urls.base import resolve
from .models import Catalogue
from django.urls import reverse
from .views import home

class ElibraryURLsTest(SimpleTestCase):
    "Test the catalogue URLs"

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_root_url_resloves_to_homepage_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home)

class CatalogueModelTests(TestCase):

    "Test the catalogue model"

    def setUp(self):a
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

    def test_saving_and_retrieving_catalogue(self):
        first_catalogue = Catalogue()
        first_catalogue.title = 'First Title'
        first_catalogue.isbn = '978-3-16-148410-0'
        first_catalogue.author = 'Samuel Torimiro'
        first_catalogue.price = '9.99'
        first_catalogue.availability = 'True'
        first_catalogue.save()

        second_catalogue = Catalogue()
        second_catalogue.title = 'Second Title'
        second_catalogue.isbn = '978-3-16-148410-1'
        second_catalogue.author = 'Hannah Torimiro'
        second_catalogue.price = '19.99'
        second_catalogue.availability = 'False'
        second_catalogue.save()

        saved_catalogues = Catalogue.objects.all()
        self.assertEqual(saved_catalogues.count(), 2)

        first_saved_catalogue = saved_catalogues[0]
        second_saved_catalogue = saved_catalogues[1]
        self.assertEqual(first_saved_catalogue.title, 'First Title')
        self.assertEqual(second_saved_catalogue.author, 'Hannah Torimiro')




    
