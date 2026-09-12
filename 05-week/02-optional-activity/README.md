# Parcial Práctico — Corte 1
**Caso seleccionado:** Pequeña cafetería local en Neiva

---

## 1. Identificación y clasificación de 4 tipos de datos

| N.º | Tipo de dato          | Ejemplo                                                     | Clasificación         |
|-----|-----------------------|-------------------------------------------------------------|-----------------------|
| 1   | Registro de ventas    | Fecha, producto, cantidad, valor unitario, total            | Estructurado          |
| 2   | Datos de clientes     | Nombre, correo, teléfono, preferencias registradas          | Estructurado          |
| 3   | Factura electrónica   | Archivo XML/PDF con datos y etiquetas definidas             | Semiestructurado      |
| 4   | Comentarios y reseñas | Texto libre escrito por clientes en redes o encuestas       | No estructurado       |

> **Definiciones:**
> - **Estructurados**: Datos organizados en campos fijos que se almacenan fácilmente en tablas o bases de datos relacionales.
> - **Semiestructurados**: Tienen cierta organización o etiquetas, pero no se ajustan estrictamente a una tabla predefinida.
> - **No estructurados**: No cuentan con un formato ni esquema definido; requieren procesamiento especial para extraer información.

---

## 2. Preguntas de analítica

**Analítica descriptiva:**
¿Cuáles fueron los tres productos más vendidos y cuál fue el ingreso total generado durante el mes de agosto de 2026?

**Analítica predictiva:**
¿Cuántas unidades de cada producto se espera vender durante la próxima semana, tomando como base el historial de ventas?

---

## 3. Diagrama: Fuente → Almacenamiento → Análisis → Visualización

```text
        FUENTE
 ┌────────────────────────────┐
 │ Caja registradora → ventas
 │ Formularios → datos clientes
 │ Sistema → facturas XML/PDF
 │ Redes/encuestas → reseñas
 └────────────┬───────────────┘
              ▼
     ALMACENAMIENTO
 ┌────────────────────────────┐
 │ Base de datos → ventas/clientes
 │ Carpeta nube → facturas
 │ Archivos texto → reseñas
 └────────────┬───────────────┘
              ▼
       ANÁLISIS
 ┌────────────────────────────┐
 │ Sumas, promedios, totales
 │ Agrupación por producto/día
 │ Cálculo de tendencias
 └────────────┬───────────────┘
              ▼
    VISUALIZACIÓN
 ┌────────────────────────────┐
 │ Tabla de ventas por día
 │ Gráfico barras → productos más vendidos
 │ Gráfico líneas → evolución ingresos
 └────────────────────────────┘
4. Frases en inglés
Descriptive analytics summarizes what has already happened using historical data to understand past business performance.
Predictive analytics forecasts what is likely to happen in the future by applying statistical models and trends to existing information.
García, E. y Martínez, A. (2021). Introducción a la Ciencia de Datos: Fundamentos y Aplicaciones. Alfaomega. (Cap. 2: Tipos y estructuras de datos)
Elmasri, R. y Navathe, S. (2017). Sistemas de Bases de Datos: Fundamentos. Pearson Educación. (Sección sobre datos estructurados, semiestructurados y no estructurados)
VanderPlas, J. (2017). Python y Ciencia de Datos: Recetario de herramientas esenciales. O’Reilly Media.
Sobre analítica descriptiva y predictiva
Provost, F. y Fawcett, T. (2018). Ciencia de Datos para Negocios: Qué hay que saber sobre minería de datos y análisis analítico. O’Reilly Media. (Cap. 1: Tipos de análisis descriptivo y predictivo)
Grus, J. (2020). Ciencia de Datos desde Cero: Principios básicos con Python. (2.ª ed.). Anaya Multimedia.
Müller, A. C. y Guido, S. (2018). Introducción al Aprendizaje Automático con Python. Addison-Wesley.
