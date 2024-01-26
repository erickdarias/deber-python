class Estudiante:
    def _init_(self,nombre,edad,grado) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self) -> None:
         print("Estudiando...")   
         
         
          
nombre = input("Digame su nombre: ")
edad = input("Ahora su edad: ")
grado = input("por ultimo su grado: ")

Estudiante =Estudiante(nombre,edad,grado)

print(f"""
      Datos del estudiante: \n\n 
      Nombre: {Estudiante.nombre} \n
      Edad: {Estudiante.edad} \n
      Grado: {Estudiante.grado}\n
      """)

estudiar = input()
if (estudiar.lower() == "estudiar"):
    Estudiante.estudiar()