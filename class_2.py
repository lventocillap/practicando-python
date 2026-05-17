class Persona:
    def __init__(self, nombre, edad, altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura

    def saludar(self):
        print(f"Hola, mi nombre es {self.__nombre} y tengo {self.__edad} años.")


persona = Persona("Juan", 30, 1.75)
nuevo_nombre = "Carlos"
persona.__nombre = nuevo_nombre
persona.saludar()

persona2 = Persona("Maria", 25, 1.65)
persona2.saludar()