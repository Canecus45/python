class RefertoMedico:
    def __init__(self, referti):
        self.referti = referti

    # punto 1
    def popola(self):
        self.referti = [
            ("01/03/2022", 323, 350, "Polistiroli"),
            ("01/03/2022", 183, 150, "Trigliceridi"),
            ("01/05/2023", 163, 150, "Glicemia"),
            ("01/06/2024", 137, 150, "Pressione"),
            ("02/06/2024", 128, 170, "Pressione"),
        ]

    # punto 2
    def vizualizzaReferto(self):
        for i in self.referti:
            print(f"Data: {i[0]}")
            print(f"Parametro: {i[3]}")
            print(f"Valore minore: {i[1]}")
            print(f"Valore maggiore: {i[2]}")
            print(f"Scostamento: {i[2]-i[1]}")
            print("\n")

    # punto 3 9:27
    def contaDiagnosi(self):
        c = 0
        while True:
            if c == self.referti.__len__():
                break
            if c == 0:
                self.referti.vizualizzaReferto()
            c += 1
        print("Numero referti: ", c)

    # punto 4 10:06
    def mediaParametri(self):
        parametri = []
        c = 0
        parametriDop = []
        for i in self.referti:
            if i[3] in parametri:
                parametriDop += i[3]
            else:
                parametri[c] += i[3]
        for i in self.referti:
            if i[3] in parametriDop:
                p += 1

        valoriMin = 0
        valoriMax = 0

        for i in self.referti:
            if i[3] in parametriDop:
                valoriMin += i[1]
                valoriMax += i[2]
        valoriMin = valoriMin / p
        valoriMax = valoriMax / p
        print(f"Valori minimi: {valoriMin}, Valori massimi: {valoriMax}")

    # punto 5
    def rilevamentoScosamento(self):
        scostamento = 0
        scostamenti = 200
        for i in self.referti:
            scostamento = i[2] - i[1]
            if scostamento < scostamenti:
                scostamenti = scostamento

        date = []
        parametro = []
        valore = []
        for i in self.referti:
            scostamento = i[2] - i[1]
            if scostamenti == scostamento:
                valore += i[2]
                date += i[0]
                parametro += i[3]
        print(parametro, ", ", valore, ",", scostamenti, ", ", date)

    # punto 6


class ReportReferti:
    def __init__(self, report) -> None:
        self.report = report

    def aggiungiReferti(self, paziente):
        self.report += ((paziente, RefertoMedico.popola()),)

    # punto 7
    def rimuoviReferti(self, paziente):

        for i in self.report:
            for n in i:
                if n[0] == paziente:
                    report -= i

    # punto 8
    def cercaReferto(self, paziente):
        for i in self.report:
            for n in i:
                if n[0] == paziente:
                    return i
        return -1

    # punto 9
    def visualizzaReferto(self, paziente):
        if self.report.cercaReferto(paziente) == -1:
            print("Non è presente il paziente")
        else:
            for i in self.referti:
                for n in i:
                    print(f"Data: {n[1][0]}")
                    print(f"Parametro: {n[1][3]}")
                    print(f"Valore minore: {n[1][1]}")
                    print(f"Valore maggiore: {n[1][2]}")
                    print(f"Scostamento: {n[1][2]-n[1][1]}")
                    print("\n")


referti = RefertoMedico([])
# 1
referti.popola()
# 2
referti.vizualizzaReferto()
# 3
referti.contaDiagnosi()
# 4
referti.mediaParametri()
# 5
referti.rilevamentoScosamento()
# 6
report = ReportReferti([])
report.aggiungiReferti("gigi")
report.aggiungiReferti("piero")
# 7
report.rimuoviReferti("gigi")
# 8

if report.cercaRefertoReferto("gigi") == -1:
    print("Non trovati referti")
else:
    print("Trovati referti")
if report.cercaRefertoReferto("piero") == -1:
    print("Non trovati referti")
else:
    print("Trovati referti")
# 9
report.visualizzaReferto("ugo")
report.visualizzaReferto("piero")
