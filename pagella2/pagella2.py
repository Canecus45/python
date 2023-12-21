# 1 Richiesta

pagella = {
    "Simone Ciniltani": [
        ("Matematica", (7, 2), (8, 1)),
        ("Italiano", (6, 3), (4, 2)),
        ("Inglese", (6, 1), (7, 0)),
        ("Geografia", (3, 10), (2, 8)),
    ],
    "Emanuele Paludetti": [
        ("Matematica", (7, 4), (7, 1)),
        ("Italiano", (8, 5), (5, 8)),
        ("Inglese", (6, 1), (7, 0)),
        ("Geografia", (3, 10), (2, 8)),
    ],
}

# 2 Richiesta

alberto = [
    ("Matematica", (10, 0), (10, 0)),
    ("Italiano", (10, 0), (10, 0)),
    ("Inglese", (10, 0), (0, 0)),
    ("Geografia", (10, 0), (10, 0)),
]

pagella["Albert Einstein"] = alberto

# 3 Richiesta

pagella["Simone Ciniltani"].append(("Fisica", (6, 3), (8, 0)))
pagella["Emanuele Paludetti"].append(("Fisica", (8, 5), (7, 2)))
pagella["Albert Einstein"].append(("Fisica", (10, 0), (10, 0)))


# 4 Richiesta
studente1 = input(
    "Inserire lo studente di cui si vuole sapere la pagella di matematica del primo quadrimestre:\n>"
)

for s1 in pagella[studente1]:
    if s1[0] == "Matematica":
        print(s1[1])

# 5 Richiesta

studente1 = input("Inserire lo studente:\n>")
materia1 = input("Inserire la materia:\n>")


for s1 in pagella[studente1]:
    if s1[0] == materia1:
        print(s1[2])

# 6 Richiesta

studente1 = input("Inserire lo studente:\n>")

mas=0


for chiave in pagella.keys():
    if(chiave==studente1):
        for materia, *voti in pagella(studente1):
            for (v1,a1),(v2,a2)in voti:
                if(mas<a1+a2):
                    ass=materia
                    mas=a1+a2

print(f"La materia in cui ha fatto più assenze {studente1} è {mas}")
# 7

studente1 = input("Inserire lo studente:\n>")

mas=100

for chiave in pagella.keys():
    if(chiave==studente1):
        for materia, *voti in pagella(studente1):
            for (v1,a1),(v2,a2)in voti:
                if(mas > v2):
                    mas=v2
mat=[]
for chiave in pagella.keys():
    if(chiave==studente1):
        for materia, *voti in pagella(studente1):
            for (v1,a1),(v2,a2)in voti:
                if(mas == v2):
                    mat.append(materia)

print(f"La materia col voto più basso è {mat}")

# 8

studente1 = input("Inserire lo studente:\n>")

for chiave in pagella.keys():
    if(chiave==studente1):
        for materia, *voti in pagella(studente1):
            for (v1,a1),(v2,a2)in voti:
                if(mas < v1):
                    mas=v1

for chiave in pagella.keys():
    if(chiave==studente1):
        for materia, *voti in pagella(studente1):
            for (v1,a1),(v2,a2)in voti:
                if(mas < v2):
                    mas=v2
mat=[]
periodo=[]
for chiave in pagella.keys():
    if(chiave==studente1):
        for materia, *voti in pagella(studente1):
            for (v1,a1),(v2,a2)in voti:
                if(mas == v1):
                    mat.append(materia)
                    periodo.append("Primo quadrimestre")
                if(mas == v2):
                    mat.append(materia)
                    periodo.append("Secondo quadrimestre")

print(f"Il voto più alto è stato {mas} in {mat} {periodo}")

# 9
cont=0
studente1 = input("Inserire lo studente:\n>")
for chiave in pagella.keys():
    if(chiave==studente1):
        for materia, *voti in pagella(studente1):
            for (v1,a1),(v2,a2)in voti:
                mas+=v1
                cont+=1
mas=mas/cont

print(f"La media è {mas}")

# 10

for chiave in pagella.keys():
    if(chiave==studente1):
        for materia, *voti in pagella:
            for (v1,a1),(v2,a2)in voti:
                mas+=v1+v2
                cont+=1

mas=mas/cont
print(f"La media totale è {mas}")