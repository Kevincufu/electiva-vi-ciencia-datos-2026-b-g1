"""
Actividad Semana 12 - Ciencia de Datos
Rediseño de un gráfico

Requisitos:
    pip install pandas matplotlib

Ejecución:
    python actividad_semana12.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE / "datos_produccion.csv")

# GRÁFICO ANTES:
# Tiene un eje Y truncado y demasiados colores sin una función clara.
plt.figure(figsize=(9, 5.5))
plt.bar(
    df["mes"],
    df["produccion"],
    color=["red", "orange", "purple", "green", "blue", "pink"]
)
plt.ylim(900, 1060)
plt.title("Producción")
plt.xlabel("Mes")
plt.ylabel("Unidades")
plt.tight_layout()
plt.savefig(BASE / "01_antes_grafico_mal_diseniado.png", dpi=180)
plt.show()

# GRÁFICO DESPUÉS:
# La escala inicia en cero y el color se utiliza solo para destacar el mayor valor.
colores = ["#B8B8B8"] * len(df)
colores[-1] = "#1F77B4"

plt.figure(figsize=(9, 5.5))
plt.bar(df["mes"], df["produccion"], color=colores)
plt.ylim(0, 1100)
plt.title("La producción aumenta y junio registra el valor más alto")
plt.xlabel("Mes")
plt.ylabel("Producción (unidades)")
plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(BASE / "02_despues_grafico_redisenado.png", dpi=180)
plt.show()

# Bibliografía:
# Matplotlib development team. (2026). Matplotlib documentation.
# https://matplotlib.org/stable/
# Cairo, A. (2016). The Truthful Art: Data, Charts, and Maps for Communication.
# New Riders.
