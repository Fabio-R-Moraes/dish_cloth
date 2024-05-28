from django.urls import reverse, resolve
from dish_cloth import views
from .test_base import ClothTestBase, Dish_Cloths

class ClothsViewsTest(ClothTestBase):
    def test_cloths_home_view_is_correct(self):
        view = resolve(reverse('dish_cloth:home'))
        self.assertIs(view.func, views.home)

    def test_cloths_dish_cloth_view_is_correct(self):
        view = resolve(reverse('dish_cloth:cloth', kwargs={'id':1}))
        self.assertIs(view.func, views.dish_cloth)

    def test_cloths_category_view_is_correct(self):
        view = resolve(reverse('dish_cloth:category', kwargs={'category_id':1}))
        self.assertIs(view.func, views.category)

    def test_cloths_home_view_return_code_200_ok(self):
        response = self.client.get(reverse('dish_cloth:home'))
        self.assertEqual(response.status_code, 200)

    def test_cloths_home_view_load_correct_template(self):
        response = self.client.get(reverse('dish_cloth:home'))
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_cloths_home_show_cloth_not_found(self):
        Dish_Cloths.objects.get(pk=1).delete()
        response = self.client.get(reverse('dish_cloth:home'))
        self.assertIn('<h1>Não há panos de prato para mostrar</h1>', 
                      response.content.decode('utf-8'))
    
    def test_cloths_category_view_return_404_if_not_found(self):
        response = self.client.get(reverse('dish_cloth:category', kwargs={'category_id':1000}))
        self.assertEqual(response.status_code, 404)

    def test_cloths_dish_cloth_view_return_404_if_not_found(self):
        response = self.client.get(reverse('dish_cloth:cloth', kwargs={'id':1000}))
        self.assertEqual(response.status_code, 404)

    def test_cloths_home_template_load_cloths(self):
        response = self.client.get(reverse('dish_cloth:home'))

        #Verificação por contexto
        #response_cloth = response.context['cloths']
        #self.assertEqual(response_cloth.first().title, 'Um novo pano de prato')

        #Verificação por conteúdo
        response_content = response.content.decode('utf-8')
        response_context_cloth = response.context['cloths']

        self.assertIn('Um novo pano de prato', response_content)
        self.assertIn('15 peças', response_content)
        self.assertIn('15,00 reais', response_content)

        #Foi gerado apenas um pano de prato
        self.assertEqual(len(response_context_cloth), 1)

    def test_cloths_category_template_load_cloths(self):
        title_needle = 'Este é um teste de categoria'

        #Precisa de um pano de prato para fazer o teste
        self.make_cloth(title=title_needle)
        response = self.client.get(reverse('dish_cloth:category', args=(2,)))

        #Verificação por conteúdo
        response_content = response.content.decode('utf-8')

        self.assertIn(title_needle, response_content)

    def test_cloths_cloth_template_load_the_correct_cloth(self):
        title_needle = 'Essa página carrega um único pano de prato'

        #Precisa de um pano de prato para fazer o teste
        self.make_cloth(title=title_needle)
        response = self.client.get(reverse('dish_cloth:cloth', kwargs={'id':1}))

        #Verificação por conteúdo
        response_content = response.content.decode('utf-8')

        self.assertIsNot(title_needle, response_content)

    def test_cloths_search_view_is_correct(self):
        view = resolve(reverse('dish_cloth:search'))
        self.assertIs(view.func, views.search)

    def test_cloths_search_load_correct_template(self):
        response = self.client.get(reverse('dish_cloth:search') + '?q=teste')
        self.assertTemplateUsed(response, 'pages/search.html')

    def test_cloths_search_no_term_get_404(self):
        url = reverse('dish_cloth:search')
        print(f'Resposta: {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
