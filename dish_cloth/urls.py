from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('dish_cloth/<int:id>/', views.dish_cloth),
]