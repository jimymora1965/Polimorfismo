""" class Gato:
    def sonido(self):
        return ("miau")
    
    
class Perro:
    def sonido(self):
        return("Guau")
        
        
gato = Gato()
perro = Perro()

print(gato.sonido())
print(perro.sonido()) """


class Gato:
    def sonido(self):
        return "Miauuuu"
    
class Perro:
    def sonido(self):
        return "Guau Guau"
    
def hacer_sonido(animal):
        print(animal.sonido())
        
        
gato = Gato()
perro = Perro()

hacer_sonido(perro)
hacer_sonido(gato)
    
    
