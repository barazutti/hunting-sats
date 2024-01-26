import json
import hashlib

def hash_sha256(word):
    return hashlib.sha256(word.encode('utf-8')).hexdigest()

# Lade die BIP39-Wortliste
dateipfad = 'bip39_wordlist.json'
with open(dateipfad, 'r') as datei:
    bip39_wordlist = json.load(datei)

# Ziel-Digest
ziel_digest = '8e6388f46272755745123688c1b72722461fcc305e3c8a000f24393deb2bc3bf'

# Iteriere über jedes Wort in der BIP39-Liste
for word in bip39_wordlist:
    # Wandle das Wort in seine binäre Repräsentation um (Index in der Liste zu Binär)
    index = bip39_wordlist.index(word)
    binary_word = format(index, '011b')  # 11 Bit für die Darstellung, da 2048 Wörter in der Liste sind
    
    # Berechne den SHA-256 Hash des binären Wortes
    digest = hash_sha256(binary_word)
    
    # Überprüfe, ob der resultierende Digest mit dem Ziel-Digest übereinstimmt
    if digest == ziel_digest:
        print(f"Übereinstimmendes Wort gefunden: {word}")
        break
else:
    print("Kein übereinstimmendes Wort in der BIP39-Liste gefunden.")
