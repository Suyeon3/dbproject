from django.shortcuts import render, redirect, get_object_or_404
from plotly.offline import plot
import plotly.graph_objs as go
from .models import Recipe, Ingredient, Nutrition

def home(request):
    return render(request, 'home.html')

def recipe_list(request):
    recipes = Nutrition.objects.all()
    result_recipes = Nutrition.objects.all()[:5]

    # plotly 그래프 생성
    x_values = ['Kcal', 'Protein', 'Fat', 'Carbohydrates']
    traces=[]
    for recipe in result_recipes:
        y_values = [recipe.kcal, recipe.protein, recipe.fat, recipe.carbohydrates]
        trace = go.Scatter(x=x_values, y=y_values, mode='markers+lines', name= str(recipe.name))
        traces.append(trace)

    # Plotly 그래프 생성
    layout = go.Layout(title='영양성분 비교', showlegend=True)
    fig = go.Figure(data=traces, layout=layout)

    # Plotly 그래프를 HTML로 변환
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)

    return render(request, 'recipe_list.html', {'recipes': recipes, 'plot_div':plot_div})
    

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