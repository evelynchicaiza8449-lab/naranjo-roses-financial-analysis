# Sistema Multiagente - Análisis Financiero Naranjo Roses Ecuador S.A.

## 1. Objetivo General
Evaluar la viabilidad económica, financiera y de inversión de **NARANJO ROSES ECUADOR S.A.** mediante un sistema multiagente coordinado, analizando la estructura de costos, decisiones de financiamiento, indicadores de rentabilidad, valoración de la empresa y gestión de riesgos en el sector florícola ecuatoriano.

## 2. Definición de Agentes y Responsabilidades

| Agente | Archivo de Prompt | Responsabilidad Principal |
| :--- | :--- | :--- |
| **Coordinador** | `agents/coordinador.md` | Divide la tarea general, asigna actividades y valida la integración global. |
| **Investigador Económico** | `agents/investigador_economico.md` | Analiza el entorno macroeconómico (Ecuador, inflación, USD) y sectorial (exportación de rosas). |
| **Analista de Datos** | `agents/analista_datos.md` | Procesa, limpia y valida los datos financieros brutos (`data/raw`). |
| **Analista Financiero** | `agents/analista_financiero.md` | Calcula razones financieras (liquidez, endeudamiento, DuPont) y Flujo de Caja. |
| **Ingeniería Económica** | `agents/ingenieria_economica.md` | Evalúa VAN, TIR, B/C, Payback y análisis de sensibilidad/escenarios. |
| **Valoración** | `agents/valoracion.md` | Aplica el método de Flujo de Caja Descontado (FCD) y Múltiples Comparables. |
| **Auditor de Riesgos** | `agents/auditor_riesgos.md` | Audita los cálculos numéricos, identifica supuestos inconsistentes y gestiona la matriz de riesgos. |
| **Visualización** | `agents/visualizacion.md` | Diseña las especificaciones de datos e indicadores para el dashboard en Vercel. |

## 3. Secuencia de Trabajo y Flujo de Información
1. **Fase 1 (Entorno y Datos):** El *Investigador Económico* recopila contexto macro/sectorial. El *Analista de Datos* estructura los balances y PyG de Naranjo Roses.
2. **Fase 2 (Modelamiento Financiero):** El *Analista Financiero* calcula ratios e hitos de flujo de caja. El de *Ingeniería Económica* genera métricas VAN/TIR y WACC.
3. **Fase 3 (Valoración y Auditoría):** El agente de *Valoración* estima el valor firme. El *Auditor de Riesgos* revisa matemáticamente todo el modelo.
4. **Fase 4 (Despliegue y Reporte):** El de *Visualización* estructura los JSON para la web, y el *Coordinador* ensambla el informe final.

## 4. Reglas de Validación y Consistencia
* Todo cálculo financiero debe ser reproducible mediante scripts ejecutables en `src/analysis/`.
* Si el *Auditor de Riesgos* encuentra una discrepancia > 1% en los cálculos de VAN/TIR o WACC, el módulo correspondiente debe recalculares.
* No se aceptan datos inventados sin el prefijo explícito de `[SUPUESTO_JUSTIFICADO]`.
