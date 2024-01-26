import json
import random
import requests
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.wallets import Wallet, wallet_create_or_open

# Lade die BIP39-Wortliste
dateipfad = 'bip39_wordlist.json'
with open(dateipfad, 'r') as datei:
    bip39_wordlist = json.load(datei)

# Fordere den Benutzer auf, die Anzahl der Versuche einzugeben
anzahl_durchgaenge = int(input("Anzahl der Versuche eingeben: "))

for durchgang in range(anzahl_durchgaenge):
    final_array = [None] * 12
    bekannte_woerter_mit_position = [] #[('apple', 3)('zoo', 5)]
    bekannte_woerter_ohne_position = ['skate', 'release', 'box', 'work', 'kiss'] 
    # HodleHodle, Jade, wasabiwallet, plebwork, cryptosteel


    for wort, position in bekannte_woerter_mit_position:
        final_array[position] = wort
        if wort in bip39_wordlist:
            bip39_wordlist.remove(wort)

    for wort in bekannte_woerter_ohne_position:
        while True:
            zufaellige_position = random.randint(0, len(final_array) - 1)
            if final_array[zufaellige_position] is None:
                final_array[zufaellige_position] = wort
                if wort in bip39_wordlist:
                    bip39_wordlist.remove(wort)
                break

    for i in range(len(final_array)):
        if final_array[i] is None:
            zufaelliges_wort = random.choice(bip39_wordlist)
            final_array[i] = zufaelliges_wort
            bip39_wordlist.remove(zufaelliges_wort)

    mnemonic_phrase = ' '.join(final_array)
    try:
        mnemo = Mnemonic()
        seed = mnemo.to_seed(mnemonic_phrase)
        print(f"Durchgang {durchgang + 1}: Gültige Mnemonic-Phrase gefunden: {mnemonic_phrase}")

        # Erstelle oder öffne eine Wallet mit dem generierten Seed
        wallet_name = "MeineBitcoinLibWallet"
        w = wallet_create_or_open(wallet_name, keys=seed, network='bitcoin')
        erste_adresse = w.get_key().address

        # Verwende die Blockstream.info API, um Informationen zur ersten Adresse abzurufen
        response = requests.get(f'https://blockstream.info/api/address/{erste_adresse}')
        adresse_info = response.json()
        print(f"Saldo der ersten Adresse {erste_adresse}: {adresse_info['chain_stats']['funded_txo_sum'] - adresse_info['chain_stats']['spent_txo_sum']} Satoshi")
        break  # Beende die Schleife, wenn eine gültige Phrase gefunden wurde
    except ValueError as e:
        print(f"Durchgang {durchgang + 1}: Ungültige Mnemonic-Phrase: {e}")
else:
    print("Keine gültige Mnemonic-Phrase nach der angegebenen Anzahl von Versuchen gefunden.")
