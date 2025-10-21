# Scrivere un programma che, data una stringa scelta dall'utente, stampi la lunghezza della sequenza più lunga di caratteri uguali consecutivi.

stringa = input("Inserisci una stringa: ")

posizioneLetteraConMaggiorFrequenza = 0
contatoreDiFrequenza = 0
letteraConMaxFrequenza = ""

contatoreTemporaneo = 0
letteraTemporanea = ""
for i in range (0, len(stringa)):
    if letteraTemporanea == stringa[i]:
        contatoreTemporaneo += 1
    else:
        contatoreTemporaneo = 1
        letteraTemporanea = stringa[i]

    if contatoreTemporaneo > contatoreDiFrequenza:
        contatoreDiFrequenza = contatoreTemporaneo
        posizioneLetteraConMaggiorFrequenza = i
        letteraConMaxFrequenza = stringa[i]

print("Lettera con maggior frequenza: ", letteraConMaxFrequenza)
print("Posizione:", posizioneLetteraConMaggiorFrequenza)
print("Frequenza: ", contatoreDiFrequenza)


