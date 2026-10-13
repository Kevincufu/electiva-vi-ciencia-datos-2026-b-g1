"""Semana 10: mini-proyecto de datos. Datos simulados de una tostadora del Huila."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

CARPETA = Path(__file__).resolve().parent
df = pd.read_csv(CARPETA / "ventas_tostadora_huila.csv")
salida = CARPETA / "salidas"
salida.mkdir(exist_ok=True)

# EXTRAER Y LIMPIAR
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
df["producto"] = df["producto"].astype("string").str.strip().str.lower().replace({
    "café premium 500 g": "Café Premium 500 g",
    "café tradicional 500 g": "Café Tradicional 500 g",
    "café especial 250 g": "Café Especial 250 g"})
df["ciudad"] = df["ciudad"].astype("string").str.strip().str.title()
for c in ["cantidad", "precio_unitario", "total_venta"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")
df = df.dropna(subset=["fecha", "producto", "ciudad", "cantidad", "precio_unitario"])
df = df[(df["cantidad"] > 0) & (df["precio_unitario"] > 0)]
df["cantidad"] = df["cantidad"].astype(int)
df["total_venta"] = df["cantidad"] * df["precio_unitario"]
df = df.drop_duplicates(subset=["id_venta"]).sort_values("fecha")
df.to_csv(salida / "ventas_limpias.csv", index=False)

# ANÁLISIS 1: ingresos por producto
por_producto = df.groupby("producto", as_index=False)["total_venta"].sum().sort_values("total_venta", ascending=False)
por_producto.to_csv(salida / "analisis_por_producto.csv", index=False)
print("\\nANÁLISIS 1 — Ingresos por producto\\n", por_producto.to_string(index=False))

# ANÁLISIS 2: ingresos por ciudad durante 2026
por_ciudad = df[df["fecha"].dt.year == 2026].groupby("ciudad", as_index=False)["total_venta"].sum().sort_values("total_venta", ascending=False)
por_ciudad.to_csv(salida / "analisis_por_ciudad_2026.csv", index=False)
print("\\nANÁLISIS 2 — Ingresos por ciudad en 2026\\n", por_ciudad.to_string(index=False))

ax = por_producto.plot(kind="bar", x="producto", y="total_venta", legend=False, title="Ingresos por producto")
ax.set_xlabel("Producto"); ax.set_ylabel("Ingresos (COP)")
plt.xticks(rotation=15, ha="right"); plt.tight_layout()
plt.savefig(salida / "ingresos_por_producto.png", dpi=160)
print(f"\\nRegistros limpios: {len(df)}. Resultados guardados en {salida}")
