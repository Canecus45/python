class Persona:
    def __init__(self, nome, cognome, codice_fiscale) -> None:
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale


class Socio(Persona):
    def __init__(self, nome, cognome, codice_fiscale, durata_iscrizione) -> None:
        super().__init__(nome, cognome, codice_fiscale)
        self.durata_iscrizione = durata_iscrizione

    def getDurataIscrizione(self) -> int:
        return self.durata_iscrizione


class Sede:
    def __init__(self, nome, indirizzo, max_soci, max_corsi) -> None:
        self.nome = nome
        self.inidirizzo = indirizzo
        self.max_soci = max_soci
        self.max_corsi = max_corsi
        self.soci = []
        self.corsi = []

    def aggiungi_socio(self, socio) -> None:
        self.soci.append(socio)

    def numero_soci(self) -> int:
        return len(self.soci)

    def aggiungi_corso(self, corso) -> None:
        self.corsi.append(corso)

    def numero_corsi(self) -> int:
        return len(self.corsi)

    def incasso_previsto(self, quota_mensile) -> float:
        return self.soci.numero_soci() * quota_mensile

    def incasso_corsi(self) -> float:
        costo = 0
        for corso in self.corsi:
            costo += corso.getCosto()

        if self.corsi.numero_corsi() == 0:
            print("Non sono presenti corsi attivi")
        else:
            return costo * self.corsi.numero_corsi()


class CorsoGruppo:
    def __init__(self, nome, costo, numero_massimo) -> None:
        self.nome = nome
        self.costo = costo
        self.numero_massimo = numero_massimo
        self.partecipanti = []

    def getCosto(self) -> float:
        return self.costo

    def aggiungi_partecipante(self, socio) -> None:
        self.partecipanti.append(socio)

    def numero_partecipanti(self) -> int:
        return len(self.partecipanti)

    def incasso_previsto(self) -> float:
        return self.numero_partecipanti() * self.costo


class Palestra:
    def __init__(self) -> None:
        self.sedi = []

    def aggiungi_sede(self, sede) -> None:
        self.sedi.append(sede)

    def numero_totale_soci(self) -> int:
        soci = 0
        for i in self.sedi:
            soci += i.numero_soci()
        return soci

    def incasso_totale(self, quota_mensile) -> float:
        mesi = 0
        for sede in self.sedi:
            for socio in sede.soci:
                mesi += socio.getDurataIscrizione()

        if mesi == 0:
            print("Non sono presenti soci")
        else:
            return mesi * quota_mensile

    def aggiungi_corso(self, sede, corso) -> None:
        presente = sede in self.sedi
        if presente:
            sede.aggiungi_corso(corso)
        else:
            print("SEDE NON ESISTENTE")


# 1. Creiamo un'istanza della classe Palestra:
palestra1 = Palestra()

# 2. Creiamo un'istanza della classe Sede:
sede1 = Sede("Palestra City", "Via Roma 1", 500, 10)

# 3. Aggiungiamo la sede alla palestra:
palestra1.aggiungi_sede(sede1)

# 4. Creiamo alcune istanze della classe Persona e della classe Socio:
persona1 = Persona("Mario", "Rossi", "RSSMRA01A01H501X")
socio1 = Socio("Mario", "Rossi", "RSSMRA01A01H501X", 12)
persona2 = Persona("Anna", "Verdi", "VRDNNM02B02H501Y")
socio2 = Socio("Anna", "Verdi", "VRDNNM02B02H501Y", 6)

# 5. Aggiungiamo i soci alla sede:
sede1.aggiungi_socio(socio1)
sede1.aggiungi_socio(socio2)

# 6. Creiamo un'istanza della classe CorsoGruppo:
corso1 = CorsoGruppo("Zumba", 20, 30)

# 7. Aggiungiamo il corso alla sede:
sede1.aggiungi_corso(corso1)

# 8. Aggiungiamo un socio al corso:
corso1.aggiungi_partecipante(socio1)

# 9. Verifichiamo il numero di partecipanti al corso:
print(corso1.numero_partecipanti())

# 10. Verifichiamo l'incasso previsto per il corso:
print(corso1.incasso_previsto())

# 11. Verifichiamo il numero totale di soci della palestra:
print(palestra1.numero_totale_soci())

# 12. Verifichiamol'incasso totale previsto per la palestra:
print(palestra1.incasso_totale(30))

"""
Risultato atteso:
1
20
2
540
"""
