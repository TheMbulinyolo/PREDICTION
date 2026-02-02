# 🏠 Paris Price ML — Prédiction du prix des appartements à Paris

Projet open source de Machine Learning visant à prédire le prix au m² des appartements à Paris à partir des données publiques DVF (Demandes de Valeurs Foncières).

Ce projet a été conçu pour :
- apprendre le Machine Learning appliqué
- comprendre un pipeline ML complet (données → modèle → déploiement)
- encourager les contributions de débutants

---

## 🎯 Objectifs du projet

- Prédire le prix au m² d’un appartement parisien
- Fournir une interface web simple et moderne (FastAPI + Tailwind)
- Servir de base d’apprentissage pour le ML, la data et le déploiement
- Être amélioré progressivement par la communauté

---

## 🧠 Modèle de Machine Learning

- Type : Régression
- Cible : log(prix_m2) (reconversion avec `exp`)
- Algorithme : CatBoost Regressor (version actuelle)
- Features principales :
  - Surface réelle bâtie
  - Nombre de pièces
  - Arrondissement

### 📈 Performances (indicatives)
- R² (log) ≈ 0.19
- MAE ≈ 2987 €/m²

> ⚠️ Les performances dépendent fortement des données DVF utilisées, du nettoyage et de la période.

---

## 🗂️ Structure du projet

PREDICTION/
├── app/
│   ├──main.py              # Application FastAPI
│   └── templates/               # Templates HTML (Tailwind)
│       ├── base.html
│       ├── index.html
│       ├── result.html
│       └── about.html
├── models/
│   └── prix_m2_pipeline.pkl # Modèle ML entraîné
├── notebooks/
│   ├── 01_exploration.ipynb
│   └── 02_train_model.ipynb
├── requirements.txt
├── vercel.json
├── README.md
└── CONTRIBUTING.md

---

## 🌐 Interface Web

- Formulaire d’estimation (surface, pièces, arrondissement)
- Page résultat avec prix au m² et prix total
- Page About détaillant :
  - caractéristiques du modèle
  - limites
  - roadmap
  - liens utiles
  - règles de contribution

Interface réalisée avec Tailwind CSS (style moderne / dark).

---

## 🚀 Déploiement

### ⚠️ Important
Les modèles ML lourds (ex: CatBoost) ne sont pas adaptés aux Serverless Functions de la limite de taille (250 MB).

### Déploiement recommandé
- Frontend (UI) : Vercel
- Backend ML (FastAPI + modèle) : Render / Railway / Fly.io

### Alternative (tout-en-un)
- Déployer l’intégralité du projet sur Render

---

## ▶️ Lancer le projet en local

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload