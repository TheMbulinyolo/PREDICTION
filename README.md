# 🏠 Prédiction du prix des appartements à Paris (Machine Learning)

## 📌 Description du projet

Ce projet a pour objectif de prédire le prix au mètre carré des appartements à Paris à partir de données publiques de transactions immobilières, en utilisant des techniques de Machine Learning supervisé.

Les données proviennent de la base DVF (Demandes de Valeurs Foncières) mise à disposition par l’État français.  
Le projet couvre l’ensemble de la chaîne ML :
- exploration des données
- nettoyage et feature engineering
- entraînement de modèles
- évaluation des performances
- amélioration progressive du modèle

Ce projet a été réalisé dans un but pédagogique et portfolio, en partant d’un niveau débutant en ML.

---

## 🎯 Objectif

- Prédire le prix au m² d’un appartement parisien
- Comprendre l’impact des variables clés (surface, pièces, localisation, temps)
- Construire un pipeline ML propre et reproductible

---

## 📂 Structure du projet

prix_appart_paris/
│
├── data/
│   ├── raw/                # Données DVF brutes (.txt)
│   └── processed/          # Données nettoyées et filtrées
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_cleaning.ipynb
│   └── 03_train_model.ipynb
│
├── models/
│   └── prix_m2_model.pkl   # Modèle entraîné sauvegardé
│
├── README.md
└── requirements.txt

---

## 📊 Données utilisées

- Source : DVF – Demandes de Valeurs Foncières
- Période : ventes récentes (ex : 2023–2025)
- Zone géographique : Paris (département 75)
- Type de bien : Appartements uniquement

### Variables principales :
- Surface réelle bâtie
- Nombre de pièces principales
- Arrondissement (extrait du code postal)

---

## 🧠 Méthodologie

### 1️⃣ Prétraitement
- Filtrage Paris + appartements
- Nettoyage des valeurs manquantes
- Correction des formats numériques (virgule → point)
- Suppression des outliers extrêmes
- Création de la variable cible : prix au m²

### 2️⃣ Feature engineering
- Extraction de l’arrondissement depuis le code postal
- Transformation logarithmique de la cible (`log(prix_m2)`)
- Ajout de variables temporelles (année, mois)

### 3️⃣ Modèles testés
- Régression linéaire (baseline)
- CatBoost Regressor (modèle principal)

---

## 🤖 Modèle final

- Algorithme : CatBoostRegressor
- Variable cible : log(prix_m2)
- Features utilisées :
  - Surface réelle bâtie
  - Nombre de pièces
  - Arrondissement

---

## 📈 Résultats

- R² (log-prix) ≈ 0.19
- MAE ≈ 2432 €/m² (selon période)

📌 Ce score est cohérent avec :
- des données publiques
- un nombre limité de features
- l’absence d’informations privées (étage, ascenseur, quartier précis)

---

## 🧪 Évaluation

Les performances sont évaluées avec :
- R² (qualité globale du modèle)
- MAE (erreur moyenne en €/m², interprétable métier)

Les métriques sont calculées dans le même espace que la cible (log ou réel).

---

## ⚠️ Limites du projet

- Pas d’information sur l’étage, l’ascenseur, l’état du bien
- Localisation limitée à l’arrondissement
- Données DVF parfois bruitées ou incomplètes
- Le modèle ne remplace pas une expertise immobilière

---

## 🚀 Pistes d’amélioration

- Ajouter une localisation plus fine (quartier, coordonnées GPS)
- Intégrer des données de transports (métro)
- Ajouter des informations bâtiment (année de construction)
- Tester un split temporel strict
- Déployer une API de prédiction (FastAPI)

---

## 🛠️ Technologies utilisées

- Python
- pandas, numpy
- scikit-learn
- CatBoost
- Jupyter Notebook

---

## 👤 Auteur

Projet réalisé par MBULINYOLO MALIYASASA EDDY 

---

## 📜 Licence

Ce projet est fourni à des fins éducatives et expérimentales.