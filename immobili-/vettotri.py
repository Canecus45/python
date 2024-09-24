import math


class Vector:

    def __init__(self, values) -> None:
        self.values = values

    def __repr__(self) -> None:
        print(self.values)

    def sum(self) -> int:
        t = 0
        for i in self.values:
            t += i
        return t

    def __getitem__(self, i) -> int:
        for j in self.values:
            if j == i:
                return j

    def __eq__(self, vector) -> bool:
        leng1 = len(self.values)
        print(leng1)
        leng2 = 0
        for i in vector:
            leng2 += 1
        print(leng2)
        verifica = 0
        if leng1 != leng2:
            print("Lunghezze differenti")
            return False
        else:
            for i in range(self.values):
                if self.__getitem__(i) == vector.__getitem__(i):
                    verifica += 1
            if verifica == leng1:
                return True
            else:
                return False

    def __add__(self, vector) -> int:
        leng1 = len(self.values)
        leng2 = len(vector)
        if leng1 != leng2:
            print("Vettori di lunghezza differente")
            return -1
        else:
            vectorT = []
            for i, j in zip(self.values, vector):
                vectorT.append(i + j)
            return vectorT

    def __sub__(self, vector) -> int:
        leng1 = len(self.values)
        leng2 = len(vector)
        if leng1 != leng2:
            print("Vettori di lunghezza differente")
            return -1
        else:
            vectorT = []
            for i, j in zip(self.values, vector):
                vectorT.append(j - i)
            return vectorT

    def __mul__(self, vector) -> int:
        leng1 = len(self.values)
        leng2 = len(vector)
        verifica = 0
        if leng1 != leng2:
            print("Vettori di lunghezza differente")
            return -1
        else:
            vectorT = []
            t = 0
            for i, j in zip(self.values, vector):
                vectorT.append(j * i)
            for i in vectorT:
                t += i
            return t

    def dot(self, vector) -> int:
        vectorT = []
        t = 0
        for i, j in zip(self.values, vector):
            vectorT.append(j * i)
        for i in vectorT:
            t += i
        return t

    def norm(self) -> float:
        t = self.values.dot(self.values)
        t = math.sqrt(t)
        return t


# VERIFICA : Con questi dati si devono ottenere i RISULTATI mostrati sotto
"""
print("1) ", v1)
print("2) ", v1[0])
print("3) ", v1.sum())
print("4) ", v1 + v2)
print("5) ", v2 - v1)
print("6) ", v1 == v1)
print("7) ", v1 == v2)
print("8) ", v1 * v2)
print("9) ", v1 * v3)
print("10) ", v3.norm())
"""
# VERIFICA:
t = 0
v1 = Vector([1, 2, 3])
v2 = Vector([2, 4, 6])
v3 = Vector([1, 2, 3, 4])
# ES 1
v1.__repr__()
# ES 2
t = v1.sum()
print(f"Ecco la somma: {t}")
# ES 3
valore = v1.__getitem__(0)
print(f"Il valore richiesto: {valore}")
# ES 4
confronto = v1.__eq__(v2)
if confronto:
    print("Vettori uguali")
else:
    print("Vettori differenti")
confronto = v1.__eq__(v1)
if confronto:
    print("Vettori uguali")
else:
    print("Vettori differenti")
# ES 5
t = v1.__add__(v2)
print(t)
# ES 6
t = v1.__sub__(v2)
print(t)
# ES 7
t = v1.__mul__(v2)
print(t)
t = v1.__mul__(v2)
print(t)
# ES 8
t = v3.norm()
print(t)
# RISULTATI
"""
1)  [1, 2, 3]
2)  1
3)  6
4)  [3, 6, 9]
5)  [1, 2, 3]
6)  True
7)  False
8)  28
I vettori hanno dimensioni diverse
9)  None
10)  5.477225575051661
"""
