from django.shortcuts import render

from django.http import HttpResponse

import ast

def recipeList(request):
    contextFile = open('ledger/contexts/Recipe List Context.txt', 'r')
    contextContent = contextFile.read()
    contextFile.close()
    ctx = ast.literal_eval(contextContent)
    return render(request, 'ledger/recipe_list.html', ctx)

def recipe1(request):
    return HttpResponse("recipe 1")

def recipe2(request):
    return HttpResponse("recipe 2") 
