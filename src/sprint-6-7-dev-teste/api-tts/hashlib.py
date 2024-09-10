import hashlib

def generate_phrase_hash(phrase):
    # Gera um hash único da frase usando SHA-256
    return hashlib.sha256(phrase.encode('utf-8')).hexdigest()