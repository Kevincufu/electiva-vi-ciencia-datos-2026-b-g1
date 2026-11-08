-- CONSULTA ORIGINAL (menos eficiente)
SELECT
    YEAR(fecha) AS anio,
    MONTH(fecha) AS mes,
    SUM(ventas) AS ventas_mensuales
FROM ventas
WHERE YEAR(fecha) = 2025
GROUP BY YEAR(fecha), MONTH(fecha)
ORDER BY anio, mes;

-- CONSULTA OPTIMIZADA
SELECT
    DATE_TRUNC('month', fecha) AS mes,
    SUM(ventas) AS ventas_mensuales
FROM ventas
WHERE fecha >= DATE '2025-01-01'
  AND fecha <  DATE '2026-01-01'
GROUP BY DATE_TRUNC('month', fecha)
ORDER BY mes;

-- Índice recomendado para filtrar por rango temporal:
CREATE INDEX idx_ventas_fecha ON ventas(fecha);

-- EXPLICACIÓN
-- La mejora principal está en el filtro: en la versión original se aplica YEAR(fecha)
-- sobre la columna, lo cual puede impedir el uso eficiente de un índice sobre fecha.
-- El rango >= / < permite un acceso más selectivo e index-friendly.
-- DATE_TRUNC se mantiene para agrupar el resultado por mes.


-- ================================================
-- BIBLIOGRAFÍA / REFERENCIAS TÉCNICAS (APA 7)
-- ================================================
-- PostgreSQL Global Development Group. (2026). Date/Time Functions and Operators: date_trunc. PostgreSQL 16 Documentation. https://www.postgresql.org/docs/16/functions-datetime.html
-- PostgreSQL Global Development Group. (2026). Indexes. PostgreSQL Documentation. https://www.postgresql.org/docs/current/indexes.html
