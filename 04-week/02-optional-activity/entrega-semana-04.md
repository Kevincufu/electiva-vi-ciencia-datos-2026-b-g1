# Actividad — Semana 4: Tipos de analítica y ética

**Estudiante:** Kevin Andres Cuevas Fuentes
**Programa:** Ingeniería Industrial
**Asignatura:** Ciencia de Datos
**Institución:** Corporación Universitaria del Huila — CORHUILA
**Periodo:** 2026-B

---

## 1. Cuatro preguntas por tipo de analítica

###  Descriptiva — ¿Qué está pasando?
> ¿Cuáles son los productos con menor rotación en inventario y en qué meses del año se acumulan más existencias?

Se resume el comportamiento histórico: se identifican los productos que menos se venden y los periodos con mayor acumulación de mercancía. Responde a lo que ocurre hoy, sin predecir ni recomendar.

---

###  Diagnóstica — ¿Por qué está pasando?
> ¿A qué causas se debe la baja rotación: baja demanda estacional, políticas de compra sobredimensionadas o características del producto?

Se investigan las causas del comportamiento observado. Se relacionan volúmenes comprados frente a ventas reales, comportamiento por temporada y tiempo de vida útil para explicar por qué se generan existencias estancadas.

---

###  Predictiva — ¿Qué va a pasar?
> Si se mantienen las tendencias actuales, ¿cuántas unidades de cada producto quedarán sin vender en los próximos seis meses y cuál será su valor estimado?

Se estima el comportamiento futuro basándose en datos históricos. Permite anticipar acumulación y cuantificar el posible impacto económico antes de que ocurra.

---

###  Prescriptiva — ¿Qué debemos hacer?
> ¿Cuántas unidades reducir en las próximas compras y qué porcentaje de descuento aplicar por temporada para evitar sobrestock sin afectar los ingresos?

Se proponen acciones concretas con valores específicos. Indica la decisión óptima para alcanzar el resultado deseado.

---

## 2.  Selección de enfoque de Machine Learning

### Para la analítica predictiva
> **Aprendizaje Automático SUPERVISADO**

**Justificación:** Se conoce claramente qué se quiere predecir (cantidad de unidades sin vender). Se cuenta con datos históricos etiquetados donde se registran ventas reales, compras y acumulación de periodos anteriores. Al tener una variable objetivo definida, el modelo puede aprender de ejemplos pasados y generalizar al futuro. Es el enfoque adecuado cuando se sabe qué buscar y se tienen resultados conocidos (Géron, 2023).

### Para la analítica prescriptiva
> **Modelo SUPERVISADO + Algoritmos de optimización**

**Justificación:** Se parte de predicciones conocidas y se busca la mejor decisión posible bajo ciertas restricciones. Las variables de decisión y sus resultados esperados se conocen, por lo que se guía al modelo con ejemplos. No se busca descubrir patrones desconocidos, sino obtener la mejor respuesta posible.

> **No se usaría Aprendizaje No Supervisado**, porque no se trata de agrupar información sin guía ni descubrir patrones ocultos. En este caso se conoce el objetivo y se tienen ejemplos de resultados, por lo que el enfoque supervisado es el indicado.

---

## 3.  Riesgo ético y sesgo + forma de mitigación

### Riesgo identificado
> **Sesgo histórico y discriminación indirecta:** Si los datos reflejan comportamientos pasados donde ciertos productos o líneas se han impulsado de forma desigual, el modelo podría recomendar reducir productos de ciertas categorías o proveedores basándose en una discriminación histórica y no en su valor real. Datos incompletos o erróneos podrían generar decisiones que perjudiquen a proveedores pequeños o regiones específicas sin justificación real.

### Forma de mitigación
- **Revisión previa de los datos:** Verificar que registros de ventas e inventario estén completos y representen a todos los productos y proveedores por igual, sin omisiones.
- **Transparencia:** Explicar siempre en qué se basa cada recomendación. No aceptar decisiones sin justificación visible.
- **Supervisión humana obligatoria:** Toda recomendación debe ser revisada por personas antes de aplicarse. El modelo es una herramienta, no una autoridad final.
- **Auditoría periódica:** Comparar si las recomendaciones afectan de forma desproporcionada a ciertos productos, líneas o proveedores. Si se detecta sesgo, corregir los datos o recalibrar.

> Como señalan el Banco Mundial y la OCDE (2021), los algoritmos reproducen los sesgos que llevan dentro los datos. Si la información histórica tiene fallas o desigualdades, las predicciones las amplifican. Por eso, antes de confiar en una recomendación, hay que revisar la calidad de los datos y mantener siempre supervisión humana.

---

## Referencias bibliográficas

> - **Géron, A. (2023).** *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O'Reilly Media. Enfoques supervisado y no supervisado.
> - **Sharda, R., Delen, D. & Turban, E. (2020).** *Business Intelligence: A Managerial Approach to Analytics and Data Science*. Pearson. Cuatro niveles de analítica.
> - **Banco Mundial / OCDE (2021).** *Inteligencia Artificial y el futuro del trabajo: Marcos éticos para una IA confiable*. Sesgos en datos y modelos.
