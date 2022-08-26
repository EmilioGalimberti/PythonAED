_author_ = 'Emilio'

class planta :
    def __init__(self, numero, nombre, tipo, precio, disponibles):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.disponibles = disponibles

def to_string(a): #> se mueve a la derecha    < se mueve a la izquierda
    return 'numero:{:>5} nombre: {:<20} tipo: {:1} precio: {:>16.2f} disponibles: {:>3}'.format(a.numero, a.nombre, a.tipo, a.precio, a.disponibles)
