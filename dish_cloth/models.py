from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Dish_Cloths(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField()
    description = models.CharField(max_length=120)
    is_published = models.BooleanField(default=False)
    quantity = models.IntegerField()
    quantity_unit = models.CharField(max_length=15)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    price_unit = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    cloth_image = models.ImageField(upload_to='dish_cloth/cloth_images/%d/%m/%Y', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

class Buies(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    date_of_buy = models.DateTimeField(auto_now_add=True)
    note_number = models.IntegerField()

class items_buy(models.Model):
    note_id = models.ForeignKey(
        Buies, on_delete=models.SET_NULL, null=True
    )
    item_id = models.ForeignKey(
        Dish_Cloths, on_delete=models.SET_NULL, null=True
    )
    
