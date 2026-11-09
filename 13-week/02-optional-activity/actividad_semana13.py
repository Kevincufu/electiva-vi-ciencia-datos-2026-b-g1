"""
Actividad Semana 13 - Ciencia de Datos
Diseño de un dashboard

Proceso elegido: ventas.
Se definen 3 KPIs y se crea un boceto de tablero con filtros.

Requisitos:
    pip install pandas matplotlib pillow

Ejecución:
    python actividad_semana13.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE / "datos_dashboard.csv", parse_dates=["fecha"])

# KPI 1: Ingresos totales
ingresos_totales = df["ingresos"].sum()

# KPI 2: Unidades vendidas
unidades_totales = df["unidades_vendidas"].sum()

# KPI 3: Cumplimiento de meta
cumplimiento_meta = unidades_totales / df["meta_unidades"].sum() * 100

print("KPIs")
print(f"Ingresos totales: ${ingresos_totales:,.0f}")
print(f"Unidades vendidas: {unidades_totales:,.0f}")
print(f"Cumplimiento de meta: {cumplimiento_meta:.1f}%")

# Evolución mensual de ingresos
mensual = df.groupby("fecha", as_index=False)["ingresos"].sum()
plt.figure(figsize=(9, 4))
plt.plot(mensual["fecha"], mensual["ingresos"], marker="o")
plt.title("Evolución mensual de ingresos")
plt.xlabel("Mes")
plt.ylabel("Ingresos")
plt.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(BASE / "chart_ingresos_mensuales.png", dpi=180)
plt.show()

# Comparación por producto
producto = df.groupby("producto", as_index=False)["unidades_vendidas"].sum()
plt.figure(figsize=(7, 4))
plt.bar(producto["producto"], producto["unidades_vendidas"])
plt.title("Unidades por producto")
plt.xlabel("Producto")
plt.ylabel("Unidades")
plt.ylim(bottom=0)
plt.tight_layout()
plt.savefig(BASE / "chart_unidades_producto.png", dpi=180)
plt.show()

# Comparación por planta
planta = df.groupby("planta", as_index=False)["unidades_vendidas"].sum()
plt.figure(figsize=(7, 4))
plt.bar(planta["planta"], planta["unidades_vendidas"])
plt.title("Unidades por planta")
plt.xlabel("Planta")
plt.ylabel("Unidades")
plt.ylim(bottom=0)
plt.tight_layout()
plt.savefig(BASE / "chart_unidades_planta.png", dpi=180)
plt.show()

# Filtros propuestos para el dashboard:
# - Fecha
# - Planta
# - Producto

# Bibliografía:
# Few, S. (2013). Information Dashboard Design (2nd ed.). Analytics Press.
# Microsoft. (2026). Power BI documentation. https://learn.microsoft.com/power-bi/
# Matplotlib development team. (2026). Matplotlib documentation. https://matplotlib.org/stable/
