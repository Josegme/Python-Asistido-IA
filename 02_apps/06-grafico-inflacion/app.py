from flask import Flask, Response, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Dataset simplificado de inflación media anual (%) en Argentina (ejemplo simulado)
data = {
    "Año": list(range(2004, 2024)),
    "Inflacion": [
        13.4, 10.9, 12.3, 15.1, 20.8, 25.6, 22.5, 23.7, 25.6, 28.3,
        40.9, 27.0, 41.0, 25.7, 34.3, 53.5, 36.1, 48.4, 50.9, 95.0
    ]
}

df = pd.DataFrame(data)


@app.route("/")
def home():
    return "<h2>Servicio de Gráfico - Inflación en Argentina</h2><p>Visita <a href='/grafico'>/grafico</a> para ver el gráfico.</p>"


@app.route("/grafico")
def grafico():
    # Crear la figura
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Año"], df["Inflacion"], marker="o", linestyle="-", color="blue", label="Inflación %")

    ax.set_title("Inflación media en Argentina (2004 - 2023)")
    ax.set_xlabel("Año")
    ax.set_ylabel("Inflación (%)")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)

    # Guardar gráfico en memoria como PNG
    img = io.BytesIO()
    plt.savefig(img, format="png")
    plt.close(fig)
    img.seek(0)

    # Convertir a base64 para incrustar en HTML
    img_base64 = base64.b64encode(img.getvalue()).decode("utf-8")

    return render_template("index.html", grafico=img_base64)


if __name__ == "__main__":
    app.run(debug=True)
