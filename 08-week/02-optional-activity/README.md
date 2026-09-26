<!--
CONFIG
FULL_NAME: Kevin Cifuentes
GITHUB_USER: kevincufu
-->

# 🔄 Pipeline ETL — Semana 8 · Corte 2
**Programa:** Ingeniería Industrial | **Asignatura:** Ciencia de Datos | **Periodo:** 2026-B

---

## 1. Diagrama del Pipeline ETL
┌─────────────────┐ ┌──────────────────┐ ┌─────────────────────┐ ┌──────────────────┐
│ FUENTES DE │ │ EXTRACCIÓN │ │ TRANSFORMACIÓN │ │ CARGA / BI │
│ DATOS │────▶│ │────▶│ │────▶│ │
│ │ │ • Python / pandas│ │ • Limpieza de datos │ │ • Base de datos │
│ • API pública │ │ • requests │ │ • Filtrado, cálculos │ │ (PostgreSQL) │
│ • Archivos CSV │ │ • Lectura CSV │ │ • Agrupaciones │ │ • Tablero BI │
│ • Base de datos │ │ • Conexión SQL │ │ • Validaciones │ │ (Power BI) │
└─────────────────┘ └──────────────────┘ └─────────────────────┘ └──────────────────┘

### Herramienta por etapa:
| Etapa          | Herramienta principal          | Propósito |
|----------------|---------------------------------|-----------|
| **Fuente**     | API REST + archivos CSV         | Obtener datos externos e internos |
| **Extracción** | Python + `requests` + `pandas`  | Conectar y descargar datos |
| **Transformación** | `pandas` + limpieza lógica    | Filtrar, unir, calcular, normalizar |
| **Carga**      | SQL / PostgreSQL + Power BI      | Almacenar y visualizar |

---

## 2. Batch vs Streaming — Justificación

| Tipo      | Partes del pipeline | ¿Por qué? |
|-----------|---------------------|-----------|
| **Batch** ✅ | Extracción desde CSV, base de datos, API (ejecución programada cada cierto tiempo) | Los datos no cambian en tiempo real de forma crítica; se procesan por lotes en horarios definidos. Es más eficiente y económico para volúmenes grandes. |
| **Streaming** ⏱️ | No aplica en este caso | No se requiere monitoreo instantáneo ni respuestas en segundos. Si se trabajara con ventas en vivo o sensores, sí se usaría flujo continuo. |

> **Conclusión:** Este pipeline funciona por **lotes (batch)** porque la información se actualiza periódicamente, no minuto a minuto. Simplifica la infraestructura y reduce costos.

---

## 3. Consumo de API Pública en Python (Ejercicio Opcional)

```python
import requests
import pandas as pd

# Consumir API pública: lista de usuarios
url = "https://jsonplaceholder.typicode.com/users"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()
    
    # Mostrar solo los primeros 3 registros
    print("✅ Datos obtenidos correctamente")
    print(f"Total de registros: {len(datos)}")
    print("\n=== Primeros 3 registros ===")
    
    for i, usuario in enumerate(datos[:3], 1):
        print(f"\nRegistro {i}:")
        print(f"  Nombre: {usuario['name']}")
        print(f"  Usuario: {usuario['username']}")
        print(f"  Correo: {usuario['email']}")
        print(f"  Ciudad: {usuario['address']['city']}")
else:
    print(f"❌ Error en la solicitud: Código {respuesta.status_code}")
✅ Datos obtenidos correctamente
Total de registros: 10

=== Primeros 3 registros ===

Registro 1:
  Nombre: Leanne Graham
  Usuario: Bret
  Correo: Sincere@april.biz
  Ciudad: Gwenborough

Registro 2:
  Nombre: Ervin Howell
  Usuario: Antonette
  Correo: Shanna@melissa.tv
  Ciudad: Wisokyburgh

Registro 3:
  Nombre: Clementine Bauch
  Usuario: Samantha
  Correo: Nathan@yesenia.net
  Ciudad: McKenziehaven
4. Bibliografía
CORHUILA. (2026). Guía de Actividad Práctica: Semana 8 — Diseña un pipeline ETL. Neiva, Colombia.
REQUESTS. (2025). Requests: HTTP for Humans. Documentación oficial.
PANDAS DEVELOPMENT TEAM. (2025). pandas: Powerful Python Data Analysis Toolkit.
CHASE, J. (2020). Data Pipelines Pocket Reference. O'Reilly.
