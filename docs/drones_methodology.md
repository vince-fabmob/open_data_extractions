# Méthode : repérage des contrats liés aux drones (Ville de Montréal)

## Objectif

Repérer, dans les données ouvertes des contrats de la Ville de Montréal, les contrats liés à l'usage de drones (achat, formation, inspection, relevé, photogrammétrie, LiDAR) et, en complément, les contrats liés à la surveillance de chantier et à la gestion des entraves routières.

## Source des données

Jeu de données ouvertes des contrats et engagements financiers de la Ville de Montréal (fournisseur, numéro de contrat, date d'approbation, description, service, activité, montant). Les données brutes ne sont pas versionnées dans ce dépôt.

## Classification à deux niveaux de preuve

1. **Explicite — drone mentionné** : la description du contrat contient un terme explicite (drone, UAV, RPAS, aeronef teleploté, etc.).
2. **Compatible — validation requise** : la description contient un objet (bâtiment, pont, toiture, infrastructure...) et une méthode (inspection, relevé, photogrammétrie, LiDAR, numérisation 3D...) compatibles avec un usage de drone, sans mention explicite. Ces contrats nécessitent une vérification manuelle avant toute conclusion, car plusieurs de ces méthodes s'appliquent également à des équipements terrestres (scanner laser statique, station totale, nacelle).

Une extension du dictionnaire permet aussi de catégoriser les contrats en :
- **Entraves, signalisation ou circulation**
- **Surveillance de chantier explicite**
- **Génie-conseil incluant surveillance**

## Statistiques clés (extraction actuelle)

| Niveau de preuve | Nombre de contrats | Montant total | Montant médian |
|---|---|---|---|
| Explicite — drone mentionné | 88 | 887 366 $ | 4 656 $ |
| Compatible — validation requise | 350 | 2 469 457 $ | 4 191 $ |

### Principaux services concernés (mentions explicites)

- Infrastructures du réseau routier
- Police
- Service de l'eau
- Gestion et planification des immeubles

### Principaux fournisseurs (mentions explicites)

- MVT Geo-Solutions inc.
- Consultco inc.
- Drone Action 360 inc.
- Air Photo Max
- DroneXperts inc.
- RMUS Québec inc.
- Genidrone inc.

### Catégorie croisée « Entraves, signalisation ou circulation »

182 lignes repérées, pour 128 contrats uniques et 8 085 737 $ de valeur cumulée, avec un montant médian de 7 020 $. Les fournisseurs récurrents incluent Artelia Canada, Groupe Intervia, Signalisation Express et Beton Brunet.

## Limites

- Les mots-clés ne démontrent pas à eux seuls l'usage réel d'un drone; le niveau « Compatible » exige une vérification manuelle des descriptions.
- Certaines mentions de « drone » concernent des achats de matériel, de la formation ou des réparations, pas nécessairement un service réalisé sur le terrain.
- Les descriptions de contrats sont parfois abrégées ou incomplètes; certains faux négatifs sont probables.
- Un même numéro de contrat peut apparaître plusieurs fois (paiements échelonnés); les analyses de valeur doivent distinguer nombre de lignes et nombre de contrats uniques.

## Données

Les fichiers d'extraction bruts (contrats détaillés, dictionnaires de recherche, synthèses par année/service/fournisseur) restent hors du dépôt GitHub et doivent être conservés localement ou dans un espace de stockage autorisé.

## Prochaine étape

Étendre la méthode de classification à deux niveaux (explicite / compatible) au projet SEAO et nouvelle mobilité, afin d'harmoniser les critères de validation manuelle entre les deux projets du dépôt.