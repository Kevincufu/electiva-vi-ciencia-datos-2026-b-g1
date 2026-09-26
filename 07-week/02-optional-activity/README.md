# Solución Guía de Actividad Práctica - Semana 07
**Asignatura:** Ciencia de Datos  
**Unidad 2:** Modelamiento, transformación y conexión de datos  

---

## 1. Conjunto de Datos de Ejemplo (Datasets)

Para esta actividad se utilizan dos tablas relacionadas mediante la clave `cliente_id`:

* **`clientes`**: Contiene la información general del cliente (`cliente_id`, `nombre`, `ciudad`).
* **`ventas`**: Contiene el historial de transacciones (`venta_id`, `cliente_id`, `producto`, `monto`).

---

## 2. Consultas en SQL y Explicación

### Consulta 1: Filtro Condicional (`WHERE`)
```sql
SELECT * 
FROM clientes 
WHERE ciudad = 'Neiva';```
SELECT 
    c.nombre AS cliente, 
    v.producto, 
    v.monto
FROM ventas v
INNER JOIN clientes c ON v.cliente_id = c.cliente_id;```
SELECT 
    c.ciudad, 
    SUM(v.monto) AS total_ventas
FROM ventas v
INNER JOIN clientes c ON v.cliente_id = c.cliente_id
GROUP BY c.ciudad;```
import pandas as pd

# 1. Definición de DataFrames
df_clientes = pd.DataFrame([
    {"cliente_id": 1, "nombre": "Carlos", "ciudad": "Neiva"},
    {"cliente_id": 2, "nombre": "Ana", "ciudad": "Pitalito"},
    {"cliente_id": 3, "nombre": "Luisa", "ciudad": "Neiva"},
    {"cliente_id": 4, "nombre": "Pedro", "ciudad": "Pitalito"}
])

df_ventas = pd.DataFrame([
    {"venta_id": 101, "cliente_id": 1, "producto": "Laptop", "monto": 1200.0},
    {"venta_id": 102, "cliente_id": 2, "producto": "Mouse", "monto": 25.0},
    {"venta_id": 103, "cliente_id": 1, "producto": "Teclado", "monto": 45.0},
    {"venta_id": 104, "cliente_id": 3, "producto": "Monitor", "monto": 300.0},
    {"venta_id": 105, "cliente_id": 4, "producto": "Audífonos", "monto": 80.0}
])

# 2. Combinación de tablas (Equivalente al INNER JOIN)
df_merged = pd.merge(df_ventas, df_clientes, on="cliente_id")

# 3. Agrupamiento y Suma (Equivalente al GROUP BY)
df_groupby = (
    df_merged.groupby("ciudad")["monto"]
    .sum()
    .reset_index()
    .rename(columns={"monto": "total_ventas"})
)

# Mostrar el resultado final
print("=== RESULTADO DEL GROUP BY EN PANDAS ===")
print(df_groupby)
4. Referencias Bibliográficas
McKinney, W. (2022). Python for Data Analysis: Data Wrangling with Pandas, NumPy, and Jupyter (3rd ed.). O'Reilly Media.

Pandas Development Team. (2026). pandas.DataFrame.groupby — pandas documentation.

Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020). Database System Concepts (7th ed.). McGraw-Hill Education.
