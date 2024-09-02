class Calzado:
    def __init__(self, tipo, suela, fecha_creacion, origen):
        self.tipo = tipo
        self.suela = suela
        self.fecha_creacion = fecha_creacion
        self.origen = origen

    def mostrar_info(self):
        return (f"Tipo: {self.tipo}, Suela: {self.suela}, "
                f"Fecha de creación: {self.fecha_creacion}, Origen: {self.origen}")


class Zapatilla(Calzado):
    def __init__(self, tipo, suela, fecha_creacion, origen, numero, modelo, materiales, stock):
        super().__init__(tipo, suela, fecha_creacion, origen)
        self.numero = numero
        self.modelo = modelo
        self.materiales = materiales
        self.stock = stock

    def mostrar_zapatilla_info(self):
        return (f"{self.mostrar_info()}, Número: {self.numero}, Modelo: {self.modelo}, "
                f"Materiales: {self.materiales}, Stock: {self.stock}")

calzado1 = Calzado("Deportivo", "Goma", "2023-01-15", "Italia")
zapatilla1 = Zapatilla("Deportiva", "Goma", "2023-01-15", "Italia", 42, "Air Max", "Sintético", 50)

print(calzado1.mostrar_info())
print(zapatilla1.mostrar_zapatilla_info())
