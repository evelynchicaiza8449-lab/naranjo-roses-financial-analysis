# Registro de Evidencias del Uso de Inteligencia Artificial

## 1. Herramienta y Framework de IA
* **Herramientas utilizadas:** VS Code AI Assistant (Gemini / Claude Code).
* **Enfoque:** Arquitectura multiagente con validación y supervisión humana activa.

## 2. Asignación de Tareas y Prompts Principales

### Agente Analista Financiero
* **Prompt asignado:** `"Genera un script en Python para calcular ratios de liquidez, endeudamiento, ROA, ROE y el WACC para Naranjo Roses Ecuador S.A. basado en la serie histórica de datos en data/raw/datos_naranjo_roses.csv."`
* **Respuesta aceptada:** Se aceptó la lógica general de ratios y la estructura del WACC.

### Agente de Ingeniería Económica
* **Prompt asignado:** `"Escribe una función en Python usando numpy_financial para calcular VAN, TIR, Beneficio/Costo y Payback descontado para un proyecto de inversión de $1.2M USD."`
* **Respuesta aceptada:** Se integraron los cálculos matemáticos de NPV e IRR.

---

## 3. Registro de Errores Identificados y Correcciones Humanas (Auditoría)

| Agente | Error Detectado por el Estudiante | Corrección Aplicada por el Estudiante |
| :--- | :--- | :--- |
| **Financiero** | La IA intentó calcular el WACC sumando la tasa de interés bancaria directamente sin aplicar la deducción fiscal del impuesto a la renta $(1 - T)$. | Se corrigió el script para incluir $(1 - t)$ en la fórmula del costo de la deuda: $WACC = w_e k_e + w_d k_d (1 - T)$. |
| **Ingeniería Económica** | La IA no contempló el signo negativo en la inversión inicial al usar `numpy_financial.npv()`, lo que daba un VAN distorsionado. | Se ajustó el flujo completo insertando `-inversion_inicial` al inicio del arreglo de flujos de caja. |
| **Datos** | La IA asumió precios en Euros por la exportación de rosas. | Se forzó la homologación a Dólares Americanos (USD) dado el esquema de dolarización de Ecuador. |

---

## 4. Decisiones Autónomas Tomadas por el Estudiante
1. **Fijación de supuestos de la Tasa de Descuento ($WACC$):** Se estableció un $WACC$ de 11.82% alineado al riesgo del sector florícola ecuatoriano y la tasa activa de la banca privada (10.5%).
2. **Definición del Desafío:** Se acotó el proyecto a la evaluación de viabilidad de una nueva línea de automatización de empaque y riego automatizado por $1,200,000 USD.

## 5. Reflexión sobre las Limitaciones de la IA
Las herramientas de IA son altamente eficientes para estructurar código y acelerar el análisis numérico, pero carecen de contexto sobre la realidad macroeconómica local (como las tasas efectivas del Banco Central del Ecuador o las regulaciones laborales agrícolas). La validación humana es indispensable para asegurar coherencia financiera.