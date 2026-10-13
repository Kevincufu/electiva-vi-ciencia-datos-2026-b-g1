"""Semana 11: serie temporal mensual y media móvil de tres meses."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

CARPETA = Path(__file__).resolve().parent
ARCHIVO = CARPETA.parent / "10-week" / "ventas_tostadora_huila.csv"
salida = CARPETA / "salidas"
salida.mkdir(exist_ok=True)

df = pd.read_csv(ARCHIVO)
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
df["total_venta"] = df["cantidad"] * df["precio_unitario"]

# Fecha como índice; resample agrega los ingresos por mes.
mensual = df.set_index("fecha")["total_venta"].resample("MS").sum().to_frame(name="ventas_mensuales")
mensual["media_movil_3_meses"] = mensual["ventas_mensuales"].rolling(window=3, min_periods=1).mean()
mensual.to_csv(salida / "serie_temporal_mensual.csv", index_label="fecha")

ax = mensual.plot(figsize=(10, 5), marker="o", title="Ventas mensuales y media móvil de 3 meses")
ax.set_xlabel("Mes"); ax.set_ylabel("Ingresos (COP)"); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig(salida / "serie_temporal_media_movil.png", dpi=160)
print(mensual.to_string())
print("\\nInterpretación: compare la tendencia general y las fluctuaciones mensuales.")
print(f"Resultados guardados en {salida}")
