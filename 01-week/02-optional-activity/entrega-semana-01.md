# Actividad — Semana 1: Encuadrar un proyecto de datos

**Estudiante:** Kevin Andres Cuevas Fuentes
**Programa:** Ingeniería Industrial
**Asignatura:** Ciencia de Datos
**Institución:** Corporación Universitaria del Huila — CORHUILA
**Periodo:** 2026-B

---

## 1. Pregunta de negocio

> ¿Cuáles son los productos con menor rotación en inventario y en qué temporadas se acumulan más existencias, para reducir el sobrestock y optimizar el uso del espacio en bodega de una empresa de manufactura?

### Justificación
La pregunta formulada cumple con los principios establecidos por **Provost & Fawcett (2013)**: es **clara, delimitada y accionable**. No resulta excesivamente amplia ni vaga, ya que delimita qué se va a medir (rotación y acumulación), en qué contexto (bodega de una empresa de manufactura) y con qué propósito (reducción de costos y optimización de espacio). Se trata de una pregunta que orienta directamente la recolección de datos y la posterior toma de decisiones.

---

## 2. Datos necesarios y fuentes

| Dato | Descripción | Fuente |
|---|---|---|
| Registro de inventario | Código de producto, cantidad almacenada, fechas de entrada y salida, ubicación en bodega | Sistema de gestión de inventarios / ERP institucional |
| Histórico de ventas | Producto vendido, fecha de transacción, cantidad vendida, valor unitario | Sistema de facturación y ventas |
| Ficha de productos | Categoría, línea de producto, tiempo de vida útil, costo de adquisición | Catálogo maestro de artículos |
| Comportamiento temporal | Mes, temporada comercial, días de rotación promedio por producto | Calendario institucional + cálculo desde registros históricos |

### Justificación
La identificación de datos pertinentes y fuentes accesibles constituye un paso esencial antes de iniciar cualquier proyecto de análisis. Como señalan **Mayer-Schönberger & Cukier (2013)**, el valor del análisis no depende únicamente de la cantidad de datos, sino también de su **calidad, pertinencia y trazabilidad**. El uso de registros operativos internos garantiza información fiable y directamente aplicable al problema planteado.

---

## 3. Decisión o acción esperada

A partir de los resultados del análisis, la empresa podrá tomar decisiones concretas:

-  **Redefinir políticas de compra:** reducir volúmenes de adquisición de productos de baja rotación.
-  **Ajustar inventarios de seguridad:** dimensionar existencias según comportamiento por temporada.
-  **Optimizar uso de espacio:** liberar áreas de bodega ocupadas por productos estancados.
-  **Diseñar estrategias comerciales:** promover mediante descuentos o paquetes los productos acumulados.
-  **Prevenir obsolescencia:** reducir pérdidas económicas por caducidad o desactualización.

### Justificación
La analítica de datos solo genera valor real cuando se traduce en **decisiones concretas y medibles**. Según **Westerman, Bonnet & McAfee (2014)**, cada hallazgo debe estar asociado a una acción definida, con responsables y beneficios esperados. Las decisiones descritas responden directamente a la pregunta de negocio y tienen impacto económico operativo directo sobre la organización.

---

## 4. Tipo de analítica

> **Analítica Descriptiva y Diagnóstica**

### Justificación
Siguiendo la clasificación utilizada por el **Departamento Nacional de Planeación y la Función Pública (2021)**, se distinguen distintos niveles de analítica:

- **Descriptiva:** Responde a **¿Qué está pasando?** Se resume, agrupa y visualiza el comportamiento histórico del inventario para identificar patrones de rotación y temporadas de mayor acumulación. Es la base de cualquier proyecto de datos.
- **Diagnóstica:** Responde a **¿Por qué está pasando?** Se exploran relaciones y causas: ¿la baja rotación se debe a comportamiento estacional?, ¿a características del producto?, ¿a políticas de compra?

> En esta etapa **no se pretende predecir el futuro (analítica predictiva) ni recomendar acciones mediante algoritmos (analítica prescriptiva)**, por lo que los dos niveles mencionados son los adecuados según el objetivo planteado.

---

## Referencias bibliográficas

> - **Provost, F. & Fawcett, T. (2013).** *Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking*. O’Reilly Media.
> - **Mayer-Schönberger, V. & Cukier, K. (2013).** *Big Data: A Revolution That Will Transform How We Live, Work, and Think*. Houghton Mifflin Harcourt.
> - **Westerman, G., Bonnet, D. & McAfee, A. (2014).** *Revolución Digital: Transformación Tecnológica en las Empresas*. MIT Sloan / Fundación Bankinter.
> - **Departamento Nacional de Planeación / Función Pública (2021).** *Guía para la implementación de analítica de datos en entidades públicas*. Adaptado como marco de referencia.

---
