from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe


def recipe_list(request):
    ctx = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'ledger/recipe_list.html', ctx)


@login_required
def recipe(request, id):
    ctx = {'ingredients': Recipe.objects.get(id=id)}
    return render(request, 'ledger/recipe.html', ctx)
