import requests
import json

def load_bip39_wordlist(url="https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"):
    response = requests.get(url)
    wordlist = response.text.strip().split('\n')
    return wordlist

# Lade die BIP39-Wortliste
bip39_wordlist = load_bip39_wordlist()

# Speichere die gesamte Wortliste in einer JSON-Datei
dateipfad = 'bip39_wordlist.json'
with open(dateipfad, 'w') as datei:
    json.dump(bip39_wordlist, datei, indent=4)

print(f"Die BIP39-Wortliste wurde erfolgreich in {dateipfad} gespeichert.")
