class Niño:
    def grito(self):
        print("El niño grita duro")
        
class Niña:
    def grito(self):
        print("La niña grita duro")
        
        
niño = Niño()
niño.grito()

niña = Niña()
niña.grito()

print("=========================")
print("Polimorfismo con funcion:")

class Niño:
    def grito(self):
        return "El niño grita muy bajo"
    
class Niña:
    def grito(self):
        return "La niña grita muy muy duro"
        
def tipoGrito(gritar):#funcion con return
    return (gritar.grito())

def nivel_de_grito(nivel):#funcion con print
    print(nivel.grito())
    
    
niño = Niño()
tipoGrito(niño)
    
niña = Niña()
voz = tipoGrito(niña)
print(voz)

print("Funcion con return:")
#Funcion con return: creo variable para poder hacer print y el return
niño = Niño()
voz = tipoGrito(niño)#como la funcion tiene return creo una variable.
print(voz)

print("Funcion con print:")
#funcion con print: los objetos niño y niña estan creados arriba
nivel_de_grito(niño)
