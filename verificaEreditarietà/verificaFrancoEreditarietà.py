class Articolo:
    # 1 Implementa il costruttore
    def __init__(self, titolo, prezzo_giornaliero) -> None:
        self.titolo = titolo
        self.prezzo_giornaliero = prezzo_giornaliero

    def scheda_articolo(self) -> str:
        return f"Titolo: {self.titolo}, prezzo giornaliero: {self.prezzo_giornaliero}"

    def modifica_scheda(self) -> None:
        modifica = int(input("1. Titolo\n2.Prezzo giornaliero"))
        if modifica == 1:
            titolo = input("Inserire il nuovo titolo\n>")
            self.titolo = titolo
        elif modifica == 2:
            prezzo_giornaliero = float(input("Inserire il prezzo giornaliero:\n>"))
            self.prezzo_giornaliero = prezzo_giornaliero


class Libro(Articolo):
    def __init__(self, titolo, prezzo_giornaliero, autore) -> None:
        # 4 Implementa il costruttore
        super().__init__(titolo, prezzo_giornaliero)
        self.autore = autore

    def scheda_articolo(self) -> str:
        # 5 Ritorna una stringa contenente gli attributi del libro
        return f"{super().scheda_articolo()}, autore: {self.autore}"

    def modifica_scheda(self) -> None:
        # 6 Permette di modificare gli attributi del libro
        modifica = int(input("1. Titolo\n2.Prezzo giornaliero\n3.Autore\n>"))
        if modifica == 1:
            titolo = input("Inserire il nuovo titolo\n>")
            self.titolo = titolo
        elif modifica == 2:
            prezzo_giornaliero = float(input("Inserire il prezzo giornaliero:\n>"))
            self.prezzo_giornaliero = prezzo_giornaliero
        else:
            autore = input("Inserire l'autore:\n>")
            self.autore = autore


class DVD(Articolo):
    def __init__(self, titolo, prezzo_giornaliero, regista) -> None:
        # 7 Implementa il costruttore
        super().__init__(titolo, prezzo_giornaliero)
        self.regista = regista

    def scheda_articolo(self) -> str:
        # 8 Ritorna una stringa contenente gli attributi del DVD
        return f"{super().scheda_articolo()}, regista: {self.regista}"

    def modifica_scheda(self) -> None:
        # 9 Permette di modificare gli attributi del DVD
        modifica = int(input("1. Titolo\n2.Prezzo giornaliero\n3.Regista\n>"))
        if modifica == 1:
            titolo = input("Inserire il nuovo titolo\n>")
            self.titolo = titolo
        elif modifica == 2:
            prezzo_giornaliero = float(input("Inserire il prezzo giornaliero:\n>"))
            self.prezzo_giornaliero = prezzo_giornaliero
        else:
            regista = input("Inserire il regista:\n>")
            self.regista = regista


class Prenotazione:
    def __init__(self) -> None:
        self.articoli = []

    # 10 Aggiunge una tupla alla lista di articoli
    def aggiungi_articolo(self, articolo, quantita, giorni) -> None:
        tupla = (articolo, quantita, giorni)
        self.articoli.append(tupla)

    # 11 - Per una prenotazione: a.1) il numero di articoli prenotati e a.2) l'importo totale senza distinguere il tipo di articolo.
    # Restituisce una stringa con numero di articoli e totale
    def totale_prenotazione(self) -> str:
        numeroArticoli = len(self.articoli)
        totale_prezzo = 0
        for tupla in self.articoli:
            totale_prezzo += tupla[0].prezzo_giornaliero
            totale_prezzo += tupla[2] * totale_prezzo
            totale_prezzo += tupla[1] * totale_prezzo

        return (
            f"Numero articoli prenotati:{numeroArticoli}, prezzo totale:{totale_prezzo}"
        )

    # 12 - Per una prenotazione: b.1) il dettaglio degli articoli, b.2) l'importo dei libri, b.3) l'importo dei dvd, b.4) l'importo totale.
    # stampa una stringa con il totale e i totali parziali per libri e dvd
    def dettaglio_prenotazione(self) -> float:
        totale_libro = 0
        totale_dvd = 0
        for tupla in self.articoli:
            if isinstance(tupla[0], Libro):
                print(tupla[0].scheda_articolo())
                totale_libro += tupla[0].prezzo_giornaliero
                totale_libro += tupla[2] * totale_libro
                totale_libro += tupla[1] * totale_libro
            elif isinstance(tupla[0], DVD):
                print(tupla[0].scheda_articolo())
                totale_dvd += tupla[0].prezzo_giornaliero
                totale_dvd += tupla[2] * totale_dvd
                totale_dvd += tupla[1] * totale_dvd
        print(
            f"totale prenotazione: {totale_libro+totale_dvd} di cui per i libri {totale_libro}€ mentre per i dvd {totale_dvd}€"
        )
        return (totale_libro, totale_dvd)


class Biblioteca:
    def __init__(self) -> None:
        self.prenotazioni = []

    # 13 implementa il metodo
    def aggiungi_prenotazione(self, prenotazione) -> None:
        if isinstance(prenotazione, Prenotazione):
            self.prenotazioni.append(prenotazione)
        else:
            print("Prenotazione non valida")

    # 14 - Per tutte le prenotazioni della biblioteca c.1)il dettaglio degli articoli, c.2) l'importo dei libri, c.3) l'importo dei dvd, c.4) l'importo totale..
    # Restituisce una stringa con importo tatola biblioteca, importo libri e importo dvd
    def dettaglio_prenotazioni(self) -> str:
        totale_libro = 0
        totale_DVD = 0
        lista_totali = []
        contatore = 0
        for articoli in self.prenotazioni:
            print("\nDettaglio prenotazione:\n")
            lista_totali.append(articoli.dettaglio_prenotazione())
            totale_libro += lista_totali[contatore][0]
            totale_DVD += lista_totali[contatore][1]
            contatore += 1

        return f"\nImporto totale biblioteca: {totale_libro+totale_DVD}, Importo per i Libri {totale_libro}€, Importo per i DVD {totale_DVD}€"


# Creazione degli oggetti libro e dvd
libro1 = Libro("Il nome della rosa", 2, "Umberto Eco")
libro2 = Libro("1984", 4, "George Orwell")
libro3 = Libro("Python", 4, "Autori vari")
dvd1 = DVD("Il Padrino", 3, "Francis Ford Coppola")
dvd2 = DVD("La vita è bella", 3, "Roberto Benigni")
dvd3 = DVD("Pulp fiction", 3, "Quentin Tarantino")

# NB. ANCHE SE NON INDICATI NELL'OUTPUT DI ESEMPIO
# Testare anche i metodi scheda_articolo e modifica_scheda
print(libro1.scheda_articolo())
libro1.modifica_scheda()
print(libro1.scheda_articolo())
print(dvd1.scheda_articolo())
dvd1.modifica_scheda()
print(dvd1.scheda_articolo())


prenotazione1 = Prenotazione()
prenotazione1.aggiungi_articolo(libro1, 2, 10)
prenotazione1.aggiungi_articolo(dvd1, 1, 3)
print("\n1. Importo totale per la prenotazione 1:")
print(prenotazione1.totale_prenotazione())
print(
    "\n2. Dettaglio degli articoli, importo totale, importo dei libri, importo dei dvd per la prenotazione 1:"
)
prenotazione1.dettaglio_prenotazione()


prenotazione2 = Prenotazione()
prenotazione2.aggiungi_articolo(libro2, 1, 7)
prenotazione2.aggiungi_articolo(dvd2, 1, 7)

prenotazione3 = Prenotazione()
prenotazione3.aggiungi_articolo(dvd3, 2, 7)
prenotazione3.aggiungi_articolo(libro3, 2, 8)

biblioteca = Biblioteca()
biblioteca.aggiungi_prenotazione(prenotazione1)
biblioteca.aggiungi_prenotazione(prenotazione2)
biblioteca.aggiungi_prenotazione(prenotazione3)
print(
    "\n3. Dettaglio degli articoli, importo totale, importo dei libri, importo dei dvd per tutte le prenotazioni:"
)
print(biblioteca.dettaglio_prenotazioni())
