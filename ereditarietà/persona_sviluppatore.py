class Persona:
    def __init__(self, nome, cognome, nascita, residenza) -> None:
        self.nome = nome
        self.cognome = cognome
        self.nascita = nascita
        self.residenza = residenza

    def profilo_personale(self) -> str:
        s = f"nome {self.nome}\ncognome: {self.cognome}\nnascita: {self.nascita}\nresidenza: {self.residenza}"
        return s

    def __repr__(self) -> str:
        s = f"nome: {self.nome}\ncognome: {self.cognome}"
        return s


class Sviluppatore(Persona):
    def __init__(
        self, nome, cognome, nascita, residenza, posizione, paga_annua
    ) -> None:
        super().__init__(nome, cognome, nascita, residenza)
        self.posizione = posizione
        self.paga_annua = paga_annua

    def profilo_impiegato(self) -> str:
        s = f"{super().profilo_personale()}\nposizione: {self.posizione}\npaga annua: {self.paga_annua}"
        return s

    def __repr__(self) -> str:
        s = f"{super().__repr__()}\nposizione: {self.posizione}"


persona_uno = Persona("Mario", "Rossi", 1990, "Via Roma 1")
print(persona_uno)

impiegato_uno = Sviluppatore(
    "Verdi", "Piero", 1994, "Via Milano 1", "Sviluppatore Back End", 60000
)
print(impiegato_uno)

print(persona_uno.profilo_personale())
print(impiegato_uno.profilo_impiegato())
