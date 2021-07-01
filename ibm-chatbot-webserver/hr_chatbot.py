from flask import Flask, render_template, request, g
import time

app = Flask(__name__)

@app.route("/")
def my_template():
	return render_template("my_template.html")

@app.before_request
def before_request():
    return str(time.time())

f = open("log.txt", "w")
f.write(str(before_request()) + "   ")
f.close()
