from django.urls import reverse, resolve
from dish_cloth import views
from .test_base import ClothTestBase

class ClothsCategoryViewsTests(ClothTestBase):
    def test_cloths_category_view_is_correct(self):
        view = resolve(reverse('dish_cloth:category', kwargs={'category_id':1}))
        self.assertIs(view.func, views.category)

    def test_cloths_category_view_return_404_if_not_found(self):
        response = self.client.get(reverse('dish_cloth:category', kwargs={'category_id':1000}))
        self.assertEqual(response.status_code, 404)

    def test_cloths_category_template_load_cloths(self):
        title_needle = 'Este é um teste de categoria'

        #Precisa de um pano de prato para fazer o teste
        self.make_cloth(title=title_needle)
        response = self.client.get(reverse('dish_cloth:category', args=(2,)))

        #Verificação por conteúdo
        response_content = response.content.decode('utf-8')

        self.assertIn(title_needle, response_content)