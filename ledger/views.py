from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm, RecipeImageForm


def recipe_list(request):
    ctx = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'ledger/recipe_list.html', ctx)


@login_required(redirect_field_name=None)
def recipe(request, id):
    ctx = {'recipe': Recipe.objects.get(id=id)}
    return render(request, 'ledger/recipe.html', ctx)


def recipe_form(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save()
            return redirect('ledger:recipe', id=new_recipe.id)
    ctx = {"create_form": form}
    return render(request, 'ledger/recipe_form.html', ctx)


@login_required(redirect_field_name=None)
def image_form(request, id):
    form = RecipeImageForm()
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = Recipe.objects.get(id=id)
            image.save()
            return redirect('ledger:recipe', id=id)
    ctx = {'create_form': form, 'id': id}
    return render(request, 'ledger/image_form.html', ctx)
