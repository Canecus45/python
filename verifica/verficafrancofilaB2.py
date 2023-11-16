def media_globale(tupla_ploviometrica, anno):
    media = 0
    contatore = 0
    for c, *tempo in tupla_pluviometrica:
        for i in tempo:
            if i[0] == anno:
                media += i[1][1]
                contatore += 1
    media = media / contatore
    return media


def pioggia(tupla, nome, mese):
    media =0
    contatore=0
    for i in tupla:
        if i[0][1] == nome:
            if i[1][1][0] == mese:
                media+= i[1][1][1] 
                contatore +=1
    media=media/contatore
    return media


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
tupla_pluviometrica = (
    (("Vittuone", "Milano"), (2022, ("gennaio", 20))),
    (("Vittuone", "Milano"), (2023, ("marzo", 80))),
    (("Vittuone", "Milano"), (2023, ("aprile", 60))),
    (("Vittuone", "Milano"), (2023, ("maggio", 80))),
    (("Vittuone", "Milano"), (2023, ("luglio", 30))),
    (("Vittuone", "Milano"), (2023, ("agosto", 20))),
    (("Varenna", "Lecco"), (2023, ("luglio", 150))),
    (("Morbegno", "Sondrio"), (2023, ("luglio", 165))),
)
while True:
    print("1. Media globale")
    print("2. Media di una città")
    print("3. Pioggia massima della provincia di Milano")
    print("4. Pioggia minima nel mese")
    inserimento = int(input("9. Per interrompere il cicloF\n>"))
    if inserimento == 1:
        print(media_globale(tupla_pluviometrica, 2023))
    elif inserimento == 2:
        nome = input("Inseire il nome della provincia:\n>")
        mese=input("Inserire il mese di cui si vuole rilevare:\n>")
        print(pioggia(nome,mese))
    elif inserimento == 3:
        giorno = input("Inserire il giorno per cui si vuole vedere le prenotazioni:\n>")
    elif inserimento == 4:
        # Non ho capito il punto
        print()
    elif inserimento == 5:
        break
