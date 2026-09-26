<!--
CONFIG
FULL_NAME: Kevin Cifuentes
GITHUB_USER: kevincufu
-->

# Actividad Semana 6 — ERD de tu caso
**Programa:** Ingeniería Industrial
**Asignatura:** Ciencia de Datos
**Institución:** CORHUILA
**Periodo:** 2026-B

---

## 1. Diagrama Entidad-Relación (ERD)

### Caso: Gestión de Proyectos, Empleados y Tareas
┌────────────────────┐ ┌────────────────────┐
│ EMPLEADO │ │ PROYECTO │
├────────────────────┤ ├────────────────────┤
│ ID_Empleado (PK) │◄───────►│ ID_Proyecto (PK) │
│ Nombre │ N:M │ Nombre │
│ Apellido │ │ Descripción │
│ Cargo │ │ Fecha_Inicio │
│ Correo │ │ Estado │
└────────────────────┘ └────────────────────┘
▲ ▲
│ │
│ ┌────────────────────┐
│ │ ASIGNACIÓN │
│ ├────────────────────┤
└─────────│ ID_Asignación (PK) │──────────┘
│ ID_Empleado (FK) │
│ ID_Proyecto (FK) │
│ Rol_En_Proyecto │
│ Horas_Asignadas │
└────────────────────┘

### Detalle de entidades, claves y relaciones

| Entidad | Atributos | PK | FK | Relación |
|---|---|---|---|---|
| **Empleado** | ID_Empleado, Nombre, Apellido, Cargo, Correo | ID_Empleado | — | Participa en N proyectos |
| **Proyecto** | ID_Proyecto, Nombre_Proy, Descripción, Fecha_Inicio, Estado | ID_Proyecto | — | Tiene N empleados asignados |
| **Asignación** (intermedia) | ID_Asignación, ID_Empleado, ID_Proyecto, Rol, Horas | ID_Asignación | ID_Empleado → Empleado<br>ID_Proyecto → Proyecto | Resuelve relación **N:M** |

> **Relación N:M:** Un empleado puede participar en varios proyectos; un proyecto puede tener varios empleados → resuelta con tabla intermedia `Asignación`.

---

## 2. Enfoque: Relacional o NoSQL?

### Opción elegida: **Modelo Relacional**

**Justificación:**
1. **Estructura estable y definida:** Los datos de empleados, proyectos y asignaciones tienen atributos fijos que no cambian con frecuencia, ajustándose perfectamente a un esquema relacional.
2. **Integridad referencial indispensable:** Es necesario asegurar que no existan asignaciones a empleados o proyectos inexistentes. Las claves foráneas garantizan esta consistencia de forma nativa.
3. **Consultas cruzadas frecuentes:** Las consultas más habituales combinan información de varias entidades: *"¿En qué proyectos trabaja este empleado?"*, *"¿Qué personal está asignado a este proyecto?"* → las uniones (`JOIN`) en SQL son eficientes y claras.
4. **Consistencia prioritaria:** Cambios como la actualización del cargo de un empleado o el estado de un proyecto deben reflejarse de forma segura y uniforme → las propiedades **ACID** son fundamentales.
5. **Sin justificación para NoSQL:** No se manejan grandes volúmenes de datos no estructurados, esquemas variables ni distribución masiva que hagan preferente NoSQL.

> *Nota: No se descartaría NoSQL en una etapa futura si se incorporan registros de desempeño en tiempo real, documentos o métricas de fuentes heterogéneas, pero para el caso actual el modelo relacional es la opción más adecuada.*

---

## 3. Aplicación de Normalización

Se aplicaron reglas de **1ª, 2ª y 3ª Forma Normal** para eliminar redundancia y prevenir anomalías:

| Elemento | Repetición evitada | Resolución |
|---|---|---|
| **Empleado** | Repetir nombre, apellido, cargo y correo en cada fila de asignación → riesgo de errores de escritura e información desactualizada | Tabla independiente `Empleado`; solo se referencia mediante `ID_Empleado` ✅ |
| **Proyecto** | Repetir nombre, descripción y fecha por cada empleado asignado → si cambia el nombre, habría que actualizarlo en múltiples registros | Tabla independiente `Proyecto`; identificada por su `ID_Proyecto` ✅ |
| **Relación N:M** | Mezclar datos del empleado, del proyecto y de la vinculación en una sola tabla → imposible asignar diferente rol o dedicación del mismo empleado en proyectos distintos | Tabla intermedia `Asignación` que separa la relación y además almacena datos propios: rol y horas asignadas ✅ |

**Resumen:**
- Se eliminó la duplicidad de datos que obligaba a escribir la misma información varias veces.
- Se evitó la inconsistencia que se produce al actualizar un dato en un lugar y no en todos los demás.
- Se separó lo que es una entidad independiente de lo que es una relación entre entidades.

---

## 4. Bibliografía
- NAVATHE, S. y ELMASRI, R. (2015). *Sistemas de Bases de Datos*. 6.ª ed. Pearson. Capítulos 3–5: Modelo Entidad-Relación y Normalización.
- MARTÍNEZ GARCÍA, R. (2021). *Bases de Datos NoSQL: Fundamentos y Casos de Uso*. Universidad Politécnica de Madrid.
- DATE, C. J. (2018). *Introducción a los Sistemas de Bases de Datos*. 8.ª ed. Addison-Wesley.
