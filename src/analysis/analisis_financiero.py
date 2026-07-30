import pandas as pd
import numpy as np

def cargar_datos(ruta_csv):
    """Carga la base de datos de Naranjo Roses desde la carpeta data/raw."""
    return pd.read_csv(ruta_csv)

def calcular_razones_financieras(df):
    """Calcula indicadores de liquidez, endeudamiento y rentabilidad."""
    df_ratios = df.copy()
    
    # Razones de Endeudamiento y Rentabilidad
    df_ratios['ratio_endeudamiento'] = df_ratios['pasivos_totales_usd'] / df_ratios['activos_totales_usd']
    df_ratios['utilidad_bruta_usd'] = df_ratios['ventas_usd'] - df_ratios['costo_ventas_usd']
    df_ratios['utilidad_operativa_usd'] = df_ratios['utilidad_bruta_usd'] - df_ratios['gastos_operativos_usd']
    
    # Margen Operativo y Retorno sobre Activos (ROA) / Patrimonio (ROE)
    df_ratios['margen_operativo'] = df_ratios['utilidad_operativa_usd'] / df_ratios['ventas_usd']
    df_ratios['roa'] = df_ratios['utilidad_operativa_usd'] / df_ratios['activos_totales_usd']
    df_ratios['roe'] = df_ratios['utilidad_operativa_usd'] / df_ratios['patrimonio_usd']
    
    return df_ratios

def calcular_wacc(costo_deuda, costo_patrimonio, tasa_impuestos, pasivo, patrimonio):
    """Calcula el Costo Promedio Ponderado de Capital (WACC)."""
    v = pasivo + patrimonio
    w_d = pasivo / v
    w_e = patrimonio / v
    
    wacc = (w_e * costo_patrimonio) + (w_d * costo_deuda * (1 - tasa_impuestos))
    return wacc

if __name__ == "__main__":
    # Ruta del archivo cargado anteriormente
    ruta = "data/raw/datos_naranjo_roses.csv"
    
    try:
        df = cargar_datos(ruta)
        df_resultados = calcular_razones_financieras(df)
        
        # Parámetros para Naranjo Roses (Sector Florícola)
        # Costo de Deuda (banca privada Ecuador ~ 10.5%), Costo Patrimonio (~ 14%), Impuestos (25%)
        wacc = calcular_wacc(
            costo_deuda=0.105, 
            costo_patrimonio=0.14, 
            tasa_impuestos=0.25, 
            pasivo=df_resultados['pasivos_totales_usd'].iloc[-1], 
            patrimonio=df_resultados['patrimonio_usd'].iloc[-1]
        )
        
        print("=== ANÁLISIS FINANCIERO NARANJO ROSES ===")
        print(df_resultados[['anio', 'ventas_usd', 'ratio_endeudamiento', 'roa', 'roe']])
        print(f"\nWACC Estimado para el proyecto: {wacc * 100:.2f}%")
        
    except FileNotFoundError:
        print(f"Asegúrate de que el archivo exista en: {ruta}")
