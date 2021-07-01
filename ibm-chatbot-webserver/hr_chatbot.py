from flask import Flask, render_template, request, jsonify
import time
app = Flask(__name__)


@app.route("/")
def my_template():
    ts = time.gmtime()
    data = request.json
    f = open("log.txt", "a")
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", ts) + "\t" + jsonify(data) + "\n")
    f.close()
    return render_template("my_template.html")


