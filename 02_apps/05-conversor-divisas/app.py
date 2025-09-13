from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "TU_API_KEY_AQUI"  # ⚠️ reemplaza con tu clave de exchangeratesapi.io
BASE_URL = "https://api.exchangeratesapi.io/v1/convert"

# Lista de monedas disponibles
CURRENCIES = ["EUR", "USD", "CNY", "JPY"]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    amount = None
    from_currency = None
    to_currency = None

    if request.method == "POST":
        try:
            # Obtener datos del formulario
            amount = float(request.form["amount"].replace(",", "."))
            from_currency = request.form["from_currency"]
            to_currency = request.form["to_currency"]

            # Parámetros de la API
            params = {
                "access_key": API_KEY,
                "from": from_currency,
                "to": to_currency,
                "amount": amount
            }

            # Hacer la petición
            response = requests.get(BASE_URL, params=params)
            data = response.json()
            print(data)  # 👈 para debug en consola

            # Verificar si la conversión fue exitosa
            if data.get("success"):
                result = f"{amount} {from_currency} = {data['result']:.2f} {to_currency}"
            else:
                error_info = data.get("error", {}).get("info", "Intenta de nuevo.")
                result = f"Error en la conversión: {error_info}"
        except Exception as e:
            result = f"Error: {str(e)}. Ingrese un monto válido."

    return render_template("index.html",
                           currencies=CURRENCIES,
                           result=result,
                           amount=amount,
                           from_currency=from_currency,
                           to_currency=to_currency)

if __name__ == "__main__":
    app.run(debug=True)
