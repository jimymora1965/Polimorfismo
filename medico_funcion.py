
# dos formas de polimorfismo
class Medico:
    def especialidad(self):
        print("Ginecologo")
        
class Medico2:
    def especialidad(self):
        print("Anestesiologo\n")
        
        
medico1 = Medico()
medico1.especialidad()

medico2 = Medico2()
medico2.especialidad()

print("Polimorfismo con funcion")
print("---------------------------")
#con funcion

class Ginecologo:
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
tipo_especialidad(medico2)