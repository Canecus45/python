def popola(record):
    record = {
        1: ["Via Rossi 23", 3, 55, 2, 110],
        2: ["Via Verdi 32", 4, 65, 5, 260],
        3: ["Via Bianchi 19", 5, 75, 2, 150],
    }
    return record


def aggiunta(codice, record, indirizzo, posti, prezzo, notti, totale):
    record[codice] = [indirizzo, posti, prezzo, notti, totale]


def elimina(codice, record):
    print("Elemento eliminato ", record.pop(codice))
    return record


def mostra(codice, record):
    print(record[codice])


def mostraTutti(record):
    for v, k in record:
        print(v, k)


def modifica(codice, record, indirizzo, posti, prezzo, notti, totale):
    record[codice] = [indirizzo, posti, prezzo, notti, totale]


def incassi(record):
    tot = 0
    for v, *k in record:
        for inc in k:
            tot += inc[4]
    print(f"Il totale è {tot}")


while True:
    print("0) Esci")
    print("1) Popola")
    print("2) Aggiungi")
    print("3) Elimina")
    print("4) Cerca")
    print("5) Mostra tutti")
    print("6) Modifica")
    inserimento = input(int("7) Calcolo totale e massimo\n>"))

    if inserimento == 0:
        break
    elif inserimento == 1:
        record = popola(record)
    elif inserimento == 2:
        chiavi = record.keys
        while codice == chiavi:
            codice = input(int("Inserire il codice dell'appartamento\n>"))
        indirizzo = input("Inserire l'indirizzo\n>")
        posti = input(int("Inserire il numero di posti\n>"))
        prezzo = input(int("Inseriore prezzo \n>"))
        notti = input(int("Inserire il numero di notti\n>"))
        totale = prezzo * notti
        aggiunta(codice, record, indirizzo, posti, prezzo, notti, totale)
    elif inserimento == 3:
        chiavi = record.keys
        while codice != chiavi:
            codice = input(int("Insrire il codice dell'appartamento da eliminare\n>"))
        record = elimina(codice, record)
    elif inserimento == 4:
        chiavi = record.keys
        while codice != chiavi:
            codice = input(int("Insrire il codice dell'appartamento da eliminare\n>"))
        mostra(codice, record)
    elif inserimento == 5:
        mostraTutti(record)
    elif inserimento == 6:
        chiavi = record.keys
        while codice != chiavi:
            codice = input(int("Inserire il codice dell'appartamento\n>"))
        indirizzo = input("Inserire l'indirizzo\n>")
        posti = input(int("Inserire il numero di posti\n>"))
        prezzo = input(int("Inseriore prezzo \n>"))
        notti = input(int("Inserire il numero di notti\n>"))
        totale = prezzo * notti
        modifica(codice, record, indirizzo, posti, prezzo, notti, totale)
    else:
        incassi(record)
