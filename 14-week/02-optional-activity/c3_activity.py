"""
Corte 3 - Análisis temporal y visualización
Actividad c3-activity

Requisitos:
    pip install pandas numpy matplotlib

Ejecutar:
    python c3_activity.py
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
CSV = BASE / "ventas_diarias.csv"

# 1. Cargar serie temporal
df = pd.read_csv(CSV, parse_dates=["fecha"])
df = df.sort_values("fecha").set_index("fecha")

# 2. Agregación por periodo (resample) y media móvil
mensual = df["ventas"].resample("MS").sum().to_frame("ventas_mensuales")
mensual["media_movil_3m"] = mensual["ventas_mensuales"].rolling(window=3).mean()

# 3. Tendencia
primeros_3 = mensual["ventas_mensuales"].iloc[:3].mean()
ultimos_3 = mensual["ventas_mensuales"].iloc[-3:].mean()
crecimiento = (ultimos_3 / primeros_3 - 1) * 100

# 4. Estacionalidad por mes del año
mensual["mes"] = mensual.index.month
estacionalidad = mensual.groupby("mes")["ventas_mensuales"].mean()

print("=== RESUMEN ===")
print(mensual.round(2))
print(f"\nCrecimiento aproximado entre los primeros y últimos 3 meses: {crecimiento:.1f}%")
print(f"Mes con mayor promedio: {estacionalidad.idxmax()}")
print(f"Mes con menor promedio: {estacionalidad.idxmin()}")

# 5. Visualización 1: evolución + media móvil
plt.figure(figsize=(11, 6))
plt.plot(mensual.index, mensual["ventas_mensuales"], marker="o", label="Ventas mensuales")
plt.plot(mensual.index, mensual["media_movil_3m"], linewidth=2.6, label="Media móvil 3 meses")
plt.title("Las ventas muestran una tendencia creciente suavizada por la media móvil")
plt.xlabel("Fecha")
plt.ylabel("Ventas agregadas")
plt.legend()
plt.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(BASE / "01_tendencia_media_movil.png", dpi=180)
plt.show()

# 6. Visualización 2: comparación estacional
nombres = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
plt.figure(figsize=(10, 5.5))
plt.bar(nombres, estacionalidad.reindex(range(1,13)).values)
plt.title("La comparación mensual permite identificar la estacionalidad de las ventas")
plt.xlabel("Mes del año")
plt.ylabel("Ventas mensuales promedio")
plt.ylim(bottom=0)  # Eje honesto para comparación con barras
plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(BASE / "02_estacionalidad_mensual.png", dpi=180)
plt.show()


# ================================================
# BIBLIOGRAFÍA / REFERENCIAS TÉCNICAS (APA 7)
# ================================================
# McKinney, W. (2022). Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter (3rd ed.). O'Reilly Media.
# pandas development team. (2026). Resampling. pandas 3.1.1 documentation. https://pandas.pydata.org/docs/reference/resampling.html
# pandas development team. (2026). pandas.DataFrame.rolling. pandas documentation. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html
# Matplotlib development team. (2026). Matplotlib documentation. https://matplotlib.org/stable/
