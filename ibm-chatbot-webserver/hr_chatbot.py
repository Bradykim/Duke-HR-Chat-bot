from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def my_template():
	return render_template("my_template.html")

@app.before_request
def start_timer():
    g.start = time.time()

f = open("log.txt", "w")
f.write(start_timer() + "   ")
f.close()
