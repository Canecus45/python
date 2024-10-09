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
    def __init__(self, nome, indirizzo, max_soci) -> None:
        self.nome = nome
        self.inidirizzo = indirizzo
        self.max_soci = max_soci
        self.soci = []

    def aggiungi_socio(self, socio) -> None:
        self.soci.append(socio)

    def numero_soci(self) -> int:
        return len(self.soci)

    def incasso_previsto(self, quota_mensile) -> float:
        return self.soci.numero_soci() * quota_mensile


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


# 1.Creazione di alcuni soci
s1 = Socio("Mario", "Rossi", "RSSMRA01A01F205X", 6)
s2 = Socio("Luca", "Bianchi", "BNCLCU02B01F205X", 12)
s3 = Socio("Anna", "Verdi", "VRDANA03C01F205X", 3)
s4 = Socio("Paola", "Neri", "NRIMPA04D01F205X", 6)

# 2.Creazione di due sedi
sede1 = Sede("Sede A", "Via Roma 1, Milano", 50)
sede2 = Sede("Sede B", "Via Dante 10, Firenze", 30)

# 3.Aggiunta dei soci alle sedi
sede1.aggiungi_socio(s1)
sede1.aggiungi_socio(s2)
sede2.aggiungi_socio(s3)
sede2.aggiungi_socio(s4)

# 4.Creazione della palestra e aggiunta delle sedi
palestra = Palestra()
palestra.aggiungi_sede(sede1)
palestra.aggiungi_sede(sede2)

# 5.Calcolo del numero totale di soci e dell'incasso totale
n_soci_totale = palestra.numero_totale_soci()
incasso_totale = palestra.incasso_totale(50)

# 6.Stampa dei risultati
print("Numero totale di soci:", n_soci_totale)
print("Incasso totale:", incasso_totale)

"""
Il risultato atteso è:
Numero totale di soci: 4
Incasso totale: 1350
"""
