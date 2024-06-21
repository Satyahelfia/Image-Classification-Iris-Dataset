import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="iris_database"
)


mycursor = mydb.cursor()

query = """INSERT INTO iris_table (sepal_length ,sepal_width ,petal_length, petal_width, variety) 
          VALUES (%s, %s, %s, %s, %s)"""
  

# Load data into the database
data = pd.read_csv('iris.csv')

# print("dataset load --> ",data)

for index, row in data.iterrows():
    mycursor.execute(query, (row['sepal_length'], row['sepal_width'],row['petal_length'],row['petal_width'] , row['variety']))


mydb.commit()
mycursor.close()
mydb.close()