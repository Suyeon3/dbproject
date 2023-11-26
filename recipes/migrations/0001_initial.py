# Generated by Django 4.2.7 on 2023-11-26 05:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('ingredient', models.TextField()),
                ('amount', models.TextField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
                ('level', models.TextField(blank=True, null=True)),
                ('recipe', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.TextField()),
                ('userId', models.TextField(blank=True, null=True)),
                ('review', models.TextField()),
                ('rating', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.TextField()),
                ('t1', models.FloatField()),
                ('t2', models.FloatField()),
                ('t3', models.FloatField()),
                ('t4', models.FloatField()),
                ('t5', models.FloatField()),
                ('t6', models.FloatField()),
                ('t7', models.FloatField()),
                ('t8', models.FloatField()),
                ('t9', models.FloatField()),
                ('t10', models.FloatField()),
                ('t11', models.FloatField()),
                ('t12', models.FloatField()),
                ('t13', models.FloatField()),
                ('t14', models.FloatField()),
                ('t15', models.FloatField()),
                ('t16', models.FloatField()),
                ('t17', models.FloatField()),
                ('t18', models.FloatField()),
                ('t19', models.FloatField()),
                ('t20', models.FloatField()),
                ('t21', models.FloatField()),
                ('t22', models.FloatField()),
                ('t23', models.FloatField()),
                ('t24', models.FloatField()),
                ('t25', models.FloatField()),
                ('t26', models.FloatField()),
                ('t27', models.FloatField()),
                ('t28', models.FloatField()),
                ('t29', models.FloatField()),
                ('t30', models.FloatField()),
                ('t31', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kcal', models.FloatField()),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('sugars', models.FloatField()),
                ('sodium', models.FloatField()),
                ('cholesterol', models.FloatField()),
                ('saturated_fat', models.FloatField()),
                ('name', models.ForeignKey(db_column='name', on_delete=django.db.models.deletion.CASCADE, to='recipes.recipes')),
            ],
        ),
    ]
