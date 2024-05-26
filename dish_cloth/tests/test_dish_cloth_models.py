from .test_base import ClothTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized

class ClothsModelsTest(ClothTestBase):
    def setUp(self) -> None:
        self.cloth = self.make_cloth()
        return super().setUp()
    
    @parameterized.expand(
       [
            ('title', 65),
            ('description', 120),
            ('quantity_unit', 15),
            ('price_unit', 20)
        ]     
    )
    def test_fields_of_cloth_with_maxlength(self, value, max_length):
        setattr(self.cloth, value, 'A' * (max_length + 1))

        with self.assertRaises(ValidationError):
            self.cloth.full_clean()

    def test_cloth_is_published_True(self):
        self.cloth.is_published = False
        self.cloth.full_clean()
        self.cloth.save()
        self.assertFalse(self.cloth.is_published, msg='Nesse caso, o campo deve ser FALSE!!!')

    def test_cloth_string_representation(self):
        necessary = 'Pano de tomates'
        self.cloth.title = necessary
        self.cloth.full_clean()
        self.cloth.save()

        self.assertEqual(
            str(self.cloth), necessary, 
            msg=f'A representação de string do pano deve ser "{necessary}"'
            f' mas está chegando "{str(self.cloth)}"...'
        )
