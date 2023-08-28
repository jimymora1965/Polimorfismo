class Auto:
    def color(self):
        print("El auto es de color rojo")
        
        
class AutoColor:
    def color(self):
        print("El auto es de color verde")
        
        
def definir_color(auto):#esta es una funcion
        print(auto.color)
        
   
#tengo clases diferentes con los mismos metodos pero imprime cosas diferentes.
        
color1 = Auto()
color1.color()

color2 = AutoColor()
color2.color()

print(color1.color())#el print de la funcion.
