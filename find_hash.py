from hashlib import sha256

def finde_hash():
    nonce = 0  # Anfangswert für Nonce
    while True:
        # Erstelle einen String zum Hashen, indem ein Basisstring mit dem aktuellen Nonce-Wert kombiniert wird
        input_str = f"nonce:{nonce}"
        # Berechne den SHA-256-Hash des Eingabestrings
        hash_result = sha256(input_str.encode()).hexdigest()
        # Prüfe, ob der Hash mit fünf Nullen beginnt
        if hash_result.startswith('00000'):
            return nonce, hash_result  # Gib Nonce und Hash-Ergebnis zurück
        nonce += 1  # Erhöhe den Nonce für den nächsten Durchlauf

# Rufe die Funktion auf und weise die Ergebnisse Variablen zu
nonce, hash_result = finde_hash()

# Gib das Ergebnis außerhalb der Funktion aus
print(hash_result)
