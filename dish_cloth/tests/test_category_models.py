from .test_base import ClothTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized

class CategoryModelsTest(ClothTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(name='Tomates verdes')
        return super().setUp()
    
    @parameterized.expand([('name',65)])
    def test_category_with_maxlength_greater_than_65(self, value, max_length):
        setattr(self.category,value, 'B' * 70)

        with self.assertRaises(ValidationError):
            self.category.full_clean()

    def test_cagegory_string_representation(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )