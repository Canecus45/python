class Veicolo:
    def __init__(self, codice, marca, modello, prezzo, annoRevisione) -> None:
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
        self.annoRevisione = annoRevisione

    def scheda_veicolo(self) -> str:
        s = f"Codice: {self.codice} \nMarca: {self.marca} \nModello: {self.modello} \nPrezzo: {self.prezzo} \nAnno di revisione: {self.annoRevisione}"
        return s

    def modifica_scheda(self) -> None:
        scelta = int(
            input(
                "Cosa si vuole modificare?\n1.Codice\n2.Marca\n3.Modello\n4.Prezzo\n5.Anno di revisione\n>"
            )
        )
        if scelta == 1 or scelta == 5:
            modifica = int(input("Inserire modifica:\n>"))
            if scelta == 1:
                self.codice = modifica
            else:
                self.annoRevisione = modifica
        elif scelta == 4:
            modifica = float(input("Inseire modifica:\n>"))
            self.prezzo = modifica
        else:
            modifica = input("Inserire modifica:\n>")
            if scelta == 2:
                self.marca = modifica
            else:
                self.modello = modifica


class Automobile(Veicolo):
    def __init__(
        self, codice, marca, modello, prezzo, annoRevisione, lunghezza, larghezza
    ) -> None:
        super().__init__(codice, marca, modello, prezzo, annoRevisione)
        self.lunghezza = lunghezza
        self.larghezza = larghezza

    def scheda_veicolo(self) -> str:
        s = (
            super().scheda_veicolo()
            + f" \nLunghezza: {self.lunghezza} \nLarghezza: {self.larghezza}"
        )
        return s


class Motociclo(Veicolo):
    def __init__(
        self, codice, marca, modello, prezzo, annoRevisione, tipo, potenza
    ) -> None:
        super().__init__(codice, marca, modello, prezzo, annoRevisione)
        self.tipo = tipo
        self.potenza = potenza

    def scheda_veicolo(self) -> str:
        s = super().scheda_veicolo() + f" \nTipo: {self.tipo} \nPotenza: {self.potenza}"
        return s


class Vendita:
    def __init__(self, codice, data, codiceVenditore) -> None:
        self.codice = codice
        self.data = data
        self.codiceVenditore = codiceVenditore
        self.automobili = []
        self.moticli = []

    def aggiungi_veicolo(self, veicolo) -> None:
        if isinstance(veicolo, Automobile):
            tipo_veicolo = "automobile"
            self.automobili.append(veicolo)
        elif isinstance(veicolo, Motociclo):
            tipo_veicolo = "motociclo"
            self.moticli.append(veicolo)

        print(f"{tipo_veicolo} aggiunto alla vendita {self.codice} del {self.data}")

    def rimuovi_veicolo(self, veicolo) -> None:
        contatore = 0
        if isinstance(veicolo, Automobile):
            contatore = 0
            if veicolo in self.automobili:
                for i in self.automobili:
                    if veicolo.codice == i.codice:
                        self.automobili.pop(contatore)
                        print("Veicolo rimoso")
                    contatore += 1
            else:
                print("Veicolo non presente")
        elif isinstance(veicolo, Motociclo):
            if veicolo in self.moticli:
                for i in self.moticli:
                    if veicolo.codice == i.codice:
                        print("Veicolo rimoso")
                        self.moticli.pop(contatore)
                    contatore += 1
            else:
                print("Veicolo non presente")
        else:
            print("L'oggetto passato non è un istanza ne di Automobile ne di Motociclo")

    def importo_vendita(self) -> None:
        contatore = 0
        totale = 0
        for i in self.automobili:
            contatore += 1
            totale += i.prezzo
        for i in self.moticli:
            contatore += 1
            totale += i.prezzo
        if contatore == 0:
            print(f"Il venditore {self.codiceVenditore} non ha venduto nessun veicolo")
        else:
            print(
                f"Codice venditore: {self.codiceVenditore}\nNumero di veicoli: {contatore}\nPrezzo totale: {totale}"
            )

    def dettaglio_vendita(self):
        # 12 Stampa il dettaglio della vendita e restituisce una lista contenente
        # [somma importi automobili, somma importi motocicli, somma importi totali, provvigione ]
        # e il totale della provvigione spettante al venditore sapendo che:
        # per automobili la provvigione spettante è il 3% del prezzo di vendita
        # per motocicli la provvigione spettante è il 2% del prezzo di vendita
        provvigione = 0
        sommaA = 0
        sommaM = 0
        for i in self.automobili:
            sommaA += i.prezzo
        for i in self.moticli:
            sommaM += i.prezzo

        if sommaA == 0 and sommaM == 0:
            print(f"Il venditore {self.codiceVenditore} non ha venduto nessun veicolo")
        else:
            provvigione += sommaA * 3 / 100
            provvigione += sommaM * 2 / 100
            return [sommaA, sommaM, sommaA + sommaM, provvigione]


class Vendite:
    def __init__(self, nome_negozio, codice_negozio):
        self.nome_negozio = nome_negozio
        self.codice_negozio = codice_negozio
        self.vendite = []

    def aggiungi_vendita(self, vendita):
        if isinstance(vendita, Vendita):
            self.vendite.append(vendita)
        else:
            print("La vendita inserita non è un istanza di Vendita")

    def rimuovi_vendita(self, vendita):
        if vendita in self.vendite:
            contatore = 0
            for i in self.vendite:
                if vendita == i:
                    break
                contatore += 1
            self.vendite.pop(contatore)
            print("Rimozione effettuata correttamente")
        else:
            print("Vendita inesistente")

    def totale_vendite(self):
        totA = 0
        totM = 0
        tot = 0
        supporto = []
        for i in self.vendite:
            supporto = i.dettaglio_vendita()
            totA += supporto[0]
            totM += supporto[1]
            tot += supporto[2]

        return [totA, totM, tot]


scelta = 0

while True:
    print("0. uscita")
    print("1. inserimento veicol")
    print("2. Modifica scheda veicolo")
    print("3. Aggiunta altri veicoli")
    print("4. Aggiunta a vendita tutti i vari veicoli appena creati")
    print("5. Rimossione due volte lo stesso veicolo")
    print("6. Importo totale vendita")
    print("7. Dettaglio vendita")
    print("8. Aggiungi e rimuovi due volte vendite per poi aggiungere di nuovo")
    print("9. Creazione e aggiunta di una nuova vendita")
    print("10. come il punto 6 però per tutte le vendite")
    scelta = int(input(">"))

    if scelta == 0:
        break
    elif scelta == 1:
        a1 = Automobile(1, "Audi", "Audi Q3", 25000, 2015, 4.5, 1.85)
        print(a1.scheda_veicolo())
        pass
    elif scelta == 2:
        a1.modifica_scheda()
        print(a1.scheda_veicolo())
    elif scelta == 3:
        a2 = Automobile(2, "Peugeot", "Peugeot 2008", 18000, 2014, 4.2, 1.75)
        m1 = Motociclo(3, "Gilera", "Gilera Runner 50", 3500, 2016, "Scooter", 1200)
        m2 = Motociclo(4, "Honda", "SW-T 400 - 2013", 4500, 2012, "Super Sport", 1000)
    elif scelta == 4:
        vendita1 = Vendita(1, "01/04/2022", "123")
        vendita1.aggiungi_veicolo(a1)
        vendita1.aggiungi_veicolo(a2)
        vendita1.aggiungi_veicolo(m1)
        vendita1.aggiungi_veicolo(m2)
    elif scelta == 5:
        vendita1.rimuovi_veicolo(m2)
        vendita1.rimuovi_veicolo(m2)
    elif scelta == 6:
        vendita1.importo_vendita()
    elif scelta == 7:
        importi = vendita1.dettaglio_vendita()
        print("--------------------------")
        print(f"\nImporto Automobili= {importi[0]}")
        print(f"\nImporto Motocicli= {importi[1]}")
        print(f"\nImporto Totale= {importi[2]}")
        print(f"\nImporto Provvigione= {importi[3]}")
    elif scelta == 8:
        vendite_negozio = Vendite("Concessionaria Magenta ", 1)
        vendite_negozio.aggiungi_vendita(vendita1)
        vendite_negozio.rimuovi_vendita(vendita1)
        vendite_negozio.rimuovi_vendita(vendita1)
        vendite_negozio.aggiungi_vendita(vendita1)
    elif scelta == 9:
        a3 = Automobile(5, "Renault", "Renault Clio", 12000, 2020, 3.2, 1.55)

        m3 = Motociclo(6, "Honda", "SW-T 500", 5500, 2021, "Sport", 1200)
        vendita2 = Vendita(2, "2/04/2022", "234")
        vendita2.aggiungi_veicolo(a3)
        vendita2.aggiungi_veicolo(m3)

        vendite_negozio.aggiungi_vendita(vendita2)
    elif scelta == 10:
        importiTotali = vendite_negozio.totale_vendite()
        print("--------------------------")
        print(f"\nImporto totale automobili= {importiTotali[0]}")
        print(f"\nImporto totale motocilci= {importiTotali[1]}")
        print(f"\nImporto totale di tutte le vendite= {importiTotali[2]}")
