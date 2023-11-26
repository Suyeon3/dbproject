from django.shortcuts import render, redirect, get_object_or_404
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px
from .models import Recipe, Ingredient, Nutrition

def home(request):
    return render(request, 'home.html')

def recipe_list(request):
    recipes = Nutrition.objects.all()
    result_recipes = recipes[:5]

    # Plotly 그래프 생성
    # 방사형 차트
    kcals = [recipe.kcal for recipe in result_recipes]
    kcal_list = []
    for kcal in kcals:
        kcal = ((kcal - min(kcals)) / (max(kcals) - min(kcals)))
        kcal_list.append(kcal)

    proteins = [recipe.protein for recipe in result_recipes]
    protein_list = []
    for protein in proteins:
        protein = ((protein - min(proteins)) / (max(proteins) - min(proteins)))
        protein_list.append(protein)

    fats = [recipe.fat for recipe in result_recipes]
    fat_list = []
    for fat in fats:
        fat = ((fat - min(fats)) / (max(fats) - min(fats)))
        fat_list.append(fat)

    carbos = [recipe.carbohydrates for recipe in result_recipes]
    carbo_list = []
    for carbo in carbos:
        carbo = ((carbo - min(carbos)) / (max(carbos) - min(carbos)))
        carbo_list.append(carbo)

    df = {
        'recipe_name': [str(recipe.name) for recipe in result_recipes],
        'kcal': kcal_list,
        'protein': protein_list,
        'fat': fat_list,
        'carbo': carbo_list,
    }

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
      r=df['kcal'],
      theta=df['recipe_name'],
      fill='toself',
      opacity=0.5,
      name='kcal'
    ))

    fig.add_trace(go.Scatterpolar(
      r=df['protein'],
      theta=df['recipe_name'],
      fill='toself',
      opacity=0.5,
      name='protein'
    ))

    fig.add_trace(go.Scatterpolar(
      r=df['fat'],
      theta=df['recipe_name'],
      fill='toself',
      opacity=0.5,
      name='fat'
    ))

    fig.add_trace(go.Scatterpolar(
      r=df['carbo'],
      theta=df['recipe_name'],
      fill='toself',
      opacity=0.5,
      name='carbohydrates'
    ))
    
    fig.update_layout(
        title='영양소 비교',
        polar=dict(
        radialaxis=dict(
        visible=True,
        )),
        showlegend=True
    )
    plot_div_radar = plot(fig, output_type='div', include_plotlyjs=False)


    return render(request, 'recipe_list.html', 
                  {'recipes': recipes, 
                   'plot_div_radar': plot_div_radar
                   })
    

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