from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, correo, especialidad):
        super().__init__(nombre, edad, correo)
        self.__especialidad = especialidad
        self.__cursos_asignados = []

    def asignar_curso(self, curso):
        self.__cursos_asignados.append(curso)

    def mostrar_asignaciones(self):
        print(f"Cursos asignados al profesor {self.get_nombre()}:")
        if not self.__cursos_asignados:
            print("No hay cursos asignados.")
        for curso in self.__cursos_asignados:
            print(f"- {curso.nombre}")
