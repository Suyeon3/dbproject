from django.contrib import admin
from .models import Recipes, Nutrition, Review, Trend


admin.site.register(Recipes)
admin.site.register(Nutrition)
admin.site.register(Review)
admin.site.register(Trend)