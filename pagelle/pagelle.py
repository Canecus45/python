class Pagelle:
    def __init__(self, nome) -> None:
        self.tuplavoti = []
        self.nome = nome

        self.popola()
        self.sommaAssenze()
        self.materieInsuff()
        self.mediaMaterie()
        self.massimoMinimo()

    def popola(self) -> None:
        self.tuplavoti.append(("Italiano", 4.5, 0))
        self.tuplavoti.append(("Matematica", 8, 10))
        self.tuplavoti.append(("Informatica", 2.5, 9))
        self.tuplavoti.append(("Storia", 6, 0))

    def __str__(self) -> str:
        return f"Nome: {self.nome}\nTupla voti: {self.tuplavoti}"

    def sommaAssenze(self) -> None:
        assenze = 0
        for i in self.tuplavoti:
            assenze += i[2]
        print(f"Le ore di assenze totali sono: {assenze}")

    def materieInsuff(self) -> None:
        materie = 0
        for i in self.tuplavoti:
            if i[1] < 6:
                materie += i[1]
        print(f"Le materie sotto sono {materie}")

    def mediaMaterie(self) -> None:
        media = 0
        for i in self.tuplavoti:
            media += i[2]
        media = media / self.tuplavoti.__len__
        print(f"La media totale è {media}")

    def massimoMinimo(self) -> None:
        massimo = 0
        minimo = 11
        materiaMas
        materiaMin
        for i in self.tuplavoti:
            if massimo < i[1]:
                massimo = i[1]
                materiaMas = i[0]
            elif minimo > i[1]:
                minimo = i[1]
                materiaMin = i[0]
        print(
            f"La materia voto più basso {materiaMin} voto {minimo} materia voto più alto {materiaMas} voto {massimo}"
        )


nome = input("Inserire il nome:\n>")
Pagelle(nome)
