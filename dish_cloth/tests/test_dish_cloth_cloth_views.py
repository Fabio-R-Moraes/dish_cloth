from django.urls import reverse, resolve
from dish_cloth import views
from .test_base import ClothTestBase

class ClothsClothViewsTests(ClothTestBase):
    def test_cloths_dish_cloth_view_is_correct(self):
        view = resolve(reverse('dish_cloth:cloth', kwargs={'id':1}))
        self.assertIs(view.func, views.dish_cloth)

    def test_cloths_cloth_template_load_the_correct_cloth(self):
        title_needle = 'Essa página carrega um único pano de prato'

        #Precisa de um pano de prato para fazer o teste
        self.make_cloth(title=title_needle)
        response = self.client.get(reverse('dish_cloth:cloth', kwargs={'id':1}))

        #Verificação por conteúdo
        response_content = response.content.decode('utf-8')

        self.assertIsNot(title_needle, response_content)

    def test_cloths_dish_cloth_view_return_404_if_not_found(self):
        response = self.client.get(reverse('dish_cloth:cloth', kwargs={'id':1000}))
        self.assertEqual(response.status_code, 404)