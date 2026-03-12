from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe


def recipe_list(request):
    ctx = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'ledger/recipe_list.html', ctx)


@login_required(redirect_field_name=None)
def recipe(request, id):
    ctx = {'recipe': Recipe.objects.get(id=id)}
    return render(request, 'ledger/recipe.html', ctx)
