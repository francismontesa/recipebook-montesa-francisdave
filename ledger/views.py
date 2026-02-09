from django.shortcuts import render

import ast


def recipe_list(request):
    ctx = get_context('ledger/contexts/Recipe List Context.txt')
    return render(request, 'ledger/recipe_list.html', ctx)


def recipe1(request):
    ctx = get_context('ledger/contexts/Recipe 1.txt')
    return render(request, 'ledger/recipe.html', ctx)


def recipe2(request):
    ctx = get_context('ledger/contexts/Recipe 2.txt')
    return render(request, 'ledger/recipe.html', ctx)


def get_context(file_dir):
    context_file = open(file_dir, 'r')
    context_content = context_file.read()
    context_file.close()
    return ast.literal_eval(context_content)
