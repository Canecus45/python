class Cane:
    def __init__(self, nome, anni, razza) -> None:
        self.nome = nome
        self.anni = anni
        self.razza = razza

    def mangia(self) -> None:
        print(f"{self.nome} sta mangiando!")

    def dormi(self) -> None:
        print(f"{self.nome} sta dormendo!")

    def abbia(self) -> None:
        print(f"{self.nome} sta abbiando!")


class Gatto:
    def __init__(self, nome, anni) -> None:
        self.nome = nome
        self.anni = anni

    def mangia(self) -> None:
        print(f"{self.nome} sta mangiando!")

    def dormi(self) -> None:
        print(f"{self.nome} sta dormendo!")

    def fusa(self) -> None:
        print(f"{self.nome} sta facendo le fusa!")
