from django.shortcuts import render
from .models import *

# Create your views here.

def recipes(request):
    if request.method == 'POST':
        data=request.POST
        recipe_name = data.get('name')
        recipe_description=data.get('description')
        recipe_image=request.FILES['image']

        Recipe.objects.create(
            name=recipe_name,
            description=recipe_description,
            image=recipe_image
        )
    
    return render(request, 'recipe.html')
