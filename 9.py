# herança é quando uma classe(filho) herda atributos e metodos de outra classe(pai)
# ela é representada por uma linha e uma seta no final
#    pessoa
# -------------
# nome
# idade
# sexo
# -------------
# aniv()
# 
# aluno
# --------
# matri
# curso
# --------
# cancelarmatri()
# 
# professor
# ------------
# salario
# materia
# ------------
# aumento()

class Pessoa:
     def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
     # metodo
     def aniversario(self):
        self.idade += 1
        print(f'O {self.nome} tem {self.idade} anos')

class Aluno(Pessoa):
     def __init__(self, nome, idade, sexo, matricula, curso):
          super().__init__(nome, idade, sexo)
          self.matricula = matricula
          self.curso = curso

     def cancelarMatricula(self):
          print(f'O aluno {self.nome} foi cancelado')
          if self.matricula:
               return self.matricula == False

     def aniversario(self):
          self.idade += 1
          print(f'O aluno {self.nome} tem {self.idade} anos')
class Prof(Pessoa):
    def __init__(self, nome, idade, sexo, salario, materia):
          super().__init__(nome, idade, sexo)
          self.salario = salario
          self.materia = materia


aluno=Aluno('nyko',17, 'masc', '12334','poo')
aluno.aniversario()

class Bolsista(Aluno):
     def __init__(self, nome, idade, sexo, matricula, curso, bolsa):
          super().__init__(nome, idade, sexo, matricula, curso)
          self.bolsa = bolsa
