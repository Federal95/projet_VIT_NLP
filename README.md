# 📜 Projet VIT NLP — Pipeline HTR + NLP
### Transcription et Analyse Philologique d'un Manuscrit Gothique du XVe siècle

> **Charles VIII · 1494 · BnF Gallica**  
> *Les lettres envoyées du roy nostre sire à nosseigneurs de parlement*

---

## 👥 Membres du groupe

| N° | Nom complet | Rôle |
|----|-------------|------|
| 1 | **Ngassa Hermine Serges NYALEU** | Prétraitement & Segmentation (Étapes 2-3) |
| 2 | **Cheick Ousmane KOUASSI** | Extraction PDF & HTR Kraken (Étapes 1 & 4) |
| 3 | **Paulin DAPA** | Pipeline NLP complet & Rapport (Étapes 5-9) |

---

## 📄 Document source

### Titre complet
> *« Les lettres envoyées du roy nostre sire à nosseigneurs de parlement, des comptes & de l'hostel de la ville de Paris, datées du x jour de septembre, l'an de grace mil CCCC. IIII. vingt & quatorze. »*

### Informations bibliographiques

| Champ | Information |
|-------|-------------|
| **Auteur** | Charles VIII (1470-1498), roi de France |
| **Date** | Septembre 1494 (an de grace mil CCCC IIII vingt et quatorze) |
| **Nature** | Lettres royales officielles — imprimé gothique incunable |
| **Destinataires** | Nosseigneurs de parlement, des comptes & de l'hostel de la ville de Paris |
| **Conservation** | Bibliothèque nationale de France (BnF) |
| **Accès** | Gallica — gallica.bnf.fr |
| **Type d'écriture** | Gothique textura XVe siècle |
| **État** | Partiellement endommagé (taches, déchirures) |
| **Pages numérisées** | 34 pages |

### Description du document

Ce document est un **recueil de lettres royales** émises par Charles VIII en septembre 1494, adressées aux institutions parisiennes (Parlement, Chambre des Comptes, Hôtel de Ville). Il s'agit d'un **imprimé gothique incunable** du XVe siècle, caractérisé par :

- Une **écriture gothique textura** dense et régulière
- Des **abréviations médiévales** nombreuses (`ꝑ` pour *par*, `&` pour *et*)
- Des **caractères spéciaux** du moyen français (`ſ` s long, `ũ` nasale)
- Une **page de titre** ornée d'une gravure sur bois représentant une scène royale
- Plusieurs pages **très endommagées** par l'humidité (taches, déchirures)

### Contenu des lettres

Les lettres relatent notamment :
- La **victoire militaire** de Charles VIII au gouffre de Rapello contre le prince de Charente
- Le **récit de bataille** par le duc d'Orléans (frère du roi)
- Les **processions** organisées à Paris pour célébrer la victoire (vendredi 19 septembre)
- Une **lettre personnelle** de Charles VIII depuis Turin mentionnant la duchesse de Savoie

### Source et licence
```
Source : gallica.bnf.fr / Bibliothèque nationale de France
Réutilisation non commerciale libre dans le cadre académique
(loi n°78-753 du 17 juillet 1978)
```

---

## 🎯 Objectif

Ce projet implémente un pipeline complet de **Reconnaissance de Texte Manuscrit (HTR)** et d'**Analyse Linguistique (NLP)** appliqué à un manuscrit gothique du XVe siècle conservé à la BnF (Gallica).

Le pipeline transforme des **images de pages manuscrites** en **entités philologiques annotées** en 9 étapes successives.

---

## 🏗️ Structure du projet

```
projet_VIT_NLP/
├── data/
│   ├── raw/                    # PDF Gallica original
│   │   └── document.pdf
│   ├── images/                 # Pages extraites (34 JPG à 300 DPI)
│   ├── processed/              # Images prétraitées OpenCV (34 JPG)
│   ├── bilevel/                # Images bi-level PNG pour Kraken (34 PNG)
│   └── lines/                  # Transcriptions HTR Kraken (9 TXT)
│       ├── page_001.txt
│       ├── page_002.txt
│       ├── page_013.txt
│       ├── page_014.txt
│       ├── page_015.txt
│       ├── page_016.txt
│       ├── page_018.txt
│       ├── page_019.txt
│       └── page_020.txt
├── notebooks/
│   ├── 01_extraction.ipynb     # PDF → images JPG
│   ├── 02_preprocessing.ipynb  # OpenCV nettoyage
│   ├── 03_segm_transcript.ipynb# Bi-level + HTR Kraken
│   └── 04_nlp.ipynb            # Pipeline NLP complet
├── results/
│   ├── transcriptions/
│   │   ├── texte_brut.txt      # Texte assemblé brut
│   │   └── texte_norm.txt      # Texte normalisé
│   ├── entities/
│   │   └── entites.json        # Entités NER annotées
│   ├── figures/
│   │   └── entites_freq.png    # Graphiques CER + entités
│   └── cer_resultats.json      # CER par page
├── models/
│   ├── kraken/                 # Modèle HTR-United-Manu_McFrench
│   ├── bertrade/               # BERTrade (moyen français)
│   └── camembert/              # CamemBERT
├── src/
│   ├── extract_pages.py
│   ├── preprocess.py
│   ├── normalize_text.py
│   └── nlp_ner.py
├── requirements.txt
├── config.py
└── README.md
```

---

## 🔄 Pipeline en 9 étapes

```
📄 PDF Gallica
     ↓
┌─────────────────────────────────────────┐
│           PARTIE HTR (Vision)           │
├─────────────────────────────────────────┤
│  1. Extraction PDF    → PyMuPDF         │
│  2. Prétraitement     → OpenCV          │
│  3. Conversion bi-level → PIL           │
│  4. Transcription HTR → Kraken ☁️ Colab│
└─────────────────────────────────────────┘
     ↓
┌─────────────────────────────────────────┐
│           PARTIE NLP (Texte)            │
├─────────────────────────────────────────┤
│  5. Normalisation     → Python re       │
│  6. CER               → jiwer          │
│  7. Lemmatisation     → spaCy          │
│  8. Levenshtein       → python-Leven.  │
│  9. NER               → dslim/bert     │
└─────────────────────────────────────────┘
     ↓
🏷️ Entités philologiques annotées
```

---

## ⚙️ Installation

### Prérequis
- Python 3.13+
- Git
- Compte Google (pour Google Colab)

### Installation locale

```bash
# Cloner le repo
git clone https://github.com/Federal95/projet_VIT_NLP.git
cd projet_VIT_NLP

# Créer l'environnement virtuel
python -m venv venv
source venv/Scripts/activate  # Windows (Git Bash)
# ou
source venv/bin/activate       # Linux/Mac

# Installer les dépendances
pip install -r requirements.txt

# Télécharger le modèle spaCy
python -m spacy download fr_core_news_sm
```

### Dépendances principales

```txt
pymupdf
opencv-python
ultralytics
kraken
transformers
torch
jiwer
spacy
python-Levenshtein
sentencepiece
matplotlib
```

---

## 🚀 Utilisation

### Étapes 1-3 — HTR (local)

```bash
source venv/Scripts/activate
jupyter notebook notebooks/01_extraction.ipynb
jupyter notebook notebooks/02_preprocessing.ipynb
jupyter notebook notebooks/03_segm_transcript.ipynb
```

### Étape 4 — Transcription Kraken (Google Colab GPU T4)

> ⚠️ **La transcription Kraken est réalisée sur Google Colab (GPU T4)**  
> CPU local : ~3h/page → GPU T4 Colab : ~10-15 min/page

```python
# Sur Google Colab — activer GPU T4 d'abord
!pip install kraken htrmopo -q

from google.colab import files
uploaded = files.upload()  # HTR-United-Manu_McFrench.mlmodel
model_path = "/content/HTR-United-Manu_McFrench.mlmodel"

uploaded_images = files.upload()  # page_001.png, page_002.png...

import subprocess, os

pages = ["page_001.png", "page_002.png", "page_013.png",
         "page_014.png", "page_015.png", "page_016.png",
         "page_018.png", "page_019.png", "page_020.png"]

for filename in pages:
    page_name = filename.replace(".png", "")
    result = subprocess.run([
        "kraken", "-i", f"/content/{filename}",
        f"/content/{page_name}.txt",
        "segment", "ocr", "-m", model_path
    ], capture_output=True, text=True,
       env={**os.environ, "PYTHONUTF8": "1"})
    if result.returncode == 0:
        print(f"✓ {page_name} transcrite !")

for page in pages:
    files.download(f"/content/{page.replace('.png', '.txt')}")
```

### Étapes 5-9 — NLP (local)

```bash
jupyter notebook notebooks/04_nlp.ipynb
```

---

## 📊 Résultats

### CER par page (Character Error Rate)

| Page | Contenu | CER | Qualité |
|------|---------|-----|---------|
| page_001 | Page de titre + gravure | 0.51% | ✅ Excellent |
| page_002 | Conditions Gallica | 9.54% | ✓ Bon |
| page_013 | Récit bataille (p.1) | 18.2% | ⚠ Acceptable |
| page_014 | Récit bataille (p.2) | 22.1% | ✗ Difficile |
| page_015 | Suite bataille | 15.3% | ⚠ Acceptable |
| page_016 | Lettre de Turin | 12.8% | ✓ Bon |
| page_018 | Récit propre | 28.4% | ✗ Difficile |
| page_019 | Page endommagée | 35.7% | ✗ Difficile |
| page_020 | Page très endommagée | 42.1% | ✗ Difficile |

### Entités nommées extraites (NER)

| Entité | Type | Score | Contexte |
|--------|------|-------|---------|
| Charles VIII | PER | 99% | Roi de France, auteur |
| Paris | LOC | 91% | Lieu d'émission |
| Orleans | LOC | 88% | Duc d'Orléans |
| Rapello | LOC | 85% | Lieu de bataille |
| Gennes | LOC | 83% | Retour après bataille |
| Turin | LOC | 81% | Ville en transit |
| Sauoye | LOC | 79% | Duché de Savoie |
| parlement | ORG | 82% | Institution destinataire |
| comptes | ORG | 79% | Institution destinataire |
| septembre | DATE | 90% | Mois d'émission |
| mil CCCC IIII vingt et quatorze | DATE | 87% | Année 1494 |

### Normalisation du moyen français

| Caractère | Signification | Occurrences | Remplacement |
|-----------|--------------|-------------|--------------|
| `ſ` | s long médiéval | ~200 | `s` |
| `ũ` | nasale abrégée | ~25 | `un` |
| `&` | esperluette | ~80 | `et` |
| `ꝑ` | abréviation par | ~30 | `par` |
| `ë` | e nasalisé | ~15 | `en` |

---

## 🔬 Modèles utilisés

| Modèle | Usage | Source |
|--------|-------|--------|
| HTR-United-Manu_McFrench | Transcription HTR | [HTRomopo](https://github.com/HTR-United) |
| fr_core_news_sm | Lemmatisation | [spaCy](https://spacy.io) |
| dslim/bert-base-NER | NER | [HuggingFace](https://huggingface.co/dslim/bert-base-NER) |

---

## ⚠️ Limitations

- **YOLO** : 0 détection sur manuscrits médiévaux → remplacé par Kraken
- **Kraken CPU** : ~3h/page → résolu via Google Colab GPU T4
- **BERTrade** : dépôt privé non accessible → remplacé par dslim/bert
- **spaCy** : limité sur le moyen français du XVe siècle
- **Corpus** : 9 pages transcrites sur 34 au total

---

## 📚 Références

- [BnF Gallica — Lettres de Charles VIII](https://gallica.bnf.fr)
- [Kraken HTR](https://kraken.re)
- [HTR-United](https://github.com/HTR-United)
- [spaCy](https://spacy.io)
- [HuggingFace Transformers](https://huggingface.co)
- [Google Colab](https://colab.research.google.com)

---

## 👨‍💻 Groupe

**Ngassa Hermine Serges NYALEU · Cheick Ousmane KOUASSI · Paulin DAPA**  
Cours Vision par Ordinateur & Analyse Philologique — Juin 2026

---

*Document : Charles VIII, Lettres envoyées, 1494 — BnF Gallica*
