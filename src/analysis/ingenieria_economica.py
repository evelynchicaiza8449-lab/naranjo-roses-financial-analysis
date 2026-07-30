import numpy_financial as npf


def evaluar_inversion(inversion_inicial, flujos_caja, tasa_descuento):
    """Calcula VAN, TIR, Beneficio/Costo y Periodo de Recuperación."""
    flujos_completos = [-inversion_inicial] + flujos_caja

    # 1. Valor Actual Neto (VAN)
    van = npf.npv(tasa_descuento, flujos_completos)

    # 2. Tasa Interna de Retorno (TIR)
    tir = npf.irr(flujos_completos)

    # 3. Relación Beneficio / Costo (B/C)
    vp_flujos_positivos = sum([f / ((1 + tasa_descuento) ** (i + 1)) for i, f in enumerate(flujos_caja)])
    bc = vp_flujos_positivos / inversion_inicial

    # 4. Periodo de Recuperación (Payback)
    acumulado = 0
    payback = 0
    for i, f in enumerate(flujos_caja):
        acumulado += f
        if acumulado >= inversion_inicial:
            payback = i + 1
            break

    return {
        "VAN_USD": round(van, 2),
        "TIR_porcentaje": round(tir * 100, 2),
        "Relacion_BC": round(bc, 2),
        "Payback_anios": payback
    }


if __name__ == "__main__":
    # Supuesto de proyecto: Inversión en nueva línea de empaque/riego
    inversion = 1200000  # $1.2M USD
    flujos_proyectados = [350000, 420000, 480000, 530000, 580000]  # 5 años
    wacc = 0.1182  # 11.82%

    resultados = evaluar_inversion(inversion, flujos_proyectados, wacc)

    print("=== EVALUACIÓN DE INGENIERÍA ECONÓMICA ===")
    for k, v in resultados.items():
        print(f"{k}: {v}")
