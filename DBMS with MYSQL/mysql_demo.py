import mysql.connector

def read(connection):
    print("Inside read function")
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM employees LIMIT 5;")
        records = cursor.fetchall()
        print("Read successful. First few rows:")
        for record in records:
            print(f"id = {record[0]}, name = {record[1]}, position = {record[2]}, department = {record[3]}, salary = {record[4]}")
    except Exception as err:
        print("Error during read:", err)
    finally:
        cursor.close()
 
def insertRecord(connection):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO employees (name, position, department, salary) VALUES (%s, %s, %s, %s)"
        val = ("Hasti", "Marketing Head", "IT", 9300)
        cursor.execute(sql, val)
        connection.commit()
        print("Insert successful.")
    except Exception as err:
        print("Error during insert:", err)
    finally:
        cursor.close()
 
 
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test"
    )
    insertRecord(mydb)
    read(mydb)
except mysql.connector.Error as e:
    print("Connection error:", e)
finally:
    if mydb.is_connected():
        mydb.close()
        print("Connection closed.")