from flask import Flask

app = Flask(__name__)


@app.route("/")
def hola_mundo():
    return "Hola mundo"


app.run(debug=True)
