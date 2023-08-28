class Medico():
    def especialidad(self):
        return "Ginecologo"
    
    
class Medico2():
    def especialidad(self):
        return "Anestesiologo"
    

medico1 = Medico()
print(medico1.especialidad())

medico2 = Medico2()
print(medico2.especialidad())