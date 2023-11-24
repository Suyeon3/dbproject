import pandas as pd
import sqlite3

# Read csv file.
df = pd.read_csv("./data/nutrition.csv", encoding="cp949")

# Connect to (create) database.
database = "db.sqlite3"
conn = sqlite3.connect(database)
# dtype={
#     "id": "IntegerField",
#     "name": "TextField",
#     "kcal": "FloatField",
#     "protein": "FloatField",
#     "fat": "FloatField",
#     "carbohydrates": "FloatField",
#     "sugars": "FloatField",
#     "sodium": "FloatField",
#     "cholesterol": "FloatField",
#     "saturated_fat": "FloatField",
# }
# df.to_sql(name='receipes_nutrition', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")
df.to_sql(name='recipes_nutrition', con=conn, if_exists='replace', index=False)
conn.close()