from flask import Flask, render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
    print("antes de la petición")

@app.after_request
def after_request(response):
    print("Después de la petición")
    return response

@app.route("/")
def index():
    data = {
        "title": "Index",
        "header": "Hola mundo"
    }
    print("Ejecutando...")
    return render_template('index.html', data=data)

@app.route("/contacto")
def contacto():
    data = {
        "title": "Contacto",
        "header": "Seccion de contacto"
    }
    return render_template("contacto.html",data=data)

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"hola {nombre}"

@app.route("/suma/<int:valor1>/<int:valor2>")
def suma(valor1, valor2):
    return f"{valor1 + valor2}"

@app.route("/lenguajes")
def lenguajes():
    data = {
        "lenguajes": ["Java", "Python", "JavaScript", "Go"]
    }
    return render_template("lenguajes.html", data=data)

@app.route("/datos")
def hola():
    print(request.args)
    valor1 = request.args.get("valor1")
    return f"Estos son los datos: {valor1}"
    
app.run(debug=True)
