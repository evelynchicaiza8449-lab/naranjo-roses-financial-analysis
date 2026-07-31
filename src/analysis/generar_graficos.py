import os
import matplotlib.pyplot as plt
import numpy as np

# Configuración de rutas para guardar en /reports
directorio_actual = os.path.dirname(os.path.abspath(__file__))
raiz_proyecto = os.path.abspath(os.path.join(directorio_actual, "..", ".."))
carpeta_reports = os.path.join(raiz_proyecto, "reports")

os.makedirs(carpeta_reports, exist_ok=True)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

def generar_grafico_flujo_caja():
    anios = ['Año 0', 'Año 1', 'Año 2', 'Año 3', 'Año 4', 'Año 5']
    flujos = [-1200000, 350000, 420000, 480000, 530000, 580000]
    acumulado = np.cumsum(flujos)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    colores = ['#e11d48' if x < 0 else '#10b981' for x in flujos]
    ax.bar(anios, [f / 1000 for f in flujos], color=colores, alpha=0.6, label='Flujo Neto Anual (k USD)')
    ax.plot(anios, acumulado / 1000, color='#2563eb', marker='o', linewidth=2.5, label='Flujo Acumulado (k USD)')
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--')

    ax.set_title('Naranjo Roses S.A. - Recuperación de la Inversión (Payback)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Miles de USD ($)')
    ax.legend(loc='upper left')
    plt.tight_layout()
    
    plt.savefig(os.path.join(carpeta_reports, 'grafico_flujo_caja.png'), dpi=300)
    plt.close()

def generar_grafico_sensibilidad():
    escenarios = ['Pesimista (-15% Ventas)', 'Base (0%)', 'Optimista (+10% Ventas)']
    van_valores = [-85.4, 384.5, 612.0]
    
    fig, ax = plt.subplots(figsize=(8, 4))
    colores = ['#ef4444', '#3b82f6', '#10b981']
    
    bars = ax.barh(escenarios, van_valores, color=colores, height=0.5)
    ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
    
    for bar in bars:
        width = bar.get_width()
        pos_x = width + 15 if width >= 0 else width - 50
        ax.text(pos_x, bar.get_y() + bar.get_height()/2, f'${width:.1f}k USD', 
                va='center', ha='left' if width >= 0 else 'right', fontweight='bold')

    ax.set_title('Análisis de Sensibilidad del VAN por Escenario', fontsize=12, fontweight='bold')
    ax.set_xlabel('Valor Actual Neto en Miles de USD ($)')
    plt.tight_layout()
    
    plt.savefig(os.path.join(carpeta_reports, 'grafico_sensibilidad.png'), dpi=300)
    plt.close()

if __name__ == "__main__":
    generar_grafico_flujo_caja()
    generar_grafico_sensibilidad()
    print("¡Gráficas generadas con éxito en la carpeta reports!")