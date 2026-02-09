from django.shortcuts import render

from django.http import HttpResponse

def recipeList(request):
    return HttpResponse("recipe list")

def recipe1(request):
    return HttpResponse("recipe 1")

def recipe2(request):
    return HttpResponse("recipe 2") 
