# libreria_funciones_proyecto1.py

def flujo_caja_neto(ingresos, costos_operativos):
    """Calcula el flujo de caja neto."""
    return ingresos - costos_operativos

def precio_venta_final(costo_base, margen_ganancia_pct, descuento_pct, iva_pct):
    """Calcula el precio final de venta aplicando margen, descuento e IVA."""
    precio_con_margen = costo_base * (1 + margen_ganancia_pct / 100)
    precio_con_descuento = precio_con_margen * (1 - descuento_pct / 100)
    return precio_con_descuento * (1 + iva_pct / 100)

def produccion_real_linea(minutos_disponibles, eficiencia_pct, tiempo_estandar, defectos_pct, num_personas):
    """Calcula la producción neta real de una línea de confección textil."""
    if tiempo_estandar <= 0 or num_personas <= 0:
        return 0.0
        
    minutos_totales_linea = minutos_disponibles * num_personas
    minutos_productivos = minutos_totales_linea * (eficiencia_pct / 100)
    produccion_bruta = minutos_productivos / tiempo_estandar
    produccion_neta = produccion_bruta * (1 - defectos_pct / 100)
    
    return round(produccion_neta, 2)



class LoteProduccionTextil:
    def __init__(self, id_lote, tipo_tela, color, cantidad_metros, estado="Programado"):
        """
        Clase que representa un lote de producción en la planta textil.
        """
        self.id_lote = id_lote
        self.tipo_tela = tipo_tela
        self.color = color
        self.cantidad_metros = float(cantidad_metros)
        self.estado = estado  # Ej. Programado, En teñido, En corte, Terminado

    def actualizar_estado(self, nuevo_estado):
        """Método para actualizar el estado del lote."""
        self.estado = nuevo_estado

    def actualizar_cantidad(self, nueva_cantidad):
        """Método para corregir la cantidad de metros del lote."""
        self.cantidad_metros = float(nueva_cantidad)
