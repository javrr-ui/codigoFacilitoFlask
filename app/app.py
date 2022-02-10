from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = {
        "title": "Index",
        "header": "Hola mundo"
    }
    return render_template('index.html', data=data)


app.run(debug=True)
