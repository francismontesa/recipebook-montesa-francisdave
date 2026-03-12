from django.urls import path

from .views import recipe_list, recipe, recipe_form, image_form

urlpatterns = [
    path('recipes/list', recipe_list, name='list'),
    path('recipe/<int:id>', recipe, name='recipe'),
    path('recipe/add', recipe_form, name='add'),
    path('recipe/<int:id>/add_image', image_form, name='add-image')
]

app_name = 'ledger'
