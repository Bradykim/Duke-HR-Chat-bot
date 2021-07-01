from flask import Flask, render_template, request, jsonify
import time
app = Flask(__name__)


@app.route("/")
def foo():
    data = request.json
    return jsonify(data)
def my_template():
    ts = time.gmtime()
    data = request.args
    f = open("log.txt", "a")
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", ts) + "\t" + str(foo) + "\n")
    f.close()
    return render_template("my_template.html")


