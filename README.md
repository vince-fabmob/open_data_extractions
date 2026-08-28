# Open Data Extractions

Outils, notebooks et méthodes reproductibles pour extraire, nettoyer et analyser des données ouvertes liées aux contrats publics, à la mobilité et aux services municipaux.

## Projets

### 1. SEAO et nouvelle mobilité

Ce projet explore les données ouvertes du Système électronique d'appel d'offres du Québec (SEAO), publiées au format Open Contracting Data Standard (OCDS). L'objectif est de repérer des contrats reliés au transport collectif à la demande, au taxi collectif, à l'autopartage, au vélopartage et aux outils de mobilité intégrée.

### 2. Drones et surveillance augmentée (Ville de Montréal)

Ce projet explore les données ouvertes des contrats de la Ville de Montréal afin de repérer les contrats liés à l'usage de drones (inspection, relevé, photogrammétrie, LiDAR) et, plus largement, aux technologies de surveillance de chantier et de gestion des entraves routières. La classification distingue les mentions explicites de drones des cas compatibles nécessitant une validation manuelle.

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

Projets exploratoires. Une correspondance par mots-clés est un outil de repérage; les résultats doivent être vérifiés avant toute interprétation ou publication.