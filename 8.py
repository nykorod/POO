class Lutador:
    def __init__(self, nom, nac, ida, alt, pes, vit=0, emp=0, der=0):
        self.nome = nom
        self.nacionalidade = nac
        self.idade = ida
        self.altura = alt
        self.peso = pes
        self.vitorias = vit
        self.empates = emp
        self.derrotas = der
        self.categoria = self.definir_categoria()

    def definir_categoria(self):
        if self.peso <= 52.2:
            return 'invalido'
        elif self.peso <= 70.3:
            return 'leve'
        elif self.peso <= 83.9:
            return 'medio'
        elif self.peso <= 120.2:
            return 'pesado'
        else:
            return 'invalido'

    def apresentacao(self) -> None:
        print(self.__str__())

    def status(self) -> None:
        print(self.nome, self.altura, self.categoria)

    def ganhar(self) -> None:
        self.vitorias += 1

    def empatar(self) -> None:
        self.empates += 1

    def perder(self) -> None:
        self.derrotas += 1

    def __str__(self) -> str:
        return (f"Nome: {self.nome}, Nacionalidade: {self.nacionalidade}, Idade: {self.idade}, "
                f"Altura: {self.altura}, Peso: {self.peso}, Categoria: {self.categoria}, "
                f"Vitórias: {self.vitorias}, Empates: {self.empates}, Derrotas: {self.derrotas}")


class Luta:
    def __init__(self, l1: Lutador, l2: Lutador):
        if not isinstance(l1, Lutador) or not isinstance(l2, Lutador):
            raise TypeError("Os parâmetros l1 e l2 devem ser instâncias da classe Lutador.")
        self.l1 = l1
        self.l2 = l2

    def aprovar(self) -> bool:
        """Aprova a luta se os lutadores têm a mesma categoria e não são o mesmo lutador."""
        if self.l1.categoria == self.l2.categoria and self.l1 != self.l2:
            return True
        else:
            return False

    def lutar(self) -> str:
        """Realiza a luta e retorna o resultado."""
        from random import randint
        if self.aprovar():
            self.l1.apresentacao()
            self.l2.apresentacao()
            resultado = randint(1, 3)
            if resultado == 1:
                self.l1.ganhar()
                self.l2.perder()
                return f'{self.l1.nome} ganhou'
            elif resultado == 2:
                self.l2.ganhar()
                self.l1.perder()
                return f'{self.l2.nome} ganhou'
            else:
                self.l1.empatar()
                self.l2.empatar()
                return 'empate'
        else:
            return 'Luta não aprovada'

# Exemplo de uso
l1 = Lutador('Nyko', 'Brasil', 17, 1.85, 100.5, 3, 4, 5)
l2 = Lutador('Fer', 'Brasil', 20, 1.45, 100, 3, 4, 5)

luta = Luta(l1, l2)
print(luta.lutar())
