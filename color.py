class Colombia:
    def color(self):
        print("La bandera de colombia tiene 3 colores")
        
        
class Ecuador:
    def color(self):
        print("La bandera de Ecuador tiene un escudo")
        
def color_ecuador(banderas):
    print(banderas.color())
        
        

banderaColombia = Colombia()
banderaColombia.color()

banderaEcuador = Ecuador()
banderaEcuador.color()


bandera = Ecuador()
color_ecuador(bandera)
