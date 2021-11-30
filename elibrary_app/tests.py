from django.test import TestCase, SimpleTestCase

from .models import Profile

from django.urls import reverse

# Create your tests here.

class TestUserProfile(SimpleTestCase):

    def test_user_profile_contains_correct_html(self):
        
        response = self.client.get(reverse('user'))
        self.assertContains(response, 'Profile')

    def test_user_profile_template(self):

        response = self.client.get(reverse('user'))
        self.assertTemplateUsed(response, 'user.html')

    def test_user_profile_code(self):

        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, 200)


class TestUserProfileModel(TestCase):

    def test_create_user_profile(self):

        self.profile = Profile.objects.create(
            first_name = 'Samuel',       
            last_name = 'Torimiro',
        )

        self.assertEqual(f'{self.profile.first_name}', 'Samuel')
        self.assertEqual(f'{self.profile.last_name}', 'Torimiro')
