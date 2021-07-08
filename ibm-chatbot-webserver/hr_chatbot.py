from flask import Flask, render_template, request, jsonify
import time
import json
app = Flask(__name__)


@app.route("/")
def my_template():
    ts = time.gmtime()
    data = request.get_json(force=False)
    #str_data = json.dumps(request)
    f = open("log.txt", "a")
    print(data)
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", ts) + "\t" + json.dumps(data) + "\n")
    f.close()
    return render_template("my_template.html")
