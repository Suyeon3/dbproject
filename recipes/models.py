from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()

    def __str__(self):
        return self.title

class Nutrition(models.Model):
    name = models.TextField()
    kcal = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrates = models.FloatField()
    sugars = models.FloatField()
    sodium = models.FloatField()
    cholesterol = models.FloatField()
    saturated_fat = models.FloatField()

    def __str__(self):
        return self.name