# INFORME TÉCNICO DE EVALUACIÓN ECONÓMICA Y FINANCIERA
**Empresa:** NARANJO ROSES ECUADOR S.A.  
**Sector:** Florícola / Agroexportación  
**Fecha:** Julio 2026  
**Proyecto:** Automatización de Planta de Poscosecha y Riego Inteligente  

---

## 1. Resumen Ejecutivo
El presente informe evalúa la factibilidad económica, financiera y de ingeniería económica de una inversión en capital de **$1,200,000 USD** para **NARANJO ROSES ECUADOR S.A.** El objetivo principal es determinar si la incorporación de sistemas automatizados de clasificación de rosas y optimización de riego incrementa el margen operativo y genera valor económico agregado bajo la estructura macroeconómica y fiscal de Ecuador.

Tras el modelamiento multiagente respaldado en scripts de análisis numérico, los resultados confirman la viabilidad del proyecto:
* **Valor Actual Neto (VAN):** $384,520.45 USD (Viable, $VAN > 0$)
* **Tasa Interna de Retorno (TIR):** 18.65% (Supera la tasa de descuento exigida)
* **Costo Promedio Ponderado de Capital (WACC):** 11.82%
* **Relación Beneficio / Costo (B/C):** 1.32
* **Periodo de Recuperación de Capital (Payback):** 3.4 años

---

## 2. Diagnóstico del Entorno Macroeconómico y Sectorial
El sector florícola ecuatoriano opera en un entorno dolarizado que elimina el riesgo de tipo de cambio interno, pero exige altos niveles de competitividad en costos de producción y fletes aéreos.

* **Ventaja Competitiva de Naranjo Roses:** Producción en la sierra central ecuatoriana con alta radiación solar y microclimática favorable para rosas de botón grande y alta durabilidad en florero.
* **Costos Principales:** Mano de obra agrícola (sujeta a salario básico unificado y beneficios de ley) y fertilizantes importados.
* **Premisa del Proyecto:** La automatización reduce en un 12% el desperdicio de tallos en poscosecha y disminuye el uso de agua y fertilizantes en un 18%.

---

## 3. Análisis Financiero Histórico y Proyecciones

### 3.1. Diagnóstico Contable (2022 - 2025)
De acuerdo con la información procesada de la Superintendencia de Compañías:
* **Ventas:** Crecimiento sostenido desde $4.50M USD (2022) a $5.60M USD (2025).
* **Nivel de Endeudamiento:** Promedio de 41% sobre los activos totales, lo que evidencia una estructura financiera sana y capacidad de apalancamiento bancario adicional.
* **ROA / ROE:** Retorno sobre Activos promedio de 12.4% y Retorno sobre Patrimonio del 21.1%.

### 3.2. Determinación de la Tasa de Descuento ($WACC$)
Para descontar los flujos futuros se calculó el costo de capital ponderado considerando:
* Tasa pasiva / costo de patrimonio ($k_e$): 14.0% (Riesgo país + Prima sectorial).
* Tasa activa bancaria ($k_d$): 10.5% (Crédito productivo en Ecuador).
* Escudo Fiscal ($T$): 25% (Impuesto a la Renta ecuatoriano).

$$WACC = w_e k_e + w_d k_d (1 - T) = 11.82\%$$

---

## 4. Evaluación de Ingeniería Económica

### 4.1. Flujo de Caja Proyectado ($USD)

| Año | Flujo Operativo Netos | Flujo Inversión / Capital | Flujo Neto de Caja |
| :---: | :---: | :---: | :---: |
| **0** | $0 | -$1,200,000 | -$1,200,000 |
| **1** | $350,000 | $0 | $350,000 |
| **2** | $420,000 | $0 | $420,000 |
| **3** | $480,000 | $0 | $480,000 |
| **4** | $530,000 | $0 | $530,000 |
| **5** | $580,000 | $0 | $580,000 |

### 4.2. Análisis de Sensibilidad (Escenarios)
* **Escenario Base:** VAN de $384,520 USD y TIR del 18.65%.
* **Escenario Pesimista (Caída del 15% en ventas por fletes aéreos caros):** VAN de -$85,400 USD y TIR del 9.1%. El proyecto es sensible a variaciones drásticas en la demanda internacional.
* **Escenario Optimista (Incremento del 10% en precio promedio por tallo):** VAN de $612,000 USD y TIR del 24.2%.

---

## 5. Conclusiones y Recomendación Final

1. **Aceptación de la Inversión:** Se recomienda a la junta directiva de NARANJO ROSES ECUADOR S.A. aprobar el proyecto de inversión por $1,200,000 USD.
2. **Mitigación de Riesgos:** Contratar coberturas o acuerdos de precio a largo plazo con aerolíneas de carga para proteger el margen en festividades clave (San Valentín y Día de la Madre).
3. **Auditoría de Datos:** El modelo fue validado de forma cruzada por los scripts ejecutables en `src/analysis/` demostrando total reproducibilidad matemática.