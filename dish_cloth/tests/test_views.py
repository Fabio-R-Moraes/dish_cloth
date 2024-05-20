from django.test import TestCase
from django.urls import reverse, resolve
from dish_cloth import views

class ClothsViewsTest(TestCase):
    def test_cloths_home_view_is_correct(self):
        view = resolve(reverse('dish_cloth-home'))
        self.assertIs(view.func, views.home)

    def test_cloths_dish_cloth_view_is_correct(self):
        view = resolve(reverse('dish_cloth-cloth', kwargs={'id':1}))
        self.assertIs(view.func, views.dish_cloth)

    def test_cloths_category_view_is_correct(self):
        view = resolve(reverse('category', kwargs={'category_id':1}))
        self.assertIs(view.func, views.category)

    def test_cloths_home_view_return_code_200_ok(self):
        response = self.client.get(reverse('dish_cloth-home'))
        self.assertEqual(response.status_code, 200)

    def test_cloths_home_view_load_correct_template(self):
        response = self.client.get(reverse('dish_cloth-home'))
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_cloths_home_show_cloth_not_found(self):
        response = self.client.get(reverse('dish_cloth-home'))
        self.assertIn('<h1>Não há panos de prato para mostrar</h1>', 
                      response.content.decode('utf-8'))
    
    def test_cloths_category_view_return_404_if_not_found(self):
        response = self.client.get(reverse('category', kwargs={'category_id':1000}))
        self.assertEqual(response.status_code, 404)

    def test_cloths_dish_cloth_view_return_404_if_not_found(self):
        response = self.client.get(reverse('dish_cloth-cloth', kwargs={'id':1000}))
        self.assertEqual(response.status_code, 404)

