# Actividad — Semana 2: Clasificación de datos y las V del Big Data

**Estudiante:** Kevin Andres Cuevas Fuentes
**Programa:** Ingeniería Industrial
**Asignatura:** Ciencia de Datos
**Institución:** CORHUILA — Periodo 2026-B

---

## 1. Fuentes de datos y clasificación por estructura

Se listan **6 fuentes** del proyecto de optimización de inventario, clasificadas según su estructura:

| # | Fuente de datos | Contenido principal | Tipo |
|---|---|---|---|
| 1 | Sistema de inventarios / ERP | Código producto, cantidades, fechas, ubicación | **Estructurado** |
| 2 | Sistema de facturación y ventas | Producto, fecha, cantidad, valor unitario, cliente | **Estructurado** |
| 3 | Catálogo maestro de artículos | Código, categoría, línea, vida útil, proveedor | **Estructurado** |
| 4 | Registros de recepción de mercancía | Albaranes, remisiones, firmas, observaciones manuscritas | **Semiestructurado** |
| 5 | Fotos y videos de estado de bodega | Imágenes de estantes, productos, condiciones de almacenamiento | **No estructurado** |
| 6 | Correos y comunicaciones con proveedores | Plazos, reclamos, acuerdos de entrega | **No estructurado** |

###  Justificación
- **Estructurados:** Datos organizados en tablas con formato definido (filas y columnas), compatibles con bases de datos relacionales. Son los más fáciles de procesar y analizar.
- **Semiestructurados:** Tienen cierta organización pero no se ajustan estrictamente a un esquema fijo; pueden contener etiquetas, campos variables o formatos mixtos.
- **No estructurados:** Sin formato ni organización predefinida; requieren procesamiento especializado (visión artificial, procesamiento de lenguaje) para extraer valor.

> Según el marco de referencia del **Departamento Nacional de Planeación (2020)**, esta distinción es fundamental porque determina las herramientas, costos y técnicas necesarias para cada tipo de dato.

---

## 2.  Las 5 V del Big Data — ¿Cuáles son críticas y por qué?

| V | Nivel de relevancia | ¿Por qué es crítica? |
|---|---|---|
|  **Volumen** | ⭐⭐⭐⭐⭐ | Se acumulan registros históricos de meses o años. A mayor cantidad de datos, mayor precisión al identificar patrones de rotación por temporada. |
|  **Velocidad** | ⭐⭐⭐⭐ | Los registros de inventario y ventas se actualizan constantemente. Si la información llega tarde o se procesa lento, las decisiones se toman sobre datos obsoletos. |
| **Variedad** | ⭐⭐⭐ | Se combinan datos estructurados con registros semiestructurados y no estructurados. Integrarlos es clave para tener una visión completa del problema. |
|  **Veracidad** | ⭐⭐⭐⭐⭐ | Datos duplicados, fechas erróneas o cantidades mal registradas pueden hacer que el análisis diga lo contrario de la realidad. Sin fiabilidad no hay valor. |
|  **Valor** | ⭐⭐⭐⭐⭐ | Es la V más importante: todo análisis debe traducirse en ahorro, menor pérdida y mejor decisión. Si no genera valor medible, el proyecto no tiene justificación. |

###  Síntesis
> **Las 3 más críticas:** **Veracidad + Valor + Volumen**. Sin datos fiables (veracidad) el análisis falla; sin volumen suficiente no se ven patrones; y si no se genera valor económico o operativo, el proyecto no cumple su propósito empresarial.

> Referencia: **Laney, D. (2001–2017).** *Las 3 V que se convirtieron en 5: Volumen, Velocidad, Variedad, Veracidad y Valor*. Marco estándar adoptado por DNP y entidades públicas en Colombia.

---

## 3.  Reto de veracidad (calidad de los datos)

### Problema identificado
> **Registros duplicados, fechas inconsistentes y cantidades mal registradas:** un mismo movimiento de inventario puede aparecer dos veces; la fecha de entrada puede ser posterior a la de salida; o cantidades registradas no coincidir con el contejo físico real. Esto genera falsos reportes de rotación y acumulación.

### ¿Cómo lo detectaría?
- **Duplicados:** Contar registros únicos por combinación de código de producto + fecha + tipo de movimiento. Si hay repeticiones exactas → hay duplicidad.
- **Inconsistencias de fecha:** Filtrar registros donde `fecha_entrada > fecha_salida` → son imposibles y señalan error de carga.
- **Descuadre de cantidades:** Comparar el saldo calculado desde el sistema con el inventario físico real. Si la diferencia supera un margen aceptable → hay datos incorrectos.
- **Valores extremos:** Detectar cantidades imposibles (ej: 0 o negativas, o cifras 10 veces mayores al promedio habitual) → probablemente errores de digitación.

### Justificación
> Como señalan **Redman (2008)** y el **DNP (2020)**, la mala calidad de los datos cuesta millones a las empresas. Detectar estos problemas antes de analizar es obligatorio: "basar decisiones en datos malos es peor que no tener datos".

---

##  Referencias bibliográficas

> - **Laney, D. (2017).** *3D Data Management: Controlling Data Volume, Velocity, and Variety*. Actualización a 5 V: Veracidad y Valor.
> - **Departamento Nacional de Planeación (2020).** *Guía de buenas prácticas para el uso y aprovechamiento de datos*. Alcaldía y Presidencia de Colombia.
> - **Redman, T. C. (2008).** *Datos malos le cuestan a Estados Unidos 600 mil millones de dólares al año*. MIT Sloan Management Review.

---
