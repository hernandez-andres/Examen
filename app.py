# archivo: app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Usuarios registrados para Ejercicio 2
users = {
    "juan": "admin",
    "pepe": "user"
}


# Ruta inicial con los botones Ejercicio 1 y Ejercicio 2
@app.route("/")
def index():
    return render_template("index.html")


# Ruta del Ejercicio 1 - Cálculo de compras
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad_tarros = int(request.form["cantidad_tarros"])

        precio_por_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_por_tarro

        # Cálculo del descuento según la edad
        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0  # Sin descuento para menores de 18 años

        total_con_descuento = total_sin_descuento * (1 - descuento)

        # Renderizar los resultados
        return render_template("resultado1.html", nombre=nombre, total_sin_descuento=total_sin_descuento,
                               total_con_descuento=total_con_descuento)

    return render_template("ejercicio1.html")


# Ruta del Ejercicio 2 - Login de usuarios
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Validar el usuario y contraseña
        if username in users and users[username] == password:
            if username == "juan":
                mensaje = f"Bienvenido administrador {username}"
            elif username == "pepe":
                mensaje = f"Bienvenido usuario {username}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template("resultado2.html", mensaje=mensaje)

    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run(debug=True)

