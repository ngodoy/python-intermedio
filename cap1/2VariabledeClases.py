class Persona():
    "variable de clases"
    Edad = 25

    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad


persona1 = Persona("Jose", "Mexicano")

print(persona1.Edad)