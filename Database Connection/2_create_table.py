import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="iris_database"
)


mycursor = mydb.cursor()

drop_table_if_exist = "DROP TABLE IF EXISTS iris_table"

query = """CREATE TABLE iris_table (  
         id INT AUTO_INCREMENT primary key NOT NULL,
         sepal_length float(20) NOT NULL,  
         sepal_width float(20) NOT NULL,  
         petal_length float(20) NOT NULL,
         petal_width float(20) NOT NULL, 
         variety VARCHAR(64) ) """
  

mycursor.execute(drop_table_if_exist)
mycursor.execute(query)

print("Iris table is created in the database")

mydb.commit()
mycursor.close()
mydb.close()
