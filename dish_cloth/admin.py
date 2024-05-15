from django.contrib import admin

from .models import Category, Dish_Cloths, Buies, items_buy

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Dish_Cloths)
class Dish_ClothsAdmin(admin.ModelAdmin):
    ...
