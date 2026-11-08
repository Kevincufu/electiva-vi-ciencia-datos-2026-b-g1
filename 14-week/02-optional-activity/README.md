# c3-activity — Corte 3: Análisis temporal y visualización

Entrega individual preparada para la actividad **Corte 3 — Análisis temporal y visualización**.

## Contenido

- `c3_activity.ipynb`: cuaderno principal con todo el desarrollo.
- `c3_activity.py`: versión ejecutable en Python.
- `ventas_diarias.csv`: serie temporal utilizada.
- `01_tendencia_media_movil.png`: visualización de evolución y media móvil.
- `02_estacionalidad_mensual.png`: visualización de estacionalidad mensual.
- `consulta_optimizada.sql`: consulta original, versión optimizada y explicación.
- `medidas_dax.txt`: dos medidas DAX relacionadas con los indicadores.
- `Informe_C3_Actividad.pdf`: informe final listo para entregar.
- `requirements.txt`: dependencias mínimas.

## Cómo ejecutar

```bash
pip install -r requirements.txt
python c3_activity.py
```

También puedes abrir `c3_activity.ipynb` en Jupyter Notebook, JupyterLab o VS Code y ejecutar todas las celdas en orden.

## Metodología

La serie contiene ventas diarias entre enero de 2024 y diciembre de 2025.  
En Python se convierte la fecha a índice temporal y se agregan los datos por mes con `resample("MS").sum()`.  
Luego se calcula una media móvil de 3 meses mediante `rolling(window=3).mean()` para suavizar fluctuaciones de corto plazo.  
La estacionalidad se estudia comparando el promedio de ventas mensuales para cada mes del año.  
Finalmente, se construyen dos visualizaciones con títulos orientados a la conclusión y ejes etiquetados de forma clara.

## Interpretación

El promedio de los últimos tres meses es aproximadamente **33.7%** superior al promedio de los primeros tres meses, lo que indica una tendencia general creciente.  
La media móvil de tres meses confirma esa dirección al reducir el ruido de los valores mensuales.  
En la comparación estacional, **May** presenta el mayor promedio mensual y **Ene** el menor dentro de esta serie.  
La gráfica de barras parte de cero para evitar exagerar diferencias visuales.

## SQL optimizado

La consulta optimizada reemplaza `YEAR(fecha) = 2025` por un filtro de rango:

```sql
WHERE fecha >= DATE '2025-01-01'
  AND fecha <  DATE '2026-01-01'
```

Este cambio evita aplicar una función sobre la columna filtrada y facilita que un índice sobre `fecha` sea aprovechado por el motor de base de datos.

## DAX

Se incluyen dos medidas adicionales:

1. **Ventas Totales**: medida base reutilizable.
2. **Promedio Móvil 3M**: suaviza la variación de corto plazo y ayuda a leer la tendencia.

## Findings

The monthly sales series shows an overall upward trend across the two-year period.  
The three-month moving average makes this trend easier to interpret because it reduces short-term fluctuations.  
The first chart compares monthly sales with the moving average and shows that the smoothed series follows the same general direction with less noise.  
The second chart compares average sales by calendar month and reveals a recurring seasonal pattern, with May showing the highest average level in this dataset.  
Because the bar chart starts at zero, the magnitude of the differences between months is represented honestly.  
The optimized SQL filter is more index-friendly than applying a year function directly to the date column, while the DAX moving-average measure provides a clearer business indicator for trend monitoring.

## Nota de reproducibilidad

Los datos del CSV fueron generados de forma reproducible con una semilla fija para fines académicos. El análisis no depende de servicios externos.


## Bibliografía

- McKinney, W. (2022). Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter (3rd ed.). O'Reilly Media.
- pandas development team. (2026). Resampling. pandas 3.1.1 documentation. https://pandas.pydata.org/docs/reference/resampling.html
- pandas development team. (2026). pandas.DataFrame.rolling. pandas documentation. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html
- Matplotlib development team. (2026). Matplotlib documentation. https://matplotlib.org/stable/
- PostgreSQL Global Development Group. (2026). Date/Time Functions and Operators: date_trunc. PostgreSQL 16 Documentation. https://www.postgresql.org/docs/16/functions-datetime.html
- PostgreSQL Global Development Group. (2026). Indexes. PostgreSQL Documentation. https://www.postgresql.org/docs/current/indexes.html
- Microsoft. (2026). Time intelligence functions (DAX). Microsoft Learn. https://learn.microsoft.com/dax/time-intelligence-functions-dax
- Microsoft. (2026). DATESINPERIOD function (DAX). Microsoft Learn. https://learn.microsoft.com/dax/datesinperiod-function-dax
- Microsoft. (2026). AVERAGEX function (DAX). Microsoft Learn. https://learn.microsoft.com/dax/averagex-function-dax
- GitHub Docs. (2026). Git basics and working with repositories. https://docs.github.com/
