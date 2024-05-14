from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def dish_cloth(request, id):
    return render(request, 'pages/dish_cloth_view.html', 
                  context={'nome': 'Rachel Moreira de Moraes'})
