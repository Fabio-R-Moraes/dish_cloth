from django.test import TestCase
from dish_cloth.models import User, Dish_Cloths, Category
import random

class ClothTestBase(TestCase):
    def setUp(self) -> None:
        self.make_cloth()
        return super().setUp()
    
    def make_category(self, name='pontes'):
        return Category.objects.create(name=name)
    
    def make_author(
            self,
            first_name='Mariana',
            last_name='Moreira de Moraes',
            username='Maricotinha',
            password='fbrql823',
            email='marianamoreira@email.com'           
    ):
        number = random.randint(0,100)
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username+str(number),
            password=password,
            email=email
        )
    
    def make_cloth(
            self,
            category_data = None,
            author_data = None,
            title = 'Um novo pano de prato',
            slug = 'um-novo-pano-de-prato',
            description = 'Uma amostra para um novo pano de prato',
            is_published=True,
            quantity = 15,
            quantity_unit = 'peças',
            price = 15,
            price_unit = 'reais',
            cloth_image = 'dish_cloth/cloth_images/16/05/2024/Pinturas_165.jpg'
    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Dish_Cloths.objects.create(
            category = self.make_category(**category_data, name='riachos'),
            author = self.make_author(**author_data),
            title = title,
            slug = slug,
            description = description,
            is_published=is_published,
            quantity = quantity,
            quantity_unit = quantity_unit,
            price = price,
            price_unit = price_unit,
            cloth_image = cloth_image
        )