import pandas as pd
import sqlite3

# Read csv file.
df = pd.read_csv("./data/nutrition.csv", encoding="cp949")
df_trend = pd.read_csv("./data/food_trends.csv", encoding="cp949")
df_recipe = pd.read_csv("./data/recipe.csv", encoding="utf-8")
df_review = pd.read_csv("./data/recipe_review.csv", encoding="utf-8")

# Connect to (create) database.
database = "db.sqlite3"
conn = sqlite3.connect(database)

df.to_sql(name='recipes_nutrition', con=conn, if_exists='replace', index=False)
df_trend.to_sql(name='recipes_trend', con=conn, if_exists='replace', index=False)
<<<<<<< HEAD
df_recipe.to_sql(name='recipes_recipe', con=conn, if_exists='replace', index=False)
=======
df_recipe.to_sql(name='recipes_recipes', con=conn, if_exists='replace', index=False)
>>>>>>> 581cd5588194ada83054a6763c43a71b43e453e1
df_review.to_sql(name='recipes_review', con=conn, if_exists='replace', index=False)
conn.close()