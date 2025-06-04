import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)
#trigger the query
mycursor = mydb.cursor()
sql = "INSERT INTO student (name, division,degree) VALUES (%s,%s,%s)"
val =("Neil", "A","CS")
mycursor.execute(sql,val)
 
#handle the result
mydb.commit()
mycursor.close()
mydb.close()