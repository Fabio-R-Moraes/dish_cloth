from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.dish_cloth.fabrica import make_cloth
from .models import Dish_Cloths, Category
from django.http import Http404
from django.db.models import Q
from utils.paginacao import make_pagination
import os

PER_PAGE = os.environ.get('CLOTHS_PER_PAGE')

def home(request):
    dishes_cloths = Dish_Cloths.objects.filter(is_published=True).order_by('-id')
    pagina_objeto, page_range = make_pagination(request, dishes_cloths, PER_PAGE)
    return render(request, 'pages/home.html', context={
        'cloths': pagina_objeto,
        'page_range': page_range,
        'title': 'Home |'
    })

def dish_cloth(request, id):
    dish_cloth = get_object_or_404(Dish_Cloths, pk=id, is_published=True)
    return render(request, 'pages/dish_cloth_view.html', context={
        'cloth': dish_cloth,
    })

def category(request, category_id):
    dishes_cloths = get_list_or_404(Dish_Cloths.objects.filter(
        category__id=category_id,
        is_published=True
        ).order_by('-id'))
    
    pagina_objeto, page_range = make_pagination(request, dishes_cloths, PER_PAGE)

    return render(request, 'pages/category.html', context={
        'cloths': pagina_objeto,
        'page_range': page_range,
        'title': f'{dishes_cloths[0].category.name} - Categoria |'
    })

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()
    
    cloths = Dish_Cloths.objects.filter(
        Q(
            Q(title__icontains=search_term) | 
            Q(description__icontains=search_term),
        ),
        is_published=True,
    ).order_by('-title')

    pagina_objeto, page_range = make_pagination(request, cloths, PER_PAGE)

    return render(request, 'pages/search.html', {
        'page_title': f'Pesquisando por "{search_term}" |',
        'cloths': pagina_objeto,
        'page_range': page_range,
        'aditional_url_query': f'&q={search_term}',
    })
