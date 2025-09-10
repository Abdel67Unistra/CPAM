# -*- coding: utf-8 -*-
"""
Analyse Niveau Basique - Dépenses de santé en France
Projet CPAM Strasbourg - Analyses descriptives avancées
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Configuration des graphiques
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def analyse_depenses_sante():
    """
    Analyse descriptive complète des dépenses de santé en France
    """
    
    # Données dépenses de santé (en millions d'euros)
    depenses_data = {
        'Categorie': ['Consultations', 'Médicaments', 'Hospitalisations', 'Soins dentaires', 'Optique'],
        'Depenses_2023': [12000, 9500, 15000, 3000, 2000],
        'Depenses_2022': [11500, 9200, 14500, 2800, 1900],
        'Depenses_2021': [11000, 8800, 14000, 2600, 1800],
        'Part_population': [85, 70, 25, 60, 40],  # % population concernée
        'Croissance_annuelle': [4.3, 3.8, 3.6, 7.1, 5.3]  # % croissance
    }
    
    df = pd.DataFrame(depenses_data)
    
    print("="*60)
    print("ANALYSE DESCRIPTIVE - DÉPENSES DE SANTÉ EN FRANCE")
    print("="*60)
    
    # 1. STATISTIQUES DESCRIPTIVES
    print("\n1. STATISTIQUES DESCRIPTIVES GÉNÉRALES")
    print("-"*50)
    
    depenses_cols = ['Depenses_2023', 'Depenses_2022', 'Depenses_2021']
    for col in depenses_cols:
        print(f"\n{col.replace('_', ' ').title()}:")
        print(f"  Total: {df[col].sum():,} M€")
        print(f"  Moyenne: {df[col].mean():.0f} M€")
        print(f"  Médiane: {df[col].median():.0f} M€")
        print(f"  Écart-type: {df[col].std():.0f} M€")
        print(f"  Min: {df[col].min():,} M€ ({df.loc[df[col].idxmin(), 'Categorie']})")
        print(f"  Max: {df[col].max():,} M€ ({df.loc[df[col].idxmax(), 'Categorie']})")
    
    # 2. ANALYSE DE L'ÉVOLUTION
    print("\n\n2. ANALYSE DE L'ÉVOLUTION TEMPORELLE")
    print("-"*50)
    
    df['Evolution_2022_2023'] = ((df['Depenses_2023'] - df['Depenses_2022']) / df['Depenses_2022'] * 100)
    df['Evolution_2021_2023'] = ((df['Depenses_2023'] - df['Depenses_2021']) / df['Depenses_2021'] * 100)
    
    print("\nÉvolution 2022-2023 par catégorie:")
    for idx, row in df.iterrows():
        print(f"  {row['Categorie']}: {row['Evolution_2022_2023']:+.1f}%")
    
    print(f"\nCroissance moyenne 2022-2023: {df['Evolution_2022_2023'].mean():.1f}%")
    
    # 3. ANALYSE DE LA RÉPARTITION
    print("\n\n3. ANALYSE DE LA RÉPARTITION")
    print("-"*50)
    
    df['Part_2023'] = (df['Depenses_2023'] / df['Depenses_2023'].sum() * 100)
    
    print("\nRépartition des dépenses 2023:")
    for idx, row in df.iterrows():
        print(f"  {row['Categorie']}: {row['Part_2023']:.1f}% ({row['Depenses_2023']:,} M€)")
    
    # 4. ANALYSE DE CORRÉLATION
    print("\n\n4. ANALYSE DE CORRÉLATION")
    print("-"*50)
    
    # Corrélation entre dépenses et part de population
    corr_pop = stats.pearsonr(df['Depenses_2023'], df['Part_population'])
    print(f"Corrélation dépenses/population concernée: {corr_pop[0]:.3f}")
    print(f"P-value: {corr_pop[1]:.3f}")
    
    # Corrélation entre dépenses et croissance
    corr_croiss = stats.pearsonr(df['Depenses_2023'], df['Croissance_annuelle'])
    print(f"Corrélation dépenses/croissance: {corr_croiss[0]:.3f}")
    print(f"P-value: {corr_croiss[1]:.3f}")
    
    # 5. INSIGHTS MÉTIER
    print("\n\n5. INSIGHTS MÉTIER POUR LA CPAM")
    print("-"*50)
    
    top_depense = df.loc[df['Depenses_2023'].idxmax()]
    top_croissance = df.loc[df['Croissance_annuelle'].idxmax()]
    
    print(f"• Poste de dépense principal: {top_depense['Categorie']} ({top_depense['Depenses_2023']:,} M€)")
    print(f"• Croissance la plus forte: {top_croissance['Categorie']} ({top_croissance['Croissance_annuelle']:.1f}%)")
    print(f"• Budget total 2023: {df['Depenses_2023'].sum():,} M€")
    print(f"• Évolution globale: +{df['Evolution_2022_2023'].mean():.1f}%")
    
    # Recommandations
    print(f"\n🔍 RECOMMANDATIONS CPAM:")
    print(f"• Surveiller les {top_croissance['Categorie'].lower()} (croissance {top_croissance['Croissance_annuelle']:.1f}%)")
    print(f"• Optimiser la gestion des {top_depense['Categorie'].lower()} (plus gros poste)")
    
    if df['Evolution_2022_2023'].mean() > 5:
        print("• Vigilance sur l'inflation des coûts de santé")
    
    return df

def analyse_actes_medicaux():
    """
    Analyse descriptive des actes médicaux par spécialité
    """
    
    actes_data = {
        'Specialite': ['Généraliste', 'Cardiologie', 'Dermatologie', 'Pédiatrie', 'Ophtalmologie'],
        'Nombre_Actes': [8500000, 1200000, 900000, 1500000, 1100000],
        'Cout_Moyen': [25, 45, 35, 30, 40],  # euros par acte
        'Taux_Remboursement': [70, 65, 60, 100, 60]  # %
    }
    
    df_actes = pd.DataFrame(actes_data)
    
    print("\n\n" + "="*60)
    print("ANALYSE DESCRIPTIVE - ACTES MÉDICAUX PAR SPÉCIALITÉ")
    print("="*60)
    
    # Calculs dérivés
    df_actes['Cout_Total'] = df_actes['Nombre_Actes'] * df_actes['Cout_Moyen'] / 1000000  # M€
    df_actes['Remboursement_CPAM'] = df_actes['Cout_Total'] * df_actes['Taux_Remboursement'] / 100
    
    print("\n1. VOLUME D'ACTES PAR SPÉCIALITÉ")
    print("-"*50)
    
    total_actes = df_actes['Nombre_Actes'].sum()
    for idx, row in df_actes.iterrows():
        part = row['Nombre_Actes'] / total_actes * 100
        print(f"  {row['Specialite']}: {row['Nombre_Actes']:,} actes ({part:.1f}%)")
    
    print(f"\nTotal actes: {total_actes:,}")
    
    print("\n2. ANALYSE ÉCONOMIQUE")
    print("-"*50)
    
    for idx, row in df_actes.iterrows():
        print(f"  {row['Specialite']}:")
        print(f"    Coût total: {row['Cout_Total']:.1f} M€")
        print(f"    Remboursement CPAM: {row['Remboursement_CPAM']:.1f} M€")
    
    print(f"\nCoût total tous actes: {df_actes['Cout_Total'].sum():.1f} M€")
    print(f"Remboursement CPAM total: {df_actes['Remboursement_CPAM'].sum():.1f} M€")
    
    return df_actes

def generer_rapport_complet():
    """
    Génère un rapport complet d'analyse
    """
    print("RAPPORT D'ANALYSE - CPAM STRASBOURG")
    print("Niveau Basique - Analyses descriptives")
    print("Date:", pd.Timestamp.now().strftime("%d/%m/%Y"))
    
    # Analyses
    df_depenses = analyse_depenses_sante()
    df_actes = analyse_actes_medicaux()
    
    # Synthèse finale
    print("\n\n" + "="*60)
    print("SYNTHÈSE EXÉCUTIVE")
    print("="*60)
    
    budget_total = df_depenses['Depenses_2023'].sum()
    cout_actes = df_actes['Cout_Total'].sum()
    
    print(f"• Budget dépenses santé 2023: {budget_total:,} M€")
    print(f"• Coût actes médicaux: {cout_actes:.1f} M€")
    print(f"• Croissance moyenne: +{df_depenses['Evolution_2022_2023'].mean():.1f}%")
    print(f"• Poste principal: {df_depenses.loc[df_depenses['Depenses_2023'].idxmax(), 'Categorie']}")
    print(f"• Spécialité dominante: {df_actes.loc[df_actes['Nombre_Actes'].idxmax(), 'Specialite']}")
    
    return {
        'depenses': df_depenses,
        'actes': df_actes,
        'budget_total': budget_total,
        'croissance': df_depenses['Evolution_2022_2023'].mean()
    }

if __name__ == "__main__":
    rapport = generer_rapport_complet()
    print(f"\n✅ Rapport généré avec succès!")
