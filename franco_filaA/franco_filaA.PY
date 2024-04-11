# 4
def stampaSettembre(macchine):
    for n in macchine:
        if n == "AA123BB":
            for k in macchine[n]:
                if k[0] == "settembre":
                    print(n, k)


# 5
def stampaLuglio1(macchine):
    for n in macchine:
        if n == "CD456FF":
            for k in macchine[n]:
                if k[0] == "luglio":
                    print(k[0])
                    print(k[1])
                    print(k[2])


# 6
def stampaLuglio2(macchine):
    for n in macchine:
        if n == "AA123BB":
            for k in macchine[n]:
                if k[0] == "luglio":
                    for v in k[1]:
                        print(v)


# 7
def maxNoleggi(macchine):
    massimo = 0
    targa = ""
    for n in macchine:
        for k in macchine[n]:
            if k[0] == "luglio":
                if massimo < max(k[1]):
                    targa = n
                    massimo = max(k[1])
    print(targa, massimo)


# 8
def sommaKm(macchine):
    km = 0
    for n in macchine:
        for k in macchine[n]:
            km += k[2]
    print(km)


# 9
def maxKm(macchine):
    maxKm = 0
    mese = ""
    for n in macchine:
        if n == "CD456FF":
            for k in macchine[n]:
                if maxKm < k[2]:
                    maxKm = k[2]
                    mese = k[0]
    print(mese, maxKm)


# 1
macchine = {
    "AA123BB": (
        ("giugno", (9, 4, 5, 7), 1293),
        ("luglio", (14, 3, 5, 12), 3231),
        ("agosto", (19, 14, 15, 17), 4020),
        ("settembre", (6, 8, 5, 7), 3928),
    ),
    "AB345CD": (
        ("giugno", (20, 24, 15, 7), 1391),
        ("luglio", (9, 14, 5, 17), 1234),
        ("agosto", (20, 24, 15, 17), 4932),
        ("settembre", (10, 14, 5, 7), 2872),
    ),
    "CD456FF": (
        ("giugno", (10, 14, 5, 7), 2872),
        ("luglio", (9, 14, 15, 7), 3273),
        ("agosto", (20, 14, 6, 6), 3211),
        ("settembre", (10, 14, 5, 7), 2827),
    ),
}
# 2
macchine["ZZ999FG"] = (
    ("giugno", (10, 10, 10, 10), 10000),
    ("luglio", (10, 10, 10, 10), 10000),
    ("agosto", (10, 10, 10, 10), 10000),
    ("settembre", (10, 10, 10, 10), 10000),
)
# 3
macchine["AA123BB"] += (("ottobre", (12, 5, 43, 5), 9812),)
macchine["AB345CD"] += (("ottobre", (8, 12, 4, 19), 3254),)
macchine["CD456FF"] += (("ottobre", (2, 14, 5, 15), 1099),)
macchine["ZZ999FG"] += (("ottobre", (10, 10, 10, 10), 10000),)
# 4
stampaSettembre(macchine)
# 5
stampaLuglio1(macchine)
# 6
stampaLuglio2(macchine)
# 7
maxNoleggi(macchine)
# 8
sommaKm(macchine)
# 9
maxKm(macchine)
