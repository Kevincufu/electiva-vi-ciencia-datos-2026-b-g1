# Actividad — Semana 3: Diseño de una arquitectura de datos

**Estudiante:** Kevin Andres Cuevas Fuentes
**Programa:** Ingeniería Industrial
**Asignatura:** Ciencia de Datos
**Institución:** Corporación Universitaria del Huila — CORHUILA
**Periodo:** 2026-B

---

## 1. Arquitectura del flujo de datos
  FUENTES DE DATOS                INGESTA              ALMACENAMIENTO        PROCESAMIENTO        ANÁLISIS / BI
┌───────────────────────┐   ┌──────────────────────┐   ┌──────────────────┐   ┌─────────────────┐   ┌──────────────────┐
│  Sistema de ERP       │   │                      │   │                  │   │  Limpieza y    │   │  Tableros de     │
│  Sistema de Ventas    │──▶│  Extracción y carga  │──▶│  DATA WAREHOUSE  │──▶│  Transformación │──▶│  Control y       │
│  Catálogo de Productos│   │  por lotes (Batch)   │   │  (Almacén de     │   │  Cálculo de     │   │  Reportes e       │
│  Registros de Bodega  │   │                      │   │   Datos)         │   │  Rotación       │   │  Indicadores      │
│  Documentos e Imágenes│   │                      │   │                  │   │  Agrupación     │   │  (Power BI)       │
└───────────────────────┘   └──────────────────────┘   └──────────────────┘   └─────────────────┘   └──────────────────┘

### Descripción del flujo
1. **Fuentes:** Sistema de inventarios/ERP, sistema de facturación, catálogo de productos, registros de recepción y documentos o imágenes de bodega.
2. **Ingesta:** Se recolectan los datos de forma periódica mediante cargas programadas, no en tiempo real.
3. **Almacenamiento:** Se integran y guardan en un repositorio estructurado optimizado para consulta y análisis.
4. **Procesamiento:** Se limpian, validan y transforman los datos: se calculan indicadores de rotación, se detectan inconsistencias y se agrupan por periodo y producto.
5. **Análisis e Inteligencia de Negocio:** Se construyen reportes y tableros para visualizar productos de baja rotación, temporadas de acumulación y recomendaciones de gestión.

---

## 2. Decisiones de arquitectura

### ¿Data Warehouse o Data Lake? → **Data Warehouse**

> Se elige **Almacén de Datos (Data Warehouse)** porque los datos provienen principalmente de sistemas operativos estructurados, con formato conocido y definido. El objetivo es generar reportes y análisis confiables para la toma de decisiones, por lo que se requiere información ya limpia, validada y organizada por temas y tiempos. Un Data Warehouse garantiza consistencia, fiabilidad y facilidad de uso para herramientas de inteligencia de negocio.

> **Justificación:** Según Inmon (2005), padre del concepto, un almacén de datos es "una colección de datos orientados al tema, integrados, no volátiles y variables en el tiempo, que sirven de apoyo a la toma de decisiones". Al tener datos estructurados y un propósito analítico definido, el Data Warehouse es la opción más adecuada. El Data Lake sería más conveniente si se quisiera guardar todo en bruto sin estructura previa, especialmente gran volumen de datos no estructurados por explorar; en este caso, no es necesario.

### ¿Procesamiento Batch o Streaming? → **Batch (por lotes)**

> Se elige **procesamiento por lotes** porque los datos de inventario y ventas no cambian cada segundo; basta con recolectarlos y procesarlos de forma programada (diaria, semanal o mensual). No se requiere respuesta en tiempo real ni inmediata; las decisiones sobre compras y existencias se toman de forma periódica.

> **Justificación:** El procesamiento por lotes es ideal cuando los datos cambian en intervalos amplios y no se necesita latencia mínima. En cambio, el procesamiento en flujo continuo (streaming) se reserva para casos donde los datos deben procesarse en el instante en que se producen, como transacciones financieras o monitoreo de sensores. En este proyecto, el procesamiento por lotes ofrece mayor simplicidad, menor costo y suficiente oportunidad para la toma de decisiones.

---

## 3. Herramientas recomendadas por etapa

| Etapa | Herramienta candidata | ¿Por qué se elige? |
|---|---|---|
| **Ingesta** | MySQL / Excel programado o Python | Los datos se encuentran en sistemas empresariales estándar; se pueden extraer y consolidar con consultas o scripts sencillos, sin necesidad de herramientas complejas. |
| **Almacenamiento** | SQL Server o PostgreSQL | Sistemas de gestión de bases de datos relacionales, compatibles con el modelo estructurado de inventario y ventas. Permiten organizar la información en tablas relacionadas y garantizar integridad. |
| **Procesamiento** | Python (Pandas) o SQL | Permiten limpiar, filtrar, calcular indicadores de rotación, detectar duplicados y transformar los datos antes de visualizarlos. Lenguajes accesibles, potentes y muy utilizados en el medio empresarial. |
| **Análisis y BI** | Power BI o Tableau | Permiten crear tableros visuales, gráficos por periodo y producto, alertas sobre existencias y compartir reportes con el equipo directivo. Se integran directamente con bases de datos SQL y archivos procesados. |

---

## Referencias bibliográficas

> - **Inmon, W. H. (2005).** *Building the Data Warehouse*. Wiley. Definición y principios del Data Warehouse.
> - **Marz, N. & Warren, J. (2015).** *Big Data: Principles and Best Practices of Scalable Realtime Data Systems*. Manning Publications. Diferencias entre procesamiento Batch y Streaming.
> - **Chambers, B. & Farley, A. (2020).** *Data Architecture: A Primer for the Data Scientist*. 2.ª edición. Diferencias y casos de uso entre Data Warehouse y Data Lake.

---
