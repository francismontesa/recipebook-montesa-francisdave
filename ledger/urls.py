from django.urls import path

from .views import recipe_list, recipe

urlpatterns = [
    path('recipes/list', recipe_list, name='list'),
    path('recipe/<int:id>', recipe, name='recipe'),
]

app_name = 'ledger'
