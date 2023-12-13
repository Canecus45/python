def analizza_consumi_energetici(citta, risorsa):
    return 4

tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        ("marzo",("elettrico",900))
        ("marzo",("gas",130))
        ("aprile",("elettrico",300))
        ("aprile",("gas",120))
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo",("elettrico",200))
        ("marzo",("gas",100))
        ("aprile",("elettrico",400))
        ("aprile",("gas",120))
    ]),
    ("Cascina Croce", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo",("elettrico",400))
        ("marzo",("gas",300))
        ("aprile",("elettrico",120))
        ("aprile",("gas",101))
    ])
)

risultato_analisi = analizza_consumi_energetici("Milano", "elettrico")

print(risultato_analisi)