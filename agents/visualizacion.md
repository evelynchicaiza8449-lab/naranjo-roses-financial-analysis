# Agente de Visualización y Dashboard

## 1. Rol y Objetivo
Diseñar la arquitectura de datos, la estructura de componentes e indicadores clave para el dashboard interactivo de **NARANJO ROSES ECUADOR S.A.**, asegurando la correcta representación visual de la decisión de inversión y despliegue funcional en Vercel.

## 2. Entradas
- Resultados consolidados de finanzas, ingeniería económica, valoración y matriz de riesgos de los agentes previos.
- Especificaciones de contenido requeridas por la rúbrica del proyecto integrador.

## 3. Responsabilidades Específicas
- **Estructura de Componentes:** Interfaz del dashboard con secciones de desafío, entorno macro, ratios, flujo de caja, VAN/TIR, sensibilidad y valoración.
- **Preparación de Datos:** Formatear las salidas financieras en estructuras JSON/JavaScript listas para consumo por el frontend.
- **Verificación de Despliegue:** Asegurar que las visualizaciones sean dinámicas, claras y accesibles en el enlace público alojado en Vercel.

## 4. Entregables
- Código base de la aplicación del dashboard en `src/dashboard/`.
- Archivo de datos unificado para las gráficas e indicadores interactivos.

## 5. Arquitectura de Datos y Componentes

### 5.1. Estructura del Dashboard
- Encabezado con nombre del proyecto y estado de la inversión.
- Sección de contexto macroeconómico: variables clave como inflación, tasa de cambio y demanda.
- Panel de ratios financieros: margen neto, ROI, liquidez, apalancamiento.
- Visualización del flujo de caja proyectado por año.
- Indicadores de VAN y TIR con comparaciones de escenario base vs sensibilidad.
- Gráfica de análisis de sensibilidad y riesgos.
- Resumen de valoración y recomendación de decisión.

### 5.2. Componentes Principales
- `HeaderDashboard`
- `MacroContextPanel`
- `FinancialRatiosCard`
- `CashFlowChart`
- `NpvIrrCard`
- `SensitivityAnalysisChart`
- `ValuationSummary`

## 6. Formato de Datos Unificado
El frontend debe consumir un archivo JSON con la siguiente estructura base:

```json
{
  "project": "NARANJO ROSES ECUADOR S.A.",
  "macro": {
    "inflation": 0.05,
    "exchangeRate": 4.5,
    "demandForecast": "Creciente"
  },
  "financialRatios": {
    "netMargin": 0.18,
    "roi": 0.22,
    "currentRatio": 1.8,
    "debtToEquity": 0.45
  },
  "cashFlow": [
    { "year": 1, "value": 120000 },
    { "year": 2, "value": 150000 },
    { "year": 3, "value": 180000 },
    { "year": 4, "value": 210000 },
    { "year": 5, "value": 240000 }
  ],
  "valuation": {
    "van": 52000,
    "tir": 0.19,
    "decision": "Aprobar"
  },
  "sensitivity": {
    "scenarios": [
      { "label": "Base", "van": 52000, "tir": 0.19 },
      { "label": "Bajo", "van": 32000, "tir": 0.14 },
      { "label": "Alto", "van": 76000, "tir": 0.23 }
    ]
  }
}
```

## 7. Requisitos de Despliegue
- Verificar que `src/dashboard/` incluya rutas estáticas y dinámicas para el frontend.
- Confirmar que el JSON de datos se cargue correctamente en el dashboard.
- Probar el enlace público de Vercel y asegurar visibilidad de gráficos y tarjetas.
- Asegurar la accesibilidad: etiquetas, contrastes y navegación clara.

## 8. Notas Finales
El archivo `agents/visualizacion.md` documenta la propuesta de arquitectura y la estructura de datos que deben implementarse para el dashboard del proyecto integrador.