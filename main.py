import json
import random
from bitcoinlib.mnemonic import Mnemonic

# Lade die BIP39-Wortliste
dateipfad = 'bip39_wordlist.json'
with open(dateipfad, 'r') as datei:
    bip39_wordlist = json.load(datei)

anzahl_durchgaenge = int(input("Anzahl der Durchgänge eingeben: "))

for durchgang in range(anzahl_durchgaenge):
    # Initialisiere das Array mit Platzhaltern
    final_array = [None] * 12

    # Liste der bekannten Wörter mit spezifizierten Positionen und ohne Positionen
    bekannte_woerter_mit_position = [('apple', 3), ('orange', 5)]
    bekannte_woerter_ohne_position = ['banana', 'grape']

    # Setze bekannte Wörter mit spezifizierten Positionen
    for wort, position in bekannte_woerter_mit_position:
        final_array[position] = wort
        if wort in bip39_wordlist:  # Stelle sicher, dass das Wort nur einmal entfernt wird
            bip39_wordlist.remove(wort)

    # Setze bekannte Wörter ohne spezifizierte Positionen an zufälligen Positionen
    for wort in bekannte_woerter_ohne_position:
        while True:
            zufaellige_position = random.randint(0, len(final_array) - 1)
            if final_array[zufaellige_position] is None:
                final_array[zufaellige_position] = wort
                if wort in bip39_wordlist:  # Stelle sicher, dass das Wort nur einmal entfernt wird
                    bip39_wordlist.remove(wort)
                break

    # Fülle den Rest des Arrays mit zufälligen Wörtern
    for i in range(len(final_array)):
        if final_array[i] is None:
            zufaelliges_wort = random.choice(bip39_wordlist)
            final_array[i] = zufaelliges_wort
            bip39_wordlist.remove(zufaelliges_wort)

    # Konvertiere die Liste von Wörtern in einen String, getrennt durch Leerzeichen
    mnemonic_phrase = ' '.join(final_array)

    # Versuche, den Seed aus der Mnemonic-Phrase zu erzeugen
    try:
        mnemo = Mnemonic()
        seed = mnemo.to_seed(mnemonic_phrase)
        print(f"Gültige Mnemonic-Phrase gefunden: {mnemonic_phrase}")
        print(f"Generierter Seed: {seed.hex()}")
        break  # Beende die Schleife, wenn eine gültige Phrase gefunden wurde
    except ValueError as e:
        print(f"Ungültige Mnemonic-Phrase bei Durchgang {durchgang + 1}: {e}")
else:
    print("Keine gültige Mnemonic-Phrase gefunden.")
