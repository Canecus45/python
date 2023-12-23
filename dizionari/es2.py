voti={}
nwVoti=[]

while True:
    nuStudenti=int(input("Inserire il numero di studenti:\n>"))
    for i in nuStudenti:
        nwStudente=input("Inserire il nome dello studente:\n>")
        nwVoti.append(int(input("Inserire il voto di Matematica:\n>")))
        nwVoti.append(int(input("Inserire il voto di Fisica:\n>")))
        nwVoti.append(int(input("Inserire il voto di Chimica:\n>")))
        voti[nwStudente]=nwVoti
        nwVoti=[]

studente=input("Inserire lo studente di cui si vuole sapere la media:\n>")

media=0

for nome in voti:
    if(nome == studente):
        media+=voti[nome]

media=media/3

print(f"La media di voti {stuende} è {round(media, 3)}")