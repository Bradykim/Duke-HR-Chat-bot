from flask import Flask, render_template, request, jsonify
import time
app = Flask(__name__)


@app.route("/")
def get_request_data():
    return (
        request.args
        or request.form
        or request.get_json(force=True, silent=True)
        or request.data
    )
def my_template():
    ts = time.gmtime()
    data = request.get_data()
    f = open("log.txt", "a")
    f.write(time.strftime("%Y-%m-%d %H:%M:%S", ts) + "\t" + str(get_request_data) + "\n")
    f.close()
    return render_template("my_template.html")


