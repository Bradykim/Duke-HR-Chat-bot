from flask import Flask, render_template, request, g
import time
app = Flask(__name__)


@app.route("/")
def my_template():
	return render_template("my_template.html")

ts = time.gmtime()

f = open("log.txt", "a")
f.write(time.strftime("%Y-%m-%d %H:%M:%S", ts) + "   " + request + "\n")
f.close()
