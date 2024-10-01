class AnimaleDomestico:

    def __init__(self, nome, anni) -> None:
        self.nome = nome
        self.anni = anni

    def mangia(self):
        print(self.nome, " sta mangiando!")

    def dormi(self):
        print(self.nome, " sta dormendo!")


class Cane(AnimaleDomestico):
    def __init__(self, nome, anni, razza) -> None:
        super().__init__(nome, anni)
        self.razza = razza

    def abbaia(self):
        print(self.nome, " sta abbaiando!")


class Gatto(AnimaleDomestico):
    def __init__(self, nome, anni, sesso) -> None:
        super().__init__(nome, anni)
        self.sesso = sesso

    def fusa(self):
        print(self.nome, " sta facendo le fusa")


gatto = Gatto("Palla", 2, "Maschio")
cane = Cane("Charlie", 4, "Maremmano")

gatto.fusa()
gatto.mangia()

cane.dormi()
cane.abbaia()
