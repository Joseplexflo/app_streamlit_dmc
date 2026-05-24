def flujo_caja_neto(ingresos, costos_operativos):
    """
    Calcula el flujo de caja neto.
    """
    return ingresos - costos_operativos

def precio_venta_final(costo_base, margen_ganancia_pct, descuento_pct, iva_pct):
    """
    Calcula el precio final de venta aplicando margen, descuento e IVA.
    """
    precio_con_margen = costo_base * (1 + margen_ganancia_pct / 100)
    precio_con_descuento = precio_con_margen * (1 - descuento_pct / 100)
    precio_final = precio_con_descuento * (1 + iva_pct / 100)
    
    return precio_final
