from unittest import TestCase
from paginacao import make_pagination_range

class PaginationTest(TestCase):
    def test_make_a_range_pagination_return_a_range_pagination(self):
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            quantity=4,
            actual_page=1,
        )['pagination']

        self.assertEqual([1,2,3,4], pagination)

    def test_make_the_middle_range_stay_correct(self):
        #Página atual=10, quantidade de páginas = 4, página do meio = 2
        #Aqui o range DEVE mudar
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            quantity=4,
            actual_page=10,
        )['pagination']

        self.assertEqual([9,10,11,12], pagination)

        #Página atual=12
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            quantity=4,
            actual_page=12,
        )['pagination']

        self.assertEqual([11,12,13,14], pagination)

    def test_make_pagination_range_static_if_last_page_in_the_range(self): # noqa E501
        #Página atual=18, quantidade de páginas = 4, página do meio = 2
        #Aqui o range DEVE mudar
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            quantity=4,
            actual_page=18,
        )['pagination']

        self.assertEqual([17,18,19,20], pagination)   

        #Página atual=19
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            quantity=4,
            actual_page=19,
        )['pagination']

        self.assertEqual([17,18,19,20], pagination)    

        #Página atual=20
        pagination = make_pagination_range(
            page_range=list(range(1,21)),
            quantity=4,
            actual_page=20,
        )['pagination']

        self.assertEqual([17,18,19,20], pagination)
