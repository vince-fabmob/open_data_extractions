# Explorateur des contrats de Montréal — version 1

Ouvrir notebooks/02_explorateur_contrats_montreal.ipynb dans Google Colab. Modifier les paramètres puis exécuter tout. Les dépendances pandas, requests et openpyxl sont nécessaires.

## Recherche
INCLURE et EXCLURE sont des listes d'expressions littérales. MODE vaut OU ou ET. La normalisation retire les accents et remplace la ponctuation par des espaces; ce n'est pas une recherche sémantique. CHAMP choisit un champ ou tous. SOURCES et SERVICES demandent les libellés exacts. CATEGORIE filtre un identifiant. Les bornes de dates et montants excluent les valeurs non reconnues. Les classifications portent uniquement sur la description, jamais sur le seul nom du fournisseur.

### Ajouter plusieurs termes
Modifier la première cellule de code. Séparer les éléments par des virgules, avec chaque élément entre guillemets, dans une liste entre crochets :

```python
INCLURE = ['vélo', 'cyclable', 'bicyclette']
```

Les guillemets simples ou doubles sont acceptés. Une expression de plusieurs mots reste dans une seule paire de guillemets :

```python
INCLURE = ['transport collectif', 'autobus', 'navette autonome']
```

Ne pas écrire `INCLURE = ['vélo, cyclable, bicyclette']` : il s'agit alors d'un seul élément, pas de trois termes.

### Choisir OU ou ET
Pour retenir au moins un terme :

```python
INCLURE = ['vélo', 'cyclable', 'bicyclette']
EXCLURE = []
MODE = 'OU'
CHAMP = 'description'
```

Pour exiger tous les termes dans la description, même éloignés ou dans un ordre différent :

```python
INCLURE = ['surveillance', 'chantier']
EXCLURE = []
MODE = 'ET'
CHAMP = 'description'
```

À distinguer de `INCLURE = ['surveillance de chantier']`, qui recherche cette suite de mots après normalisation. Un espace dans une expression n'est pas un opérateur ET.

### Exclure des termes

```python
INCLURE = ['surveillance', 'chantier']
EXCLURE = ['caméra', 'gardiennage']
MODE = 'ET'
CHAMP = 'description'
```

Les deux termes inclus sont requis; la présence d'au moins un terme exclu écarte l'enregistrement. `EXCLURE = []` désactive les exclusions. Avec `INCLURE = []` et `EXCLURE = []`, seuls les autres filtres s'appliquent; l'export peut être volumineux. Utiliser des éléments non vides contenant des lettres ou des chiffres, pas uniquement de la ponctuation.

### Choisir le champ

| CHAMP | Contenu recherché |
|---|---|
| 'tous' | Fournisseur, description, décision, dossier et numéro source |
| 'description' | Objet ou description |
| 'fournisseur' | Nom du fournisseur |
| 'decision' | Numéro de décision |
| 'dossier' | Numéro de dossier |
| 'numero_source' | Numéro source lorsqu'il est disponible |

`tous` n'inclut pas service, direction ni activité. Avec `tous` et `ET`, les termes peuvent être dans différents champs d'un même enregistrement.

Exemple pour un fournisseur :

```python
INCLURE = ['Transdev']
EXCLURE = []
MODE = 'OU'
CHAMP = 'fournisseur'
```

### Comprendre les correspondances et relancer
La recherche ignore les majuscules et les accents; la ponctuation est remplacée par des espaces. Elle cherche des portions de texte : `cyclable` peut correspondre à `cyclables`. Elle ne trouve pas automatiquement les synonymes et ne corrige pas les fautes. Les expressions sont littérales, pas des expressions régulières. Une même liste ne permet pas les combinaisons imbriquées telles que `(vélo OU bicyclette) ET entretien` : faire plusieurs recherches ou adapter le code.

Après modification, sélectionner Exécution → Tout exécuter pour recalculer résultats et exports. Modifier seulement les paramètres utiles; conserver `MODE = 'OU'` ou `MODE = 'ET'` en majuscules et un nom de champ figurant dans le tableau.

## Règles
config/contrats_categories.csv définit les axes et libellés. config/contrats_regles.csv contient une expression obligatoire, un terme requis facultatif et une exclusion facultative par règle. Plusieurs règles peuvent attribuer la même catégorie; les preuves sont conservées. Une catégorie vide signifie non classé, pas absence du thème. Le dictionnaire initial est volontairement limité. Les classifications sont des propositions non validées.

## Actualisation
Remplacer les quatre CSV complets à la racine, conserver leurs noms, faire commit puis push. Relancer tout avec REF=main. Le notebook résout main vers un commit unique avant de charger données et règles. Un SHA dans REF fige une analyse. Ne pas concaténer des extractions complètes successives. Un échec de téléchargement arrête le traitement.

## Limites
Chaque ligne reste un enregistrement, pas un contrat unique. L'empreinte de contenu ne permet pas d'identifier une modification de contrat. Aucun rapprochement interversions, historique automatique ou mécanisme de validation manuelle persistante n'est inclus dans cette version. Les doublons exacts sont conservés par défaut; l'option d'exclusion ne supprime que des lignes identiques dans une même source. Les dates sont analysées au format ISO sans deviner jour/mois. Les montants sont convertis sans corriger les séparateurs ambigus. Les données originales restent dans les colonnes original__. Les sources ont des couvertures différentes. Recettes, avenants, décisions multifournisseurs et ententes-cadres empêchent de considérer la somme brute comme une dépense. Les synthèses comptent des enregistrements sans additionner les montants. Les échantillons d'audit ne prouvent ni exhaustivité ni stabilité des identifiants.

## Exports
Excel contient résultats, synthèse, preuves, qualité, couverture, catégories, règles et manifeste. Un manifeste JSON séparé contient commit, paramètres et empreintes des CSV. Excel peut tronquer les cellules de plus de 32767 caractères; utiliser les sources originales pour les textes très longs. Les chaînes commençant par =,+,-,@ sont neutralisées pour éviter les formules. Les sorties Colab sont temporaires : conserver les exports. Aucun fichier n'est écrit sur GitHub par le notebook.
