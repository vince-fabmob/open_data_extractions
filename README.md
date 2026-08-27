# Open Data Extractions

Outils, notebooks et méthodes reproductibles pour extraire, nettoyer et analyser des données ouvertes liées aux contrats publics, à la mobilité et aux services municipaux.

## Projet initial : SEAO et nouvelle mobilité

Ce premier projet explore les données ouvertes du Système électronique d'appel d'offres du Québec (SEAO), publiées au format Open Contracting Data Standard (OCDS). L'objectif est de repérer des contrats reliés au transport collectif à la demande, au taxi collectif, à l'autopartage, au vélopartage et aux outils de mobilité intégrée.

Les données brutes ne sont pas incluses dans ce dépôt : elles sont téléchargées depuis leurs sources ouvertes au moment de l'analyse.

## Structure

- `notebooks/` : analyses exploratoires et notebooks Colab
- `src/` : fonctions Python réutilisables
- `config/` : dictionnaires de mots-clés et exclusions
- `docs/` : méthode, hypothèses et limites
- `data/` : données locales non versionnées
- `outputs/` : résultats produits localement, non versionnés

## Installation

```bash
pip install -r requirements.txt
```

## Statut

Projet exploratoire. Une correspondance par mots-clés est un outil de repérage; les résultats doivent être vérifiés avant toute interprétation ou publication.