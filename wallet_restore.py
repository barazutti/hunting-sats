import requests
from bitcoinlib.wallets import Wallet, wallet_create_or_open
from bitcoinlib.mnemonic import Mnemonic

# Deine Mnemonic-Phrase
mnemonic_phrase = "moon other evolve apple grape orange banana chest cluster judge orbit donkey"

# Erzeuge den Seed aus der Mnemonic-Phrase
mnemo = Mnemonic()
seed = mnemo.to_seed(mnemonic_phrase)

# Erstelle oder öffne eine Wallet mit dem generierten Seed
wallet_name = "MeineBitcoinLibWallet"
w = wallet_create_or_open(wallet_name, keys=seed, network='bitcoin')

# Gebe einige Informationen über die Wallet aus
print(f"Wallet-Name: {w.name}")
erste_adresse = w.get_key().address
print(f"Erste Adresse der Wallet: {erste_adresse}")

# Du kannst weitere Schlüssel und Adressen generieren, wenn nötig
zusatzlicher_schlussel = w.new_key()
print(f"Zusätzliche Adresse: {zusatzlicher_schlussel.address}")

# Verwende die Blockstream.info API, um Informationen zur ersten Adresse abzurufen
response = requests.get(f'https://blockstream.info/api/address/{erste_adresse}')
adresse_info = response.json()

# Ausgabe des Saldos der ersten Adresse
print(f"Saldo der ersten Adresse {erste_adresse}: {adresse_info['chain_stats']['funded_txo_sum'] - adresse_info['chain_stats']['spent_txo_sum']} Satoshi")
