class Curso:
    def __init__(self, nombre, clave, creditos):
        self.nombre = nombre
        self.clave = clave
        self.creditos = creditos

    def descripcion(self):
        return f"Curso: {self.nombre}, Clave: {self.clave}, Créditos: {self.creditos}"
