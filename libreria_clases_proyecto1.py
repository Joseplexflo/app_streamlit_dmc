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
