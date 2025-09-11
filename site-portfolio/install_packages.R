# CPAM Analytics - R Dependencies
# Plateforme d'analyse de données de santé
# Auteur: Cheriet Abdelmalek  
# Date: Septembre 2025

# Installation des packages R requis
# Exécuter: Rscript install_packages.R

# === MANIPULATION DE DONNÉES ===
install.packages("dplyr")              # Manipulation de données (>= 1.1.0)
install.packages("tidyr")              # Restructuration de données
install.packages("readr")              # Lecture de fichiers CSV/TSV
install.packages("lubridate")          # Gestion des dates et heures

# === VISUALISATION ===
install.packages("ggplot2")            # Grammaire des graphiques (>= 3.4.0)
install.packages("plotly")             # Graphiques interactifs
install.packages("corrplot")           # Matrices de corrélation
install.packages("ggcorrplot")         # Corrélations avec ggplot2

# === ANALYSES STATISTIQUES ===
install.packages("car")                # Tests statistiques avancés (>= 3.1.0)
install.packages("psych")              # Psychométrie et statistiques
install.packages("Hmisc")              # Fonctions statistiques de Harrell
install.packages("nortest")            # Tests de normalité

# === ANALYSE DE SURVIE ===
install.packages("survival")           # Analyse de survie Kaplan-Meier (>= 3.5.0)
install.packages("survminer")          # Visualisation analyse de survie
install.packages("KMsurv")             # Données d'analyse de survie

# === SÉRIES TEMPORELLES ===
install.packages("forecast")           # Prévisions temporelles (>= 8.21.0)
install.packages("tseries")            # Analyse de séries temporelles
install.packages("zoo")                # Objets temporels irréguliers
install.packages("xts")                # Séries temporelles extensibles

# === MACHINE LEARNING ===
install.packages("caret")              # Classification et régression
install.packages("randomForest")       # Forêts aléatoires
install.packages("cluster")            # Analyse de clusters
install.packages("factoextra")         # Extraction et visualisation factorielle

# === TESTS STATISTIQUES ===
install.packages("broom")              # Conversion résultats en tibbles
install.packages("emmeans")            # Moyennes marginales estimées
install.packages("multcomp")           # Comparaisons multiples

# === RAPPORT ET DOCUMENTATION ===
install.packages("knitr")              # Génération de rapports
install.packages("rmarkdown")          # Documents R Markdown
install.packages("DT")                 # Tables interactives

# === UTILITAIRES ===
install.packages("here")               # Chemins de fichiers relatifs
install.packages("janitor")            # Nettoyage de données
install.packages("scales")             # Formatage d'échelles graphiques

# Vérification des packages installés
cat("Packages R installés avec succès pour CPAM Analytics\n")
cat("Version R:", R.version.string, "\n")

# Liste des packages chargés
packages <- c("dplyr", "ggplot2", "survival", "car", "forecast")
for(pkg in packages) {
  if(require(pkg, character.only = TRUE)) {
    cat("✓", pkg, ":", packageVersion(pkg), "\n")
  } else {
    cat("✗ Erreur lors du chargement de", pkg, "\n")
  }
}
