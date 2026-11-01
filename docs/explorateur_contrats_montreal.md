# Explorateur des contrats de Montréal — version 1

Ouvrir notebooks/02_explorateur_contrats_montreal.ipynb dans Google Colab. Modifier les paramètres puis exécuter tout. Les dépendances pandas, requests et openpyxl sont nécessaires.

## Recherche
INCLURE et EXCLURE sont des listes d'expressions littérales. MODE vaut OU ou ET. La normalisation retire les accents et remplace la ponctuation par des espaces; ce n'est pas une recherche sémantique. CHAMP choisit un champ ou tous. SOURCES et SERVICES demandent les libellés exacts. CATEGORIE filtre un identifiant. Les bornes de dates et montants excluent les valeurs non reconnues. Les classifications portent uniquement sur la description, jamais sur le seul nom du fournisseur.

## Règles
config/contrats_categories.csv définit les axes et libellés. config/contrats_regles.csv contient une expression obligatoire, un terme requis facultatif et une exclusion facultative par règle. Plusieurs règles peuvent attribuer la même catégorie; les preuves sont conservées. Une catégorie vide signifie non classé, pas absence du thème. Le dictionnaire initial est volontairement limité. Les classifications sont des propositions non validées.

## Actualisation
Remplacer les quatre CSV complets à la racine, conserver leurs noms, faire commit puis push. Relancer tout avec REF=main. Le notebook résout main vers un commit unique avant de charger données et règles. Un SHA dans REF fige une analyse. Ne pas concaténer des extractions complètes successives. Un échec de téléchargement arrête le traitement.

## Limites
Chaque ligne reste un enregistrement, pas un contrat unique. L'empreinte de contenu ne permet pas d'identifier une modification de contrat. Aucun rapprochement interversions, historique automatique ou mécanisme de validation manuelle persistante n'est inclus dans cette version. Les doublons exacts sont conservés par défaut; l'option d'exclusion ne supprime que des lignes identiques dans une même source. Les dates sont analysées au format ISO sans deviner jour/mois. Les montants sont convertis sans corriger les séparateurs ambigus. Les données originales restent dans les colonnes original__. Les sources ont des couvertures différentes. Recettes, avenants, décisions multifournisseurs et ententes-cadres empêchent de considérer la somme brute comme une dépense. Les synthèses comptent des enregistrements sans additionner les montants. Les échantillons d'audit ne prouvent ni exhaustivité ni stabilité des identifiants.

## Exports
Excel contient résultats, synthèse, preuves, qualité, couverture, catégories, règles et manifeste. Un manifeste JSON séparé contient commit, paramètres et empreintes des CSV. Excel peut tronquer les cellules de plus de 32767 caractères; utiliser les sources originales pour les textes très longs. Les chaînes commençant par =,+,-,@ sont neutralisées pour éviter les formules. Les sorties Colab sont temporaires : conserver les exports. Aucun fichier n'est écrit sur GitHub par le notebook.
