# Dizionario che rappresenta la scacchiera con 9 posizioni, inizialmente libere
# mentre la partita si svolge il valore associato sarà o X oppure O
theBoard = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}


def printBoard(theBoard):
    cont = 0
    for i in theBoard:
        if cont < 3:
            print(i, "|", end="")

        elif cont < 6:
            print(i, "|", end="")
        else:
            print(i, end="")
        if cont == 2 or cont == 5:
            print("-", "+", "-", "+", "-")
        cont += 1


def controllaPosizione(board, posizione):
    if board[posizione] == "":
        return True
    else:
        return False


def controllaVittoria(board):
    if (
        board[top - L] == board[top - M]
        and board[top - R] == board[top - L]
        and board[top - R] == board[top - M]
    ):
        print(f"Vittoria di {top-L}")
    elif (
        board[mid - L] == board[mid - M]
        and board[mid - R] == board[mid - L]
        and board[mid - R] == board[mid - M]
    ):
        print(f"Vittoria di {mid-L}")
    elif (
        board[low - L] == board[low - M]
        and board[low - R] == board[low - L]
        and board[low - R] == board[low - M]
    ):
        print(f"Vittoria di {low-L}")
    elif (
        board[top - L] == board[mid - M]
        and board[low - R] == board[top - L]
        and board[low - R] == board[mid - M]
    ):
        print(f"Vittoria di {top-L}")

    elif (
        board[low - L] == board[mid - M]
        and board[top - R] == board[low - L]
        and board[top - R] == board[mid - M]
    ):
        print(f"Vittoria di {low-L}")


# stabilisce il turno iniziale
turn = "X"

# ciclo per gestire le 9 mosse
for i in range(9):
    printBoard(theBoard)
    for i in range(9):
        if i % 2:
            mossa = input("Giocatore 1 inserire dove vuoi mettere la X:\n>")
        else:
            mossa = input("Giocatore 2 inserire dove vuoi mettere la O:\n>")
        if controllaPosizione(theBoard, mossa):
            print()
        if controllaVittoria(theBoard):
            pass

    # aggiorna dizionario

    # cambia turno
