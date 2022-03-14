from django.test import TestCase, SimpleTestCase
from django.urls.base import resolve
from .models import Catalogue
from django.urls import reverse
from .views import home
from .forms import AddCatalogueForm

class CatalogueTemplateTests(SimpleTestCase):
    
    def test_homepage_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'E-library Application')

    def test_hompage_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'Hello World') 
    

class CatalogueFormTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_catalogue_form(self):
        form = self.response.context.get('add_catalogue_form')
        self.assertIsInstance(form, AddCatalogueForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_bootstrap_class_used_for_default_styling(self):
        form = self.response.context.get('add_catalogue_form')
        self.assertIn('class="form-control"', form.as_p())

    def test_catalogue_form_validation_for_blank_items(self):
        add_catalogue_form = AddCatalogueForm(
            data={'title': '', 'ISBN': '', 'author': '', 'price': '', 'availability': ''}
            )
        self.assertFalse(add_catalogue_form.is_valid())


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

    def setUp(self):
        self.c = Catalogue(
            title = 'First Title',
            ISBN = '978-3-16-148410-0',
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
        first_catalogue.ISBN = '978-3-16-148410-0'
        first_catalogue.author = 'Samuel Torimiro'
        first_catalogue.price = '9.99'
        first_catalogue.availability = 'True'
        first_catalogue.save()

        second_catalogue = Catalogue()
        second_catalogue.title = 'Second Title'
        second_catalogue.ISBN = '978-3-16-148410-1'
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




    
