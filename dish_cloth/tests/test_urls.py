from django.test import TestCase
from django.urls import reverse

class ClothsURLsTest(TestCase):
    def test_cloths_home_url_is_correct(self):
        url = reverse('dish_cloth:home')
        self.assertEqual(url, '/')

    def test_cloths_category_url_is_correct(self):
        url = reverse('dish_cloth:category', kwargs={'category_id':1})
        self.assertEqual(url, '/dish_cloth/category/1/')

    def test_cloths_cloth_url_is_correct(self):
        url = reverse('dish_cloth:cloth', kwargs={'id':1})
        self.assertEqual(url, '/dish_cloth/1/')
        