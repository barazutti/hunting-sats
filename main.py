import json
import random
from bitcoinlib.mnemonic import Mnemonic



# Der Pfad zur JSON-Datei, die die Wortliste enthält
dateipfad = 'bip39_wordlist.json'

# Öffnen der JSON-Datei und Laden der Wortliste
with open(dateipfad, 'r') as datei:
    bip39_wordlist = json.load(datei)

# Liste der bekannten Wörter mit spezifizierten Positionen und ohne Positionen
bekannte_woerter_mit_position = [('apple', 3), ('orange', 5)]
bekannte_woerter_ohne_position = ['banana', 'grape']

# Initialisiere das Array mit Platzhaltern
final_array = [None] * 12

# Setze bekannte Wörter mit spezifizierten Positionen
for wort, position in bekannte_woerter_mit_position:
    final_array[position] = wort
    bip39_wordlist.remove(wort)  # Entferne das Wort aus der Wortliste, um Duplikate zu vermeiden

# Setze bekannte Wörter ohne spezifizierte Positionen an zufälligen Positionen
for wort in bekannte_woerter_ohne_position:
    while True:
        zufaellige_position = random.randint(0, len(final_array) - 1)
        if final_array[zufaellige_position] is None:  # Finde eine leere Position
            final_array[zufaellige_position] = wort
            bip39_wordlist.remove(wort)  # Entferne das Wort aus der Wortliste, um Duplikate zu vermeiden
            break

# Fülle den Rest des Arrays mit zufälligen Wörtern
for i in range(len(final_array)):
    if final_array[i] is None:  # Suche nach Platzhaltern
        zufaelliges_wort = random.choice(bip39_wordlist)
        final_array[i] = zufaelliges_wort
        bip39_wordlist.remove(zufaelliges_wort)  # Entferne das Wort aus der Wortliste, um Duplikate zu vermeiden


# Konvertiere die Liste von Wörtern in einen String, getrennt durch Leerzeichen
mnemonic_phrase = ' '.join(final_array)
print(mnemonic_phrase)
# Optional kannst du ein Passwort hinzufügen, das zum Salt der PBKDF2-Funktion wird
# Erzeuge den Seed aus der Mnemonic-Phrase
mnemo = Mnemonic()
#mnemonic_phrase = mnemo.generate(128)  # 128 gibt die Entropielänge an, die zu einer Phrase mit 12 Wörtern führt
seed = mnemo.to_seed(mnemonic_phrase)


# Zeige die Mnemonic-Phrase und den generierten Seed an
print("Mnemonic-Phrase:", mnemonic_phrase)
print("Generierter Seed:", seed.hex())






