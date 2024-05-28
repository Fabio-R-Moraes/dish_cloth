from django.urls import reverse, resolve
from dish_cloth import views
from .test_base import ClothTestBase

class ClothsSearchViewsTest(ClothTestBase):
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

    def test_cloths_search_term_on_the_page_and_scape(self):
        url = reverse('dish_cloth:search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Pesquisando por &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
            )
        
    def test_cloths_search_find_cloth_by_title(self):
        oneTitle = 'Este é o primeiro título'
        twoTitle = 'Este é osegundo título'

        oneCloth = self.make_cloth(
            slug='one',
            title=oneTitle,
            author_data={'username': 'oneUser'}
        )

        twoCloth = self.make_cloth(
            slug='two',
            title=twoTitle,
            author_data={'username': 'twoUser'}
        )

        wanted_url = reverse('dish_cloth:search')
        one_response = self.client.get(f'{wanted_url}?q={oneTitle}')
        two_response = self.client.get(f'{wanted_url}?q={twoTitle}')
        both_response = self.client.get(f'{wanted_url}?q=Este')

        self.assertIn(oneCloth, one_response.context['cloths'])
        self.assertNotIn(twoCloth, one_response.context['cloths'])

        self.assertIn(twoCloth, two_response.context['cloths'])
        self.assertNotIn(oneCloth, two_response.context['cloths'])

        self.assertIn(oneCloth, both_response.context['cloths'])
        self.assertIn(twoCloth, both_response.context['cloths'])
