# Dossier de Fundamentos — Corte 1
**Asignatura:** Ciencia de Datos · Semana 5
**Periodo:** 2026-B

---

## Caso seleccionado
Pequeña cafetería local en Neiva

---

## 1. Pregunta de negocio + Decisión esperada

**Pregunta de negocio:**
¿Cuáles son los productos más rentables y en qué horarios y días de la semana se registran mayores ventas, para optimizar la preparación de productos, el personal y las promociones?

**Decisión esperada:**
Ajustar la cantidad de productos preparados por horario, asignar el personal en los momentos de mayor afluencia y diseñar ofertas en los productos y horarios con menor rotación, reduciendo desperdicios y aumentando ingresos.

---

## 2. Fuentes y clasificación de datos + Variables relevantes

### Fuentes de datos
- Caja registradora / sistema de ventas diarias
- Formularios y encuestas de satisfacción de clientes
- Sistema de facturación electrónica
- Redes sociales y comentarios libres de los clientes

### Clasificación de datos

| N.º | Tipo de dato | Ejemplo | Clasificación |
|-----|--------------|---------|---------------|
| 1 | Registro de ventas | Fecha, hora, producto, cantidad, valor unitario, total | Estructurado |
| 2 | Datos de clientes | Nombre, correo, teléfono, preferencias registradas | Estructurado |
| 3 | Factura electrónica | Archivo XML/PDF con datos y etiquetas definidas | Semiestructurado |
| 4 | Comentarios y reseñas | Texto libre escrito por los clientes | No estructurado |

### Variables relevantes
- **Fecha y hora de venta** → identificar patrones por día y franja horaria
- **Producto y categoría** → conocer cuáles se venden más y su rentabilidad
- **Cantidad vendida y valor total** → medir desempeño económico
- **Comentarios y calificaciones** → detectar gustos, quejas y oportunidades de mejora

---

## 3. Arquitectura de datos propuesta
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
│ Base de datos SQL → ventas/clientes
│ Carpeta en nube → facturas
│ Archivos de texto → reseñas
└────────────┬───────────────┘
▼
ANÁLISIS
┌────────────────────────────┐
│ Sumas, promedios, totales
│ Agrupación por producto/día/hora
│ Cálculo de tendencias y pronósticos
└────────────┬───────────────┘
▼
VISUALIZACIÓN
┌────────────────────────────┐
│ Tabla de ventas por día y hora
│ Gráfico de barras → productos más vendidos
│ Gráfico de líneas → evolución de ingresos
└────────────────────────────┘

---

## 4. Tipos de analítica objetivo + Riesgo ético

### Analítica descriptiva
¿Cuáles fueron los tres productos más vendidos, los horarios de mayor afluencia y el ingreso total generado durante el mes de agosto de 2026?

### Analítica predictiva
¿Cuántas unidades de cada producto se espera vender por horario durante la próxima semana, según el historial de ventas registrado?

### Riesgo ético
**Protección de datos personales:** Al almacenar información de clientes (nombre, correo, teléfono), se debe garantizar que estos datos no se compartan ni se utilicen sin su consentimiento para fines distintos a los declarados. Se debe respetar la Ley de Protección de Datos Personales de Colombia, evitando recolectar información innecesaria, garantizando confidencialidad y permitiendo que los clientes soliciten la eliminación de sus datos cuando lo deseen.

---
