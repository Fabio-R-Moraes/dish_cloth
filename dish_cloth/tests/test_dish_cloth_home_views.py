from django.urls import reverse, resolve
from dish_cloth import views
from .test_base import ClothTestBase, Dish_Cloths
from unittest.mock import patch

class ClothsHomeViewsTests(ClothTestBase):
    #Testes para a página home
    def test_cloths_home_view_is_correct(self):
        view = resolve(reverse('dish_cloth:home'))
        self.assertIs(view.func, views.home)

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

    @patch('dish_cloth.views.PER_PAGE', new=4)
    def test_cloths_home_is_paginated(self):
        #Precisam de vários panos de prato para fazer o teste
        for i in range(18):
            kwargs = {'author_data': {
                'username': f'Fabio_{i}'},
                'slug': f'Teste de paginacao_{i}'}
            self.make_cloth(**kwargs)

        response = self.client.get(reverse('dish_cloth:home'))
        response_context_cloth = response.context['cloths']
        pagination = response_context_cloth.paginator

        self.assertEqual(pagination.num_pages, 5)
        self.assertEqual(len(pagination.get_page(1)), 4)
        self.assertEqual(len(pagination.get_page(2)), 4)
