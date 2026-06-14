class Mascota:
    
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre    
        self.especie = especie  
        self.edad = edad        

    def mostrar_informacion(self):
        print("-" * 30)
        print(f"Nombre:  {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad:    {self.edad} años")
        print("-" * 30)

    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            return "¡Guau guau!"
        elif self.especie.lower() == "gato":
            return "¡Miau miau!"
        elif self.especie.lower() == "loro":
            return "¡Hola hola!"
        else:
            return "Sonido no definido para esta especie"