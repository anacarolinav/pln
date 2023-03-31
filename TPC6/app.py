from flask import Flask
from flask import  render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('Home.html')

@app.route("/about")
def about():
    return render_template('About.html')

@app.route("/animals")
def animais():
    return render_template('Animals.html')

@app.route("/services")
def servicos():
    return render_template('Services.html')

app.run(host="localhost", port=4002, debug=True)