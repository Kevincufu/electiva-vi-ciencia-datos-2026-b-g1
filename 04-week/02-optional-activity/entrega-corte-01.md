# Actividad Calificable — Corte 1: Diagnóstico de datos de un proceso

**Estudiante:** Kevin Andres Cuevas Fuentes
**Proceso seleccionado:** Gestión de inventario y logística en empresa de manufactura
**Periodo:** 2026-B — Semana 4

---

## 1. Problema y pregunta de datos

### Problema
> Existe acumulación de productos en bodega que rotan muy poco, ocupando espacio y generando costos de almacenamiento y riesgo de obsolescencia. No se identifican claramente cuáles son esos productos ni en qué temporadas se acumulan más.

### Pregunta de datos
> ¿Cuáles son los productos con menor rotación en inventario y en qué meses del año se acumulan más existencias, para reducir el sobrestock y optimizar el uso del espacio en bodega?

---

## 2. Inventario de datos — 6 fuentes clasificadas

| N° | Fuente / Campo | Contenido principal | Tipo de dato |
|---|---|---|---|
| 1 | Sistema de inventarios / ERP | Código de producto, cantidad almacenada, fechas de entrada y salida, ubicación en bodega | Estructurado |
| 2 | Sistema de facturación y ventas | Producto vendido, fecha, cantidad vendida, valor unitario | Estructurado |
| 3 | Catálogo maestro de artículos | Código, categoría, línea de producto, tiempo de vida útil, proveedor | Estructurado |
| 4 | Registros de recepción de mercancía | Albaranes, remisiones, fechas de entrega y observaciones | Semiestructurado |
| 5 | Fotografías e informes de bodega | Estado de estantes, condiciones de almacenamiento, anotaciones de personal | No estructurado |
| 6 | Comunicaciones con proveedores | Correos, plazos de entrega, acuerdos y reclamos | No estructurado |

---

## 3. Tipo de analítica y ¿Es caso de Big Data?

### Tipo de analítica aplicada
> **Descriptiva + Diagnóstica + Predictiva**

**¿Por qué?**
- **Descriptiva:** Se resume qué productos rotan menos y en qué meses se acumulan.
- **Diagnóstica:** Se investigan las causas: ¿baja demanda estacional?, ¿compras sobredimensionadas?
- **Predictiva:** Se estima cuánto se acumulará en los próximos meses si nada cambia.

### ¿Es un caso de Big Data?  SÍ — Justificación con las 5 V

| V | Análisis |
|---|---|
|  **Volumen** | Registros acumulados de meses o años; cuantos más datos, mayor precisión. |
|  **Velocidad** | Se actualiza continuamente; si llega tarde, las decisiones pierden valor. |
|  **Variedad** | Se combinan datos estructurados, semiestructurados y no estructurados. |
|  **Veracidad** | Existen duplicados, fechas inconsistentes y cantidades erróneas que deben limpiarse. |
|  **Valor** | Se traduce directamente en ahorro, menor desperdicio y mejor uso del espacio. |

> **Conclusión:** Aunque el volumen no sea masivo, la combinación de variedad, velocidad, necesidad de veracidad y valor generado lo convierte en un caso de Big Data según el marco de Laney.

---

## 4. Ciclo de vida del proyecto aplicado al caso
 PREGUNTA  →   OBTENER  →   LIMPIAR  →   ANALIZAR  →   VISUALIZAR  →   DECIDIR
 Definir qué     Extraer datos   Corregir      Identificar    Mostrar en       Ajustar compras,
 se quiere       de inventario   errores y     patrones de    gráficos y       existencias y
 saber           y ventas       duplicados    rotación       tableros         promocionar

### Explicación breve
1. **Pregunta:** Se define claramente qué se quiere responder.
2. **Obtener:** Se recolectan datos de los sistemas de inventario, ventas y productos.
3. **Limpiar:** Se corrigen registros duplicados, fechas inconsistentes y cantidades erróneas.
4. **Analizar:** Se identifican productos de baja rotación y temporadas de acumulación.
5. **Visualizar:** Se presentan resultados en tablas y gráficos comprensibles.
6. **Decidir:** Se toman acciones concretas sobre compras, existencias y promociones.

---

## 🇬🇧 Requirement in English — Problem & Data

> **The problem is that some products stay in the warehouse for a long time without being sold, taking up space and increasing storage costs. The question I want to answer is: which products rotate the least and in which months do they accumulate more stock?**
>
> **I need structured data from inventory systems and sales records, semi-structured delivery notes, and unstructured photos and reports from the warehouse. The analytics approach will be descriptive to understand what is happening, diagnostic to find the causes, and predictive to estimate future accumulation.**

---

##  Referencias bibliográficas

> - Laney, D. (2017). Las 5 dimensiones del Big Data: Volumen, Velocidad, Variedad, Veracidad y Valor.
> - Provost, F. y Fawcett, T. (2013). Data Science for Business. O'Reilly Media.
> - DNP (2020). Guía de buenas prácticas para el uso y aprovechamiento de datos.

---
