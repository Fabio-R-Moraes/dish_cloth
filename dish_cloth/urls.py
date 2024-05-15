from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dish_cloth-home'),
    path('dish_cloth/<int:id>/', views.dish_cloth, name='dish_cloth-cloth'),
]