def encode(name, upper=True) -> str:
        from unicodedata import normalize

        ascii_name = normalize("NFKD", name).encode("ascii", errors="ignore").decode("ascii")        
        return ascii_name.upper() if upper else ascii_name
    


def nome(name) -> str:
        """ Remove caractere inicial em branco, caso haja, e retorna decodicidado em upperCase """
        return encode(name.strip())