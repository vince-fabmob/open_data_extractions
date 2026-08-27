# Méthode SEAO : repérage de la nouvelle mobilité

## Objectif

Repérer, dans les publications ouvertes du SEAO au format OCDS, les avis, attributions et contrats pouvant concerner la nouvelle mobilité.

## Processus

1. Recenser les ressources ouvertes publiées par le SEAO.
2. Télécharger les fichiers de façon incrémentale, avec reprise après interruption.
3. Extraire les champs `buyer`, `tender`, `awards` et `contracts` des releases OCDS.
4. Construire une table plate centrée sur l'OCID, l'acheteur, le titre, la description, les fournisseurs et les montants.
5. Normaliser le texte : minuscules, retrait des accents et espaces homogènes.
6. Repérer les thèmes à l'aide des dictionnaires YAML.
7. Examiner les résultats, retirer les faux positifs et documenter les décisions.

## Limites

- Les mots-clés ne démontrent pas à eux seuls l'objet réel d'un contrat.
- Les descriptions peuvent être incomplètes ou variables selon l'organisme public.
- Une même occasion peut produire plusieurs releases, attributions ou contrats.
- Les résultats doivent être dédoublonnés et vérifiés avant analyse financière ou diffusion.

## Données

Les données brutes restent hors du dépôt GitHub. Elles doivent être obtenues depuis leur portail de données ouvertes et conservées localement ou dans un espace de stockage autorisé.
