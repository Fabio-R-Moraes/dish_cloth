from django.shortcuts import render
from utils.dish_cloth.fabrica import make_cloth

def home(request):
    return render(request, 'pages/home.html', context={
        'cloths': [make_cloth() for _ in range(20)]
    })

def dish_cloth(request, id):
    return render(request, 'pages/dish_cloth_view.html', 
                  context={'cloth': make_cloth()})
