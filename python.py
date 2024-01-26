class Estudiante:
    def _init_(self,nombre,edad,grado) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
pedro = Estudiante("Pedro",23,3)

print(pedro.nombre)