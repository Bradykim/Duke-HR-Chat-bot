from flask import Flask, render_template, request, g
import time
app = Flask(__name__)


@app.route("/")
def my_template():
	return render_template("my_template.html")

f = open("log.txt", "w")
f.write(time.ctime(time.time) + "   ")
f.close()
