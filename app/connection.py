import mysql.connector
from mysql.connector import Error
import sys 
def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password, 
            database=db_name
        )
        print("MySQL Database connection successful", file=sys.stderr)
    except Error as err:
        print(f"Error: '{err}'",  file=sys.stderr)
    return connection
#uses the connection.commit() method to make 
#sure that the commands detailed in our SQL queries are implemented.
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful",  file=sys.stderr)
    except Error as err:
        print(f"Error: '{err}'",  file=sys.stderr)

#execute query with data argument to poulate table 
def execute_query_insert(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query successful",  file=sys.stderr)
    except Error as err:
        print(f"Error: '{err}'",  file=sys.stderr)
    
#insert a new record into an existing table 
def insert_table(question, intent):
    statement = "INSERT INTO questions (question, intent) VALUES (%s, %s)"
    data = (question, intent) 
    connection = create_server_connection("db", "root", "HR", "sample_qna")
    execute_query_insert(connection, statement, data)

#reading data from database without making changes 
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'", file=sys.stderr)