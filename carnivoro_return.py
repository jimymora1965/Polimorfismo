class Tigre:
    def carnivoro(self):
        return ("El tigre es carnivoro")
    
class Lobo:
    def carnivoro(self):
        print("El lobo es carnivoro")
        
def comer_carne(animal):
    print(animal.carnivoro())
    
tigre = Tigre()
print(tigre.carnivoro())#print porque tiene tiene return

lobo = Lobo()
lobo.carnivoro()#lobo.carnvoro() porque lobo tiene print

comer_carne(lobo)#llamando al metodo comer_carne


""" class Ginecologo:
    def especialidad(self):
        return "Ginecologo"
    
class Anestesiologo:
    def especialidad(self):
        return "Anestesiologo"

# la funcion
def tipo_especialidad(especialista):
    print(especialista.especialidad())

medico1 = Ginecologo()
medico2 = Anestesiologo()


tipo_especialidad(medico1)
tipo_especialidad(medico2) """


