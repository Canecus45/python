# NON CONSIDERO IL NON DISPONDIBILE
def calcolo_tot(vendite, nome):
    media = 0
    c = 0
    massimo = 0
    minimo = 0
    mMassimo = ""
    mMinimo = ""
    for i, *repa in vendite:
        print(i)
        for reparto in repa:
            if i == nome:
                c += 1
                media += reparto[1][1]
                if massimo < reparto[1][1]:
                    mMassimo = reparto[1][0]
                    massimo = reparto[1][1]
                if minimo > reparto[1][1]:
                    mMinimo = reparto[1][0]
                    minimo = reparto[1][1]

    media = media / c
    return (media, (massimo, mMassimo), (minimo, mMinimo))


vendite = (
    (
        "Elettronica",
        (
            ("Gennaio", 104),
            ("Febbraio", 5000),
            ("Marzo", 70000),
            ("Aprile", 900),
            ("Maggio", 71),
        ),
    ),
    (
        "Cucina",
        (
            ("Gennaio", 80),
            ("Febbraio", 3000),
            ("Marzo", 4000),
            ("Aprile", 0),
            ("Maggio", 400),
        ),
    ),
    (
        "Animali",
        (
            ("Gennaio", 90000),
            ("Febbraio", 89),
            ("Marzo", 8000),
            ("Aprile", 6000),
            ("Maggio", 69),
        ),
    ),
)

nome = input("Inserie il nome del reparto:\n>")

print(calcolo_tot(vendite, nome))
