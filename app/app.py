from flask import Flask, request, Response, render_template
from typing import List, Dict
import mysql.connector
from mysql.connector import Error
import json
from connection import * 
import time


app = Flask(__name__)


@app.route('/')
def index():
    #Timestamp (Emily)
    ts = time.gmtime()
    data = request.args
    str_data = json.dumps(data)
    f = open("/persistent_flask_logs/log.txt", "a")
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", ts) + " " + request.remote_addr + " \t" + str_data + "\n")
    print("after writing", file=sys.stderr)
    f.close()

    return render_template("my_template.html")
    
#webhook     
@app.route('/webhook', methods=['POST', 'GET'])
def respond():
    
    #Example JSON object for IBM bot
    example_dict = {"message" : "Hello, world!"}
    return json.dumps(example_dict)

    # Timestamp (Jacqueline & Mitchell)
    """time = datetime.datetime.now()
    #print(time, file=sys.stderr)"""

    details = request.json
    question = details["question"]
    intent = details["intent"]
    print(question, file=sys.stderr)
    print(intent, file=sys.stderr)

    #insert data as a row in questions table 
    insert_table(question, intent) 


    #read data from table 
    #q1 = """
    #SELECT *
    #FROM questions;
    #"""
    """
    connection = create_server_connection("db", "root", "registrar", "sample_qna")
    results = read_query(connection, q1)
    for result in results:
        print(result, file=sys.stderr)
    """
    
    #Update a record 
    #Ex: changing intent for a specific question 
    #update = """
    #UPDATE questions 
    #SET intent = 'form requests' 
    #WHERE question = 'How do I request a trancript?';
    #"""
    ##WHERE uniquely identifies which record/records to update 
    #connection = create_server_connection("db", "root", "registrar", "sample_qna")
    #execute_query(connection, update)

    #Delete a record 
    #delete_question = """
    #DELETE FROM questions 
    #WHERE question = 'a question';
    #"""
    #connection = create_server_connection("db", "root", "registrar", "sample_qna")
    #execute_query(connection, delete_question)
    
    #return Response(status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0') #, ssl_context=('/home/vcm/registrar-chatbot/server.crt', '/home/vcm/registrar-chatbot/server.key'))
