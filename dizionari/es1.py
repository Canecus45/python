voti={}

while True:
    nChiave=input("Inserire la materia (se si inserisce fine il ciclo finisce): ")
    if nChiave=="fine":
        break
    nVoto=int(input(f"Inserire il voto di {nChiave}: "))    
    voti[nChiave]=nVoto

cont=0

for materia in voti:
    print(f"-{materia}: {voti[materia]}")
    cont+=1

media=0

for materia in voti:
    media+=voti[materia]

media=media/cont
print(f"La media è {media}")