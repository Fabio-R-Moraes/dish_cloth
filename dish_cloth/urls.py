from django.urls import path
from dish_cloth import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'dish_cloth'

urlpatterns = [
    path('', views.home, name='home'),
    path('dish_cloth/category/<int:category_id>/', views.category, name='category'),
    path('dish_cloth/<int:id>/', views.dish_cloth, name='cloth'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)