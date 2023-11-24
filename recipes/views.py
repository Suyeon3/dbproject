from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Ingredient, Nutrition

def home(request):
    return render(request, 'home.html')

def recipe_list(request):
    # recipes = Recipe.objects.order_by('title')
    recipes = Nutrition.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})
    # return render(request, 'recipe_list.html', {'recipes': recipes})
    # if request.method == 'POST':
    #     ingredients = request.POST.get('ingredients')
    #     # 이후 레시피 리스트를 가져오는 모델 함수를 호출하여 리스트를 구현하세요.
    #     # recipes = get_recipes(ingredients)
    #     recipes = []  # 임시로 레시피 리스트를 빈 리스트로 설정

    #     return render(request, 'recipe_list.html', {'recipes': recipes, 'ingredients': ingredients})
    # else:
    #     return redirect('home')

def recipe_detail(request, recipe_id):
    # 이후 레시피 상세 정보를 가져오는 모델 함수를 호출하여 정보를 구현하세요.
    # recipe = get_recipe(recipe_id)
    # recipe = {}  # 임시로 레시피 정보를 빈 딕셔너리로 설정
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


# def add_example_data(request):
#     # Create example ingredients
#     ingredient1 = Ingredient.objects.create(name='돼지고기')
#     ingredient2 = Ingredient.objects.create(name='김치')
#     ingredient3 = Ingredient.objects.create(name='양파')

#     # Create an example recipe
#     recipe = Recipe.objects.create(
#         title='돼지김치두루치기',
#         instructions='1. 김치 썰기. \n\n 2. 삼겹살 굽기 \n\n 3. 같이 볶기',
#     )
#     recipe.ingredients.add(ingredient1, ingredient2, ingredient3)

#     return render(request, 'home.html', {'message': 'Example data added successfully!'})