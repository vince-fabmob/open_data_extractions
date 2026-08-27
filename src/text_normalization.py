import re
import unicodedata


def normaliser_texte(valeur):
    """Retourne une chaîne minuscule, sans accents et à espaces normalisés."""
    if valeur is None:
        return ""

    texte = str(valeur).lower()
    texte = unicodedata.normalize("NFD", texte)
    texte = "".join(
        caractere
        for caractere in texte
        if unicodedata.category(caractere) != "Mn"
    )
    texte = re.sub(r"\s+", " ", texte)
    return texte.strip()
