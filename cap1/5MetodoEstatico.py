class Persona():
    def _init_(self):
        pass

    def brincar(self):
        print("Brinco")

    @classmethod
    def correr(cls):
        print("Corro")

    @staticmethod
    def nadar():
        print ("Nado")


jose = Persona()
jose.nadar()