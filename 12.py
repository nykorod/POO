class AcoesVideo:
     def __init__(self):
          pass

     def play(self):
          if self.repr:
               return 'pause'
          else:
               return 'play'
     def like(self):
          self.curtidas += 1
          return self.curtidas
     

class Video(AcoesVideo):
     def __init__(self, tit='', av=0, view=0, curtidas: int = 0, repr=False):
          super().__init__()
          self.tit = tit
          self.av = av
          self.view = view
          self.curtidas = curtidas
          self.repr = repr
print(Video(curtidas=500).like())


class Pessoa:
     def __init__(self,nome='',idade=0,sexo='', exp =0):
          self.nome = nome
          self.idade = idade
          self.sexo = sexo
          self.exp = exp
     
     def ganharExp(self):
          self.exp += 1


class Gafanhoto(Pessoa):
     def __init__(self, nome = '', idade = 0, sexo = '', exp = 0,login='',totAssistido=0):
          super().__init__(nome, idade, sexo, exp)
          self.login = login
          self.totAssistido = totAssistido
     

class Vizualizacao:
     def __init__(self, espec: Gafanhoto, filme: Video):
          self.espec = espec
          self.filme = filme
     def avaliar(self,nota):
          try:
               if isinstance(nota,int) and 0 <= nota <= 10 :
                    return f"{self.espec.nome} sua nota foi {int(nota)}/10!"
               
               elif isinstance(nota,float) or isinstance(nota,int) and 0 <= nota <= 100:
                    return f'{self.espec.nome} sua nota foi {float(nota)}%!'
               
               else:
                    return 'erro ao dar nota'
               
          except:
                    return 'erro ao dar nota'


video = Video(tit='Python Tutorial', view=100, curtidas=50, repr=True)
nyko = Gafanhoto(nome='nyko', idade=25, sexo='M', login='joaopy', totAssistido=20)
viz = Vizualizacao(nyko, video)

print(viz.avaliar(23))
