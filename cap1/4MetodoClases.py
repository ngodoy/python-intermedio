class Persona():
    def _init_(self):
        pass

    def despedir(self):
        print("adios")

    @classmethod
    def saludar(cls, nombre):
        print ("Esta saludando" + nombre)


Persona.saludar("Juan")