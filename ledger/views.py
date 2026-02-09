from django.shortcuts import render

from django.http import HttpResponse

def recipeList():
    return HttpResponse("recipe list")

def recipe1():
    return HttpResponse("recipe 1")

def recipe2():
    return HttpResponse("recipe 2") 
