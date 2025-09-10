# -*- coding: utf-8 -*-
"""
Tous les projets de Data Analyse Statistique pour un stage à la CPAM Strasbourg
"""

# Liste complète des projets
projets = [
    # Niveau Basique
    {
        "niveau": "Basique",
        "nom": "Analyse des dépenses de santé",
        "objectif": "Étudier l’évolution des dépenses de santé par région, catégorie et temps",
        "outils": "Python, Tableau, Power BI"
    },
    {
        "niveau": "Basique",
        "nom": "Répartition des actes médicaux par spécialité",
        "objectif": "Comprendre la distribution des actes médicaux par spécialité et région, identifier les pics saisonniers",
        "outils": "Python, Power BI"
    },

    # Niveau Intermédiaire
    {
        "niveau": "Intermédiaire",
        "nom": "Prévision des dépenses médicales",
        "objectif": "Anticiper les coûts futurs des remboursements pour aider à la planification budgétaire",
        "outils": "Python (ARIMA, Prophet), Tableau"
    },
    {
        "niveau": "Intermédiaire",
        "nom": "Détection de fraudes potentielles",
        "objectif": "Identifier des comportements atypiques ou anomalies dans les remboursements pour détecter des fraudes",
        "outils": "Python (Isolation Forest, DBSCAN)"
    },

    # Niveau Avancé
    {
        "niveau": "Avancé",
        "nom": "Étude de la consommation de médicaments",
        "objectif": "Identifier les tendances de consommation, détecter surconsommations et corréler avec les campagnes de prévention",
        "outils": "Python, Tableau"
    },
    {
        "niveau": "Avancé",
        "nom": "Optimisation des délais de traitement des dossiers",
        "objectif": "Réduire les délais de traitement des dossiers de remboursement, analyser les étapes ralentissant le processus",
        "outils": "Python (Kaplan-Meier), Power BI"
    }
]

# Affichage des projets sous forme de tableau
import pandas as pd

df_projets = pd.DataFrame(projets)
pd.set_option('display.max_colwidth', None)  # Affiche le contenu complet
print(df_projets)
