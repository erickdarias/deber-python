class Persona: 
     def __init__(self, nombre, edad, nacionalidad):
         self.nombre = nombre
         self.edad= edad
         self.nacionalidad = nacionalidad
         
     def hablar(self):
        print(f"Hola soy {self.nombre} y estoy hablando un poco")
         
class Empleado(Persona): 
    def __init__ (self, nombre, edad, nacionalidad, trabajo, salario): 
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

mario = Empleado("Mario", 45, "ecuatoriano", "Desarrollador", "1500 dolares")
mario.hablar()

class Estudiante(Persona): 
    def __init__(self, nombre, edad, nacionalidad, universidad, carrera):
        super().__init__(nombre, edad, nacionalidad)
        self.universidad = universidad
        self.carrera = carrera
        
erick = Estudiante("Erick", 21, "Ecuatoriano", "Universidad de las Fuerzas Armadas ESPE", "Ingenieria en Tecnologias de la Informacion")
print("El estudiante", erick.nombre, "tiene", erick.edad, "años de edad, estudia en la", erick.universidad, "la carrera", erick.carrera)
erick.hablar()



    
    
      