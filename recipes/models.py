from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Recipes(models.Model):
    name = models.TextField(primary_key=True)
    ingredient = models.TextField()
    amount = models.TextField(
        blank=True,
        null=True
    )
    time = models.TextField(
        blank=True,
        null=True
    )
    level = models.TextField(
        blank=True,
        null=True
    )
    recipe = models.TextField()

    def __str__(self):
        return self.name


class Nutrition(models.Model):
    # foodName = models.TextField()
    name = models.ForeignKey(Recipes, on_delete=models.CASCADE, db_column="name")
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
    

class Review(models.Model):
    foodName = models.TextField()
    userId = models.TextField(
        blank=True,
        null=True
    )
    review = models.TextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.foodName
    

class Trend(models.Model):
    foodName = models.TextField()
    t1 = models.FloatField()
    t2 = models.FloatField()
    t3 = models.FloatField()
    t4 = models.FloatField()
    t5 = models.FloatField()
    t6 = models.FloatField()
    t7 = models.FloatField()
    t8 = models.FloatField()
    t9 = models.FloatField()
    t10 = models.FloatField()
    t11 = models.FloatField()
    t12 = models.FloatField()
    t13 = models.FloatField()
    t14 = models.FloatField()
    t15 = models.FloatField()
    t16 = models.FloatField()
    t17 = models.FloatField()
    t18 = models.FloatField()
    t19 = models.FloatField()
    t20 = models.FloatField()
    t21 = models.FloatField()
    t22 = models.FloatField()
    t23 = models.FloatField()
    t24 = models.FloatField()
    t25 = models.FloatField()
    t26 = models.FloatField()
    t27 = models.FloatField()
    t28 = models.FloatField()
    t29 = models.FloatField()
    t30 = models.FloatField()
    t31 = models.FloatField()

    def __str__(self):
        return self.name