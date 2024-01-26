#Ejercicio 4
class Perosnaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**2)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**2)
        return Perosnaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
        
        
goku = Perosnaje("Goku",50,50)
vegeta= Perosnaje("Vegeta", 40,40)
jiren = Perosnaje("Jiren", 60,60)

gogeta = goku + vegeta
jireta = gogeta + jiren

print(goku)
print(vegeta)
print(jiren)
print(gogeta)
print(jireta)

