class Persona:
    def __init__(self, nome, cognome, età, residenza) -> None:
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza

    def scheda_personale(self) -> str:
        s = f"nome: {self.nome}\ncognome: {self.cognome}\netà:{self.età}\nresidenza:{self.residenza}"
        return s

    def modifica_scheda(self, modifica, tipo_modifica) -> None:
        if tipo_modifica == "nome":
            self.nome = modifica
        elif tipo_modifica == "cognome":
            self.cognome = modifica
        elif tipo_modifica == "età":
            self.età = modifica
        else:
            self.residenza = modifica


class Studente(Persona):
    profilo = "Studente"

    def __init__(self, nome, cognome, età, residenza, corso_di_studio) -> None:
        super().__init__(nome, cognome, età, residenza)
        if corso_di_studio == None:
            self.corso_di_studio = corso_di_studio
        else:
            self.corso_di_studio = None

    def scheda_personale(self) -> str:
        s = f"{super().scheda_personale()}\ncorso di studio: {self.corso_di_studio}"
        return s

    def cambio_corso(self, corso) -> None:
        self.corso_di_studio = corso


class Insegnante(Persona):
    profilo = "Insegnante"

    def __init__(self, nome, cognome, età, residenza, materie=None) -> None:
        super().__init__(nome, cognome, età, residenza)
        self.materie = materie

    def scheda_personale(self) -> str:
        s = f"{super().scheda_personale()}\nmaterie: {self.materie}"

    def aggiungi_materia(self, nuova) -> None:
        self.materie.append(nuova)


class Residenza:
    profilo = "Casa dello studente"

    def __init__(self, nome, indirizzo, capienza) -> None:
        self.nome = nome
        self.indirizzo = indirizzo
        self.capienza = capienza
        self.studenti = []
        self.insegnanti = []
        pass

    def aggiungi_studente(self, studente) -> None:
        self.studenti.append(studente)

    def rimuovi_studente(self, studente) -> None:
        self.studenti.pop(studente)

    def elenco_studenti(self) -> str:
        return self.studenti

    def aggiungi_insegnante(self, insegnante) -> None:
        self.insegnanti.append(insegnante)

    def rimuovi_insegnante(self, insegnante) -> None:
        self.insegnanti.pop(insegnante)

    def elenco_insegnanti(self) -> str:
        return self.insegnanti

    def __repr__(self) -> str:
        s = f"\nnome: {self.nome}\nindirizzo: {self.indirizzo}\ncapienza: {self.capienza}"
        return s


class Catena:
    def __init__(self) -> None:
        self.residenze = []

    def aggiungi_residenza(self, residenza) -> None:
        self.residenze.append(residenza)

    def rimuovi_residenza(self, residenza) -> None:
        self.residenze.pop(residenza)

    def elenco_residenza(self) -> None:
        for i, j in enumerate(self.residenze):
            print(f"\nstudente: {i+1}")
            print(j.__repr__())


studente_uno = Studente("Marco", "Verdi", 24, "Casa Dello Studente")
insegnante_uno = Insegnante("Mario", "Rossi", 33, "Viale Roma 32")
print(studente_uno.scheda_personale())
print(insegnante_uno.scheda_personale())

studente_due = Studente(
    "Mirta", "Gialli", 24, "Casa Della Studentessa", "Corso informatica 1"
)
insegnante_due = Insegnante("Maria", "Rosa", 33, "Viale Roma 62", ["sistemi", "tpsi"])

print(studente_due.scheda_personale())

print(insegnante_due.scheda_personale())

insegnante_due.aggiungi_materia("Informatica")

print(insegnante_due.scheda_personale())

studente_due.cambio_corso("Informatica")

print(studente_due.scheda_personale())

casa = Residenza("Casa 1", "Indirizzo 1", 100)
casa.aggiungi_studente(studente_uno)
casa.aggiungi_studente(studente_due)

stud = casa.elenco_studenti()
for i, s in enumerate(stud):
    print(f"Studente: {i+1}")
    print(s.scheda_personale())
