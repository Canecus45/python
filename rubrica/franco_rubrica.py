def nuovoCont(rubrica, chiave, numero, indirizzo, mail):
    rubrica[chiave] = numero, indirizzo, mail


def visualizzaList():
    return


def modContatto():
    return


def cancellaConttato():
    return


def recerca():
    return


rubrica = {
    "Giuseppe Gullo": [3393527822, "Indirizzo 1", "ggullo@mail.it"],
    "Antonio Barbera": [3393228442, "Indirizzo 2", "abarbera@mail.it"],
    "Nicola Spina": [3383522812, "Indirizzo 3", "nspina@mail.it"],
}

inserimento = 0
while inserimento != 9:
    print("1. Popola la rubrica")
    print("2. Aggiungi nuovo contatto")
    print("3. Elimina contatto")
    print("4. Mostra dati contatto")
    print("5. Mostra dati di tutti i contatti")
    print("6. Modifica i dati di un contatto")
    inserimento = input(int("9.Esci dal ciclo:\n>"))
    if inserimento == 1:
        nome = input("Inserire il nome:\n>")
        cognome = input("Inserire il cognome:\n>")
        while True:
            numero = input(int("Inserire il numero di telefono:\n>"))
            if numero >= 100000000 and numero <= 999999999:
                break
        indirizzo = input("Inserire l'indirizzo:\n>")
        while True:
            mail = input("Inserire la mail:\n>")
            if "@" in mail:
                break
        chiave = nome + " " + cognome
        if chiave != rubrica.keys:
            nuovoCont(rubrica, chiave, numero, indirizzo, mail)
        else:
            print("Persona già presente")
    elif inserimento==2:
        
