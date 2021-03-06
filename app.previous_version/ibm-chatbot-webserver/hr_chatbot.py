from flask import Flask, render_template, request, jsonify
import time
import json
app = Flask(__name__)


@app.route("/")
def my_template():
    ts = time.gmtime()
    data = request.args
    str_data = json.dumps(data)
    f = open("log.txt", "a")
    print(data)
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", ts) + " " + request.remote_addr + " \t" + str_data + "\n")
    f.close()
    return render_template("my_template.html")
