# Scrivere un programma che riceva in input una stringa dall'utente e controlli se il primo carattere della stringa è una vocale, ignorando se è maiuscolo o minuscolo.

inputStringa = input("Inserisci una stringa: ")

vocali = ["a", "e", "i", "o", "u"]

isAVocal = False

for vocale in vocali:
    if(vocale == inputStringa[0].lower()):
        isAVocal = True

print(f"La prima lettera{"" if isAVocal else " non" } è una vocale")