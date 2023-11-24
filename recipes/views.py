from django.shortcuts import render, redirect, get_object_or_404
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px
from .models import Recipe, Ingredient, Nutrition

def home(request):
    return render(request, 'home.html')

def recipe_list(request):
    recipes = Nutrition.objects.all()
    result_recipes = Nutrition.objects.all()[:5]

    # Plotly 그래프 생성
    # 전체 영양소
    '''
    x_values = ['Kcal', 'Protein', 'Fat', 'Carbohydrates']
    traces=[]
    for recipe in result_recipes:
        y_values = [recipe.kcal, recipe.protein, recipe.fat, recipe.carbohydrates]
        trace = go.Scatter(x=x_values, y=y_values, mode='markers+lines', name=str(recipe.name))
        traces.append(trace)

    layout = go.Layout(title='영양성분 비교', showlegend=True)
    fig = go.Figure(data=traces, layout=layout)

    # Plotly 그래프를 HTML로 변환
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)

    # Kcal
    kcal_x = [str(recipe.name) for recipe in result_recipes]
    kcal_y = [recipe.kcal for recipe in result_recipes]
    trace_kcal = go.Scatter(x=kcal_x, y=kcal_y, mode='markers+lines', name='칼로리')

    layout_kcal = go.Layout(title='칼로리 비교', showlegend=True)
    fig_kcal = go.Figure(data=trace_kcal, layout=layout_kcal)

    plot_div_kcal = plot(fig_kcal, output_type='div', include_plotlyjs=False)

    # Protein
    protein_x = [str(recipe.name) for recipe in result_recipes]
    protein_y = [recipe.protein for recipe in result_recipes]
    trace_protein = go.Scatter(x=protein_x, y=protein_y, mode='markers+lines', name='단백질')

    layout_protein = go.Layout(title='단백질 비교', showlegend=True)
    fig_protein = go.Figure(data=trace_protein, layout=layout_protein)

    plot_div_protein = plot(fig_protein, output_type='div', include_plotlyjs=False)

    # fat
    fat_x = [str(recipe.name) for recipe in result_recipes]
    fat_y = [recipe.fat for recipe in result_recipes]
    trace_fat = go.Scatter(x=fat_x, y=fat_y, mode='markers+lines', name='지방')

    layout_fat = go.Layout(title='지방 비교', showlegend=True)
    fig_fat = go.Figure(data=trace_fat, layout=layout_fat)

    plot_div_fat = plot(fig_fat, output_type='div', include_plotlyjs=False)

    # carbo
    carbo_x = [str(recipe.name) for recipe in result_recipes]
    carbo_y = [recipe.carbohydrates for recipe in result_recipes]
    trace_carbo = go.Scatter(x=carbo_x, y=carbo_y, mode='markers+lines', name='탄수화물')

    layout_carbo = go.Layout(title='탄수화물 비교', showlegend=True)
    fig_carbo = go.Figure(data=trace_carbo, layout=layout_carbo)

    plot_div_carbo = plot(fig_carbo, output_type='div', include_plotlyjs=False)
'''
    # 방사형 차트
    df = {
        'recipe_name': [str(recipe.name) for recipe in result_recipes],
        'kcal': [recipe.kcal for recipe in result_recipes],
        'protein': [recipe.protein for recipe in result_recipes],
        'fat': [recipe.fat for recipe in result_recipes],
        'carbo': [recipe.carbohydrates for recipe in result_recipes],
    }

    fig_radar_kcal = px.line_polar(df, r="kcal", theta='recipe_name', line_close=True)
    fig_radar_kcal.update_traces(fill='toself')
    fig_radar_kcal.update_layout(
    title='칼로리 비교',
    polar=dict(
        radialaxis=dict(
            visible=True
        )
    ),
    showlegend=True
    )
    plot_div_radar_kcal = plot(fig_radar_kcal, output_type='div', include_plotlyjs=False)

    fig_radar_protein = px.line_polar(df, r="protein", theta='recipe_name', line_close=True)
    fig_radar_protein.update_traces(fill='toself')
    fig_radar_protein.update_layout(
    title='단백질 비교',
    polar=dict(
        radialaxis=dict(
            visible=True
        )
    ),
    showlegend=True
    )
    plot_div_radar_protein = plot(fig_radar_protein, output_type='div', include_plotlyjs=False)

    fig_radar_fat = px.line_polar(df, r="fat", theta='recipe_name', line_close=True)
    fig_radar_fat.update_traces(fill='toself')
    fig_radar_fat.update_layout(
    title='지방 비교',
    polar=dict(
        radialaxis=dict(
            visible=True
        )
    ),
    showlegend=True
    )
    plot_div_radar_fat = plot(fig_radar_fat, output_type='div', include_plotlyjs=False)

    fig_radar_carbo = px.line_polar(df, r="carbo", theta='recipe_name', line_close=True)
    fig_radar_carbo.update_traces(fill='toself')
    fig_radar_carbo.update_layout(
    title='탄수화물 비교',
    polar=dict(
        radialaxis=dict(
            visible=True
        )
    ),
    showlegend=True
    )
    plot_div_radar_carbo = plot(fig_radar_carbo, output_type='div', include_plotlyjs=False)

    return render(request, 'recipe_list.html', 
                  {'recipes': recipes, 
                #    'plot_div': plot_div, 
                #    'plot_div_kcal': plot_div_kcal, 
                #    'plot_div_protein': plot_div_protein, 
                #    'plot_div_fat': plot_div_fat, 
                #    'plot_div_carbo': plot_div_carbo,
                   'plot_div_radar_kcal': plot_div_radar_kcal,
                   'plot_div_radar_protein': plot_div_radar_protein,
                   'plot_div_radar_fat': plot_div_radar_fat,
                   'plot_div_radar_carbo': plot_div_radar_carbo
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