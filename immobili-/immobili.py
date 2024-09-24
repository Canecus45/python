class Immobile:
    def __init__(
        self, codice, mq, tipologia, indirizzo, città, prezzo, venduto
    ) -> None:
        self.codice = codice
        self.mq = mq
        self.tipologia = tipologia
        self.indirizzo = indirizzo
        self.città = città
        self.prezzo = prezzo
        self.venduto = False

    # converzione stringa
    def __str__(self) -> str:
        s = f"""
            Codice: {self.codice}
            Metri quadri: {self.mq}
            Tipologia: {self.tipologia}
            Indirizzo: {self.indirizzo}
            Città: {self.città}
            Prezzo: {self.prezzo}
            Veduto: {self.venduto}
        """
        return s

    def setVendita(self, venduto) -> None:
        self.venduto = venduto

    def getCodice(self) -> int:
        return self.codice

    def setPrezzo(self, prezzo) -> None:
        self.prezzo = prezzo

    def getTipologia(self) -> str:
        return self.tipologia

    def getPrezzo(self) -> int:
        return self.prezzo


# parte 3
class Agenzia:
    def __init__(self) -> None:
        self.immobile = []

    def add(self, immobile) -> None:
        self.immobile.append(immobile)

    def vendita(self, codice) -> bool:
        trovato = False
        for i in self.immobile:
            if i.getCodice == codice:
                i.setVendita(True)
                trovato = True
                return trovato
        return trovato

    def prezzo(self, codice, prezzo) -> bool:
        trovato = False
        for i in self.immobile:
            if i.getCodice == codice:
                self.i.setPrezzo(prezzo)
                trovato = True
                return trovato
        return trovato

    def tipologia(self, tipologiaVoluta) -> None:
        for i in self.immobile:
            if tipologiaVoluta == i.getTipologia():
                print(str(i))

    def visualizza(self, codice) -> bool:
        trovato = False
        for i in self.immobile:
            if i.getCodice == codice:
                print(i)
                trovato = True
        return trovato

    def visualizzaTutti(self) -> None:
        for i in self.immobile:
            print(i)

    def prezzoTotale(self) -> float:
        prezzo = 0.0
        for i in self.immobile:
            if i.getPrezzo():
                prezzo += i.getPrezzo()

        return prezzo

    def prezzoTipologia(self, tipologia) -> float:
        prezzo = 0.0
        for i in self.immobile:
            if i.getTipologia() == tipologia:
                prezzo += i.getPrezzo()
        return prezzo


# prima modalità
immobile1 = Immobile(32, 1000, "Trilocale", "Via Bernardi", "Magenta", 2000, True)
print(str(immobile1))

"""
codice = int(input(("Isnerire il codice: ")))
mq = int(input("inserisci i mq (es. 90 :"))
tipo = input("inserisci la tipologia: ")
indirizzo = input("inserisci l'indirizzo: ")
citta = input("inserisci la città: ")
prezzo = int(input("inserisci il prezzo: "))
# non chiedo se è veduto perchè è a priori false
immobile2 = Immobili(codice, mq, tipo, indirizzo, citta, prezzo)
print(immobile2)
"""

# seconda modalità
immobile2 = Immobile(100, 3000, "Quarilocale", "Via Trice", "Bergamo", 7000, True)
immobile3 = Immobile(104, 400, "Bilocale", "Via Cossemo Bava", "Caldara", 800, True)

immobili = [immobile1, immobile2, immobile3]
"""
giri=int(input("Inserire il numero di oggetti che si vogliono inserire: "))

for i in giri:
    codice = int(input(("Isnerire il codice: ")))
    mq = int(input("inserisci i mq (es. 90 :"))
    tipo = input("inserisci la tipologia: ")
    indirizzo = input("inserisci l'indirizzo: ")
    citta = input("inserisci la città: ")
    prezzo = int(input("inserisci il prezzo: "))
    Immobilex=Immobile(codice,mq,tipo,indirizzo,citta,prezzo)
    Immobili.append(Immobilex)
    """

for i in immobili:
    print(str(i))

# parte tre
# punto 1
agenzia = Agenzia(immobile1)
agenzia.add(immobile2)
agenzia.add(immobile3)
# punto 2
codice = int(input("Inserie il codice dell'immobile che si vuole comprare: "))
trovato = agenzia.vendita(codice)
if trovato:
    print("Immobile trovato")
else:
    print("Immobile non trovato")

# punto 3
codice = int(
    input("Inserie il codice dell'immobile di cui si vule modificare il prezzo\n>")
)
prezzo = int(input("Inserire il nuovo prezzo:\n>"))

trovato = agenzia.prezzo(codice, prezzo)

if trovato:
    print("Prezzo di vendita cambaito")
else:
    print("Immobile non trovato")
# punto 4
tipologiaDesiderata = input("Inserire la tipologia di immobile desiderato:\n>")

agenzia.tipologia(tipologiaDesiderata)

# punto 5
codice = int(input("Inserie il codice dell'immobile che si vuole visualizzare: "))

trovato = agenzia.visualizza(codice)

if not trovato:
    print("Immobile non trovato")
# punto 6
agenzia.visualizzaTutti()

# punto 7

prezzo = agenzia.prezzoTotale()
print(f"La somma dei prezzi è: {prezzo}")

# punto 8
tipologia = input("Inserire la tipologia di immobile: ")
prezzo = agenzia.prezzoTipologia(tipologia)
if prezzo == 0:
    print("Questa tipologia al momento non è presente tra gli immobili in vendita")
else:
    print(f"Il prezzo medio per questa tipologia è:{prezzo}")
