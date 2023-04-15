from flask import Flask, render_template
import json
from flask import request

app = Flask(__name__)

file = open("/Users/anacarolinaalves/Desktop/MESTRADO/2/PLN/TPC5-copia/dicionario_translate_resultado_TPC5.json")
db = json.load(file)

@app.route("/")
def home():
    return render_template("home.html", title="Welcome")

@app.route("/terms")
def terms():
    return render_template("terms.html", designations=db.keys())

@app.route("/term/<t>")
def term(t):
    return render_template("term.html", designation = t , value = db.get(t, "None"))


@app.route("/about")
def about():
    return render_template('About.html')

app.run(host="localhost", port=3000, debug=True)
