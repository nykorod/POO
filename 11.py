# polimorfismo
# poli = muito
# morfo = modos
# muitos modos de algo acontecer/ser/fazer algo
# assinatura do metodo:
# se a quantidades e tipos de PARAMETROS for a msm
# ex: ((l1: int,l2:float) return true e (v1: int, v2: float) retunr int) tem a MESMA ASSINATURA
# 
# TIPOS DE POLIMORFISMO:
# sobreposição
# quando sobrepomos um metodo de uma superclasse em uma subclasse usando a msm assinatura
# mesma assinatura em classes diferentes

# sobrecarga
# quando 
# mesma classe com assinaturas diferentes
# 

class Animal:
     def __init__(self, idade, peso):
          self.idade= idade
          self.peso = peso
     def andar(self):
          return ("andando")
     def comer(self):
          return ("comendo")

class Cachorro(Animal):
     def __init__(self, idade, peso, raca):
          super().__init__(idade, peso)
          self.raca = raca
     def andar(self):
          return ("andando como cachorro")
     def comer(self):
          return ('comendo ração')
     def latir(self, frase: str, idade: int):
          if frase == 'ola' and idade == 1:
               return ('abanar e latir')
          else:
               return ('rosnar')
     def latir(self, peso: float):
          if peso >= 5:
               return 'ignora'
          else:
               return 'abanar'
c2 = Cachorro(3,6.7,'pintcher')
print(c2.latir('ola', 1))









     
class Peixe(Animal):
     def __init__(self, idade, peso, escama):
          super().__init__(idade, peso)
          self.escama = escama
     def andar(self):
          return ("nadando como peixe")
     def comer(self):
          return ("comendo peixe")
c = Cachorro(3, 10, 'golden retriever')
print(c.andar())

p = Peixe(2, 4, 'azul')
print(p.andar())


