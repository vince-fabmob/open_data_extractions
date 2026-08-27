def extraire_valeur(objet):
    """Extrait le montant d'un objet OCDS contenant une structure value."""
    return (objet or {}).get("value", {}).get("amount")


def extraire_fournisseurs(objet):
    """Retourne les noms de fournisseurs d'une attribution ou d'un contrat."""
    return [
        fournisseur.get("name")
        for fournisseur in objet.get("suppliers", [])
        if fournisseur.get("name")
    ]


def aplatir_release(release):
    """Transforme une release OCDS en lignes d'attributions et de contrats."""
    buyer = release.get("buyer", {})
    tender = release.get("tender", {})

    base = {
        "ocid": release.get("ocid"),
        "date_publication": release.get("date"),
        "acheteur": buyer.get("name"),
        "titre": tender.get("title"),
        "description": tender.get("description"),
        "statut": tender.get("status"),
    }
    lignes = []

    for award in release.get("awards", []):
        lignes.append({
            **base,
            "type_source": "award",
            "montant": extraire_valeur(award),
            "fournisseurs": " | ".join(extraire_fournisseurs(award)),
        })

    for contract in release.get("contracts", []):
        lignes.append({
            **base,
            "type_source": "contract",
            "montant": extraire_valeur(contract),
            "fournisseurs": " | ".join(extraire_fournisseurs(contract)),
        })

    return lignes or [{**base, "type_source": "tender"}]
