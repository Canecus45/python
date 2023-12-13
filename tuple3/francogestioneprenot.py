"""
Un ristorante tiene traccia delle prenotazioni dei tavoli. Per ogni prenotazione, sono
registrati i dettagli seguenti: '("Cliente", "Data prenotazione", "Numero di
persone", "Tavolo")'.

Scivi una serie di funzioni in Python per gestire le prenotazioni

1.Una funzione 'aggiungi_prenotazione' che accetta la lista delle prenotazioni, il nome del
  cliente, la data prenotazione, il nunmero di persone di persone e il numero del tavolo, e
  aggiunge una nuova prenotazione alla lista.
2.Una funzione 'rimuovi_prenotazione' che accetta la lista delle prenotazioni, il nome del
  cliente e la data della prenotazione, e rimuovere la prenotazione corrispondente della lista.
3.Una funzione 'tavoli_disponibili' che accetta la lista delle prenotazioni e una data, e
  restituisce una lista dei tavoli disponibili per quella data. I tavoli disponibili sono quelli che
  non sono stati prenotati per quella data
4.Una funzione 'prenotazione_cliente' che accetta la lista delle prenotazione e il nome di
  restituisce il conto totale delle prenotazioni fatte per quella data.
5.Una fuznione 'conto_totale' che accetta la lista delle prenotazioni e una data, e
  restituisce il conto totale delle prenotazioni fatte per quella data. 

# Inizializza una lista vuota per le prenotazioni
prenotazioni = []

# Esempio di utilizzo delle funzioni
aggiungi_prenotazione(prenotazioni, "Maria", "04-10-2023", 4, 3)
aggiungi_prenotazione(prenotazioni, "Pietro", "04-10-2023", 2, 2)
aggiungi_prenotazione(prenotazioni, "Carlo", "04-10-2023", 5, 5)
print("Tavoli disponibili per il 04-10-2023:", tavoli_disponibili(prenotazioni, "04-10-2023"))
print("Prenotazioni di Maria:", prenotazioni_cliente(prenotazioni, "Maria"))
print("Conto totale per il 04-10-2023:", conto_totale(prenotazioni, "04-10-2023"))
"""


def aggiungi_prenotazione(prenotazioni, nome, giorno, numero, tavolo):
    prenotazioni.append(nome, giorno, numero, tavolo)


def rimuovi_prenotazione(prenotazioni, nome, giorno):
    for i in range(prenotazioni):
        if prenotazioni[i][1] == nome and prenotazioni[i][2] == giorno:
            prenotazioni.pop(i)
            break


def tavoli_disponibili(prenotazioni, giorno):
    prenotati = []
    for i in range(prenotazioni):
        if prenotazioni[i][2] == giorno:
            prenotati.appen(prenotazioni[i][3])
    return prenotati


def conto_totale(prenotazioni, giorno):
    tot = 0
    for i in range(prenotazioni):
        if prenotazioni[i][2] == giorno:
            tot += 1
    return tot


inserimento = 0
prenotazioni = []

while inserimento != 9:
    print("1. Per aggiungere una prenotazione\n")
    print("2. Per riumuovere una prenotazione\n")
    print("3. Per vedere i tavoli disponibili\n")
    print("4. Per vedere le prenotazioni dei clienti\n")
    print("5. Per vendere le prenotazioni fatte in un giorno y\n")
    inserimento = int(input("9. Per interrompere il cicloF\n>"))
    if inserimento == 1:
        nome = input("Inserire il nome:\n>")
        giorno = input("Inserire la data della prenotazione:\n>")
        numero = int(input("Insererire il numero di persone:\n>"))
        tavolo = int(input("Inserire il numero di tavolo"))
        aggiungi_prenotazione(prenotazioni, nome, giorno, numero, tavolo)
    elif inserimento == 2:
        nome = input("Inseire il nome a cui era a carico la prenotazione:\n>")
        giorno = input("Inserire la data a cui era a carico la prenotazione:\n>")
        rimuovi_prenotazione(prenotazioni, nome, giorno)
    elif inserimento == 3:
        giorno = input("Inserire il giorno per cui si vuole vedere le prenotazioni:\n>")
        print(
            f"Prenotazioni per i tavoli del giorno {giorno}: {tavoli_disponibili(prenotazioni, giorno)}"
        )
    elif inserimento == 4:
        # Non ho capito il punto
        print()
    elif inserimento == 5:
        giorno = input("Inserire il giorno per cui si vuole vedere le prenotazioni:\n>")
        print(
            f"Prenotazioni totali per il giorno {giorno}: {conto_totale(prenotazioni,giorno)}"
        )
    else:
        break
