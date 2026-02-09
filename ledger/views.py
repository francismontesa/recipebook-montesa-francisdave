from django.shortcuts import render

from django.http import HttpResponse

import ast

def readContextFile(fileDir):
    contextFile = open(fileDir, 'r')
    contextContent = contextFile.read()
    contextFile.close()
    return ast.literal_eval(contextContent)

def recipeList(request):
    ctx = readContextFile('ledger/contexts/Recipe List Context.txt')
    return render(request, 'ledger/recipe_list.html', ctx)

def recipe1(request):
    ctx = readContextFile('ledger/contexts/Recipe 1.txt')
    return render(request, 'ledger/recipe.html', ctx)

def recipe2(request):
    ctx = readContextFile('ledger/contexts/Recipe 2.txt')
    return render(request, 'ledger/recipe.html', ctx)
