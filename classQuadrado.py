quadrado.py

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novoLado):
        self.lado = novoLado

    def valorLado(self):
        return self.lado

    def area(self):
        return self.lado*self.lado
        
  
///////////////////////////////////

quadradoTeste.py 

from quadrado import Quadrado

lado = int(input("Informe valor do lado do quadrado: "))
q = Quadrado(lado)
print("O valor do lado eh %d e a area do quadrado eh %d" % (q.valorLado(),q.area()))
lado = int(input("Informe novo valor para o lado do quadrado: "))
q.mudarLado(lado)
print("O novo valor para lado eh %d e a nova area do quadrado eh %d" % (q.valorLado(),q.area()))
