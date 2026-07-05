# CONVENTIONS NLP — Projet Charles VIII 1484

## Contexte
Pipeline HTR + NLP sur les Lettres de Charles VIII (1494),
manuscrit gothique XVe siècle, BnF Gallica.

## Règles de normalisation

| Règle | Avant | Après | Justification |
|-------|-------|-------|---------------|
| s long | ſ | s | ~200 occurrences — non reconnu par spaCy/BERT |
| nasale | ũ | un | ~25 occurrences — abréviation médiévale fréquente |
| esperluette | & | et | ~80 occurrences — conjonction abrégée |
| abréviation par | ꝑ | par | ~30 occurrences — abréviation latine médiévale |
| e nasalisé | ë | en | ~15 occurrences — voyelle nasalisée |
| R/S majuscules | pRince | prince | ~150 occurrences — erreur Kraken |
| coupures ligne | mot-\nmot | motmot | césures en fin de ligne |

## Schéma BIO pour NER

| Label | Signification | Exemple |
|-------|--------------|---------|
| B-PER | Début personne | Charles |
| I-PER | Suite personne | VIII |
| B-LOC | Début lieu | Paris |
| B-ORG | Début organisation | parlement |
| B-DATE | Début date | septembre |
| O | Hors entité | les, de, et |

## Modèles utilisés

- **HTR** : HTR-United-Manu_McFrench (Kraken, Google Colab GPU T4)
- **Lemmatisation** : spaCy fr_core_news_sm (français moderne — résultats partiels)
- **NER** : dslim/bert-base-NER (BERTrade privé non accessible)

## Seuils retenus

- Confiance HTR < 0.80 → ligne marquée needs_review
- Distance Levenshtein = 1 → correction automatique proposée
- Score NER > 0.75 → entité validée
