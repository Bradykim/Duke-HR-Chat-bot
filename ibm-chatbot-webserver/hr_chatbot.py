from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def my_template():
	return render_template("my_template.html")
