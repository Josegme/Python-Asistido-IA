from flask import Flask, render_template, request

app = Flask(__name__)

class ReglaTresCalculator:
    """Clase responsable de la lógica de cálculo de regla de tres"""

    @staticmethod
    def calcular(a: float, b: float, c: float) -> float:
        if a == 0:
            raise ValueError("El primer número (A) no puede ser cero.")
        return (b * c) / a


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            c = float(request.form["c"])
            resultado = ReglaTresCalculator.calcular(a, b, c)
        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Entrada inválida. Por favor, ingrese números válidos."

    return render_template("index.html", resultado=resultado, error=error)


if __name__ == "__main__":
    app.run(debug=True)
