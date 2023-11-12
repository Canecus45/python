"""
# Esercizio 1
Un negozio di alimentari tiene traccia dei prezzi dei suoi prodotti in un periodo di una settimana.
Per ogni prodotto, vengono registrati i prezzi quotidiani. Ogni record è strutturato come segue
("Prodotto","Giorno della settimana", Prezzo).

Scrivi una funzione in Python chiamata prezzo_medio che calcoli il prezzo medio di un prodotto
in un determinato giorno della settiaman. la funzione dovrebbe accettare tre argomenti:
tupla dei prodotti, il nome del prodotto e il giorno della settiamna
la funzione dovrebbe restituire il prezzo medio di quel prodotto nel giorno spercificato.

Versione 2
prodotti=(
    (Mela,
    (("Lunedì",0.9),
    ("Martedì",1.10),
    ("Mercoledì",2.0),
    ("Giovedì",0.3),
    ("Venerdì",0.2)),
    ("fogli protocollo di cini",
    (("Lunedì",1.15),
    ("Martedì",1.10),
    ("Mercoledì",2.0),
    ("Giovedì",3.3),
    ("Venerdì",10.2))
    )

)
"""
def prezzo_medio(prodotti,nome,giorno):
    media=0
    cont=0
    for i in range(len(prodotti)):
        if nome==prodotti[i][0]:
            if giorno==prodotti[i][1]:
                media+=prodotti[i][2]
                cont+=1
        else:
            break
    
    media=media/cont
    return media

prodotti=(
    ("Mela","Lunedì",0.9),
    ("Mela","Martedì",1.10),
    ("Mela","Mercoledì",2.0),
    ("Mela","Giovedì",0.3),
    ("Mela","Venerdì",0.2),
    ("Pippo","Lunedì",10.0),
    ("Pippo","Martedì",1.3),
    ("Pippo","Mercoledì",3.0),
    ("Pippo","Lunedì",0.1),
    ("Pippo","Venerdì",0.9)
)

nome=input("Inserire il nome del prodotto:\n>")
giorno=input("Inserire il giorno:\n>")


media=prezzo_medio(prodotti,nome,giorno)
print(f"La media di {giorno} del prodotto {nome} è {media}")