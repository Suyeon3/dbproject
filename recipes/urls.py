from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe-list/', views.recipe_list, name='recipe_list'),
    path('recipe-detail/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    # path('add-example-data/', views.add_example_data, name='add_example_data'),
]