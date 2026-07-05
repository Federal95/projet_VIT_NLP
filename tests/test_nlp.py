
import pytest
import json
import re
import os

# ── Fonction de normalisation à tester ──────────────────────────────────────
def normalize(text):
    text = text.replace("ſ", "s")
    text = text.replace("ũ", "un")
    text = text.replace("&", "et")
    text = text.replace("ꝑ", "par")
    text = text.replace("ë", "en")
    text = re.sub(r"(?<=[a-z])R(?=[a-z])", "r", text)
    text = re.sub(r"(?<=[a-z])S(?=[a-z])", "s", text)
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    return text

# ── Test 1 : Normalisation s long ───────────────────────────────────────────
def test_normalisation_s_long():
    """La normalisation remplace le s long par s normal"""
    assert normalize("noſtre") == "nostre"
    assert normalize("ſeigneur") == "seigneur"

# ── Test 2 : Normalisation esperluette ──────────────────────────────────────
def test_normalisation_esperluette():
    """La normalisation remplace & par et"""
    assert normalize("comptes & parlement") == "comptes et parlement"

# ── Test 3 : Normalisation nasale ───────────────────────────────────────────
def test_normalisation_nasale():
    """La normalisation remplace ũ par un"""
    assert normalize("ũg pont") == "ung pont"

# ── Test 4 : Normalisation abréviation par ──────────────────────────────────
def test_normalisation_par():
    """La normalisation remplace ꝑ par par"""
    assert normalize("ꝑ terre") == "par terre"

# ── Test 5 : Schéma data contract ───────────────────────────────────────────
def test_data_contract_schema():
    """Le data contract contient tous les champs requis"""
    with open("results/data_contract.json", encoding="utf-8") as f:
        data = json.load(f)

    assert "document" in data
    assert "pages" in data
    assert len(data["pages"]) > 0

    page = data["pages"][0]
    assert "page_id" in page
    assert "lines" in page
    assert len(page["lines"]) > 0

    line = page["lines"][0]
    assert "text" in line
    assert "confidence" in line
    assert "char_confidences" in line
    assert "needs_review" in line
    assert "candidates" in line
    assert "polygon" in line

# ── Test 6 : Normalisation ne dégrade pas ───────────────────────────────────
def test_normalisation_ne_degrade_pas():
    """La normalisation ne supprime pas de mots"""
    texte = "Les lettreſ envoyees du roy noſtre ſire & de ſon royaume"
    normalise = normalize(texte)

    # Le texte normalisé doit être plus court ou égal (remplacement 1→1)
    assert len(normalise.split()) == len(texte.split())

    # Aucun caractère médiéval ne doit rester
    assert "ſ" not in normalise
    assert "&" not in normalise

# ── Test 7 : Normalisation coupures de ligne ────────────────────────────────
def test_normalisation_coupures_ligne():
    """La normalisation recolle les mots coupés en fin de ligne"""
    assert normalize("roy-\naume") == "royaume"
    assert normalize("mot-\nmot") == "motmot"
