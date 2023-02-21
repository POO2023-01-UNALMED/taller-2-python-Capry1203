class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        listaColors = ["rojo","verde","amarillo","negro","blanco"]

        if color in listaColors:
            self.color = color 


class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        
     def cantidadAsientos(self):
           cont = 0
           asientos = self.asientos

           for i in asientos:
               if type(i) == Asiento:
                   cont += 1
            
            return cont



class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if (tipo == "gasolina") or (tipo == "electrico"):
            self.tipo = tipo
