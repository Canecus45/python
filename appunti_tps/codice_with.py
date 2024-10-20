"""
Construtto with:
serve per aprire e poi 
chiudere in autonomia il file

ESEMPIO:
"""

file = open("file.txt", "r")
try:
    contenuto = file.read()
finally:
    # Questo blocco di codice verrà eseguito sempre,
    # anche se nel blocco try viene genereta un eccezzione
    file.close

with open(file):
    pass
