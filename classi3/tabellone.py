class Pagelle:
    def __init__(self, nome) -> None:
        self.pagella1 = []
        self.pagella2 = []
        self.nome = nome

    def popola(self):
        self.pagella1.append(("ITALIANO", 8, 5))
        self.pagella1.append(("STORIA", 8, 4))
        self.pagella1.append(("MATEMATICA", 10, 3))
        self.pagella1.append(("LINGUA INGLESE", 9, 0))
        self.pagella1.append(("TELECOMUNICAZIONI", 10, 7))
        self.pagella1.append(("INFORMATICA", 5, 0))
        self.pagella1.append(("SISTEMI E RETI", 5, 0))
        self.pagella1.append(("TECN. PROG. SIST. I.", 4, 0))
        self.pagella1.append(("SCIENZE MOTORIE E SP", 6, 0))

        self.pagella2.append(("ITALIANO", 8, 5))
        self.pagella2.append(("STORIA", 8, 4))
        self.pagella2.append(("MATEMATICA", 10, 3))
        self.pagella2.append(("LINGUA INGLESE", 9, 0))
        self.pagella2.append(("TELECOMUNICAZIONI", 10, 7))
        self.pagella2.append(("INFORMATICA", 5, 0))
        self.pagella2.append(("SISTEMI E RETI", 5, 0))
        self.pagella2.append(("TECN. PROG. SIST. I.", 4, 0))
        self.pagella2.append(("SCIENZE MOTORIE E SP", 6, 0))


# Completare i metodi che al momento sono vuoti(pass)
class Tabellone:
    def __init__(self) -> None:
        pass

    def push(self, pagella):
        pass

    def pop(self, studente):
        pass

    def cercaPagella(self, studente):
        pass

    def __repr__(self):
        pass


# Codice di esempio per l'output
tabellone = Tabellone()
pagella1 = Pagella("NOME_1")
pagella1.popola()
tabellone.push(pagella1)
pagella2 = Pagella("NOME_2")
pagella2.popola()
tabellone.push(pagella2)
print(tabellone)  # esegue il metodo __repr__(self)
