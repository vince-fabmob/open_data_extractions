from src.text_normalization import normaliser_texte


def contient_mot_cle(texte, mots_cles):
    """Indique si un texte contient au moins un mot-clé normalisé."""
    texte_normalise = normaliser_texte(texte)
    return any(
        normaliser_texte(mot_cle) in texte_normalise
        for mot_cle in mots_cles
    )


def classer_texte(texte, categories):
    """Retourne la première catégorie correspondant à un texte, ou None."""
    for categorie, mots_cles in categories.items():
        if contient_mot_cle(texte, mots_cles):
            return categorie
    return None
