from django.test import TestCase, Client
from django.urls import reverse
from .models import AthleteData, MealData
from .forms import AthleteForm
class DietAppViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'DietApp/main.html')

    def test_predict_view_get(self):
        response = self.client.get(reverse('predict'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'DietApp/index.html')
        self.assertIsInstance(response.context['form'], AthleteForm)

    def test_predict_view_post_valid_form(self):
        data = {'your_form_data_here'}  # Replace with valid form data
        response = self.client.post(reverse('predict'), data)
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect
        self.assertRedirects(response, reverse('recommended_meal'))

        # Add assertions to check if the form data was saved in the database, if necessary

    def test_viewpredictions_view(self):
        response = self.client.get(reverse('viewpredictions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'DietApp/predictions.html')

        # Add assertions to check the content of the response, if necessary

    def test_view_meals_view(self):
        response = self.client.get(reverse('view_meals'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'DietApp/meals.html')

        # Add assertions to check the content of the response, if necessary

    def test_recommended_meal_view(self):
        response = self.client.get(reverse('recommended_meal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'DietApp/meal.html')

        # Add assertions to check the content of the response, if necessary

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # 302 indicates a redirect
        self.assertRedirects(response, reverse('main'))

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'DietApp/about.html')

