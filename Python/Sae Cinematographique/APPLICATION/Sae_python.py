#SAE python feuille de route 2

import pandas as pd

# chargement des données csv

def chargementdonnees(cheminFichier, colonnes_a_charger=None, ligne_debut=None, ligne_fin=None, filtre =None):
    """
    Charge un fichier CSV avec une sélection de colonnes et de lignes spécifiques.
    
    Parametres :
        cheminFichier (str) : Le chemin du fichier CSV à charger.
        colonnes_a_charger (list of str, optional) : Liste des colonnes à charger. Si None, toutes les colonnes sont chargées.
        ligne_debut (int, optional) : Ligne de début (index 0). Si None, commence à la première ligne.
        ligne_fin (int, optional) : Ligne de fin (index 0). Si None, charge jusqu'à la fin.
    
    Retourne :
        pandas.DataFrame : Le DataFrame avec les données demandées.
    """
    # Charger les données avec la plage de lignes et les colonnes spécifiées
    data = pd.read_csv(cheminFichier,encoding='ISO-8859-1',sep=';',usecols=colonnes_a_charger,skiprows=ligne_debut,nrows=(ligne_fin - ligne_debut + 1)if ligne_debut is not None and ligne_fin is not None else None)
                 
    return data

colonnes_souhaitees = ['nom', 'adresse']
data2022 = chargementdonnees("data\etablissements-cinematographiques.csv")

data2021 = chargementdonnees("data\Données cartographie 2021.csv")
data2020 = chargementdonnees("data\Données cartographie 2020 -.csv")
data2019 = chargementdonnees("data\Données Cartographie 2019.csv")
data2018 = chargementdonnees("data\DonnéesCartographie2018.csv")


def filtre(data, filtre):
    """
   Applique un filtre sur un DataFrame en fonction des conditions spécifiées dans un dictionnaire.

   Parametres :
       data (pandas.DataFrame) : Le DataFrame sur lequel appliquer les filtres.
       filtre (dict, optional) : Un dictionnaire où chaque clé est une colonne du DataFrame et chaque valeur est la condition de filtrage.
                                  Par exemple, {"colonne1": "valeur1", "colonne2": "valeur2"} va filtrer les lignes où `colonne1` = `valeur1` et `colonne2` = `valeur2`.

   Retourne :
       data : Le DataFrame filtré selon les conditions spécifiées dans `filtre`.
       
   """
    if filtre is not None:
        for key, value in filtre.items():
            if key in data.columns:
                data = data[data[key] == value]
            else:
                print(f"Attention : La colonne '{key}' n'existe pas dans le DataFrame.")

    return data

data = filtre(data2022,{'N° auto': 31})



def afficher(data, n=4):
    """
    Affiche les premières lignes d'un DataFrame.

    Parametres :
        data (pandas.DataFrame): Le DataFrame dont les premières lignes doivent être affichées.
        n (int, optional): Le nombre de lignes à afficher (par défaut 4).

    Retourne:
        None: La fonction affiche simplement les lignes, sans rien retourner.
    """
    print(data.head(n))
    
    
def afficher1(data, n=4, filtre=None):
    """
    Affiche les premières lignes d'un DataFrame, avec possibilité d'appliquer un filtre.
    
    Parametres :
        data (pandas.DataFrame): Le DataFrame dont les premières lignes doivent être affichées.
        n (int, optional): Le nombre de lignes à afficher (par défaut 4).
        filtre (dict, optional): Dictionnaire contenant les colonnes et valeurs à filtrer, par exemple {"departement": "75", "commune": "Paris"}.
    
    Retourne :
        None: La fonction affiche simplement les lignes filtrées et sélectionnées, sans rien retourner.
    """
    # Appliquer un filtre si spécifié
    if filtre is not None:
        for key, value in filtre.items():
            if key in data.columns:
                data = data[data[key] == value]
            else:
                print(f"Attention : La colonne '{key}' n'existe pas dans le DataFrame.")
    
    # Afficher les premières lignes après filtrage
    print(data.head(n))


# Exemple avec filtre supplémentaire sur la population
afficher1(data2022, n=3, filtre={'N° auto': 31})

# Visualisation des données

def tableau_somme_par_departement(df, colonne):
    """
    Calcule la somme des valeurs d'une colonne par département.

    Paramètres :
        df (pandas.DataFrame) : Le tableau de données.
        colonne (str)         : Le nom de la colonne à sommer.

    Retour :
        pandas.DataFrame : Un DataFrame avec deux colonnes : 'departement' et la somme demandée.
    """
    return df.groupby("DEP")[colonne].sum().reset_index()

##TEST 
n = tableau_somme_par_departement(data2022, "fauteuils")
tableau_somme_par_departement(data2022, "écrans")
tableau_somme_par_departement(data2022, "séances")

print(data2022.shape)
print(data2022.describe())

import matplotlib.pyplot as plt

def visualiser_donnees(df, colonne_x, colonne_y=None, type_graphique="histogramme"):
    """
    Visualise les données avec Matplotlib selon différents types de graphiques.

    :param df: DataFrame pandas, les données
    :param colonne_x: str, nom de la colonne pour l'axe X
    :param colonne_y: str, nom de la colonne pour l'axe Y (si applicable)
    :param type_graphique: str, type de graphique ("histogramme", "boîte", "nuage", "courbe")
    """
    plt.figure(figsize=(8, 5))

    if type_graphique == "histogramme":
        plt.hist(df[colonne_x], bins=20, color="blue", edgecolor="black")
        plt.xlabel(colonne_x)
        plt.ylabel("Fréquence")
        plt.title(f"Histogramme de {colonne_x}")

    elif type_graphique == "boîte":
        plt.boxplot(df[colonne_x], vert=True, patch_artist=True, boxprops=dict(facecolor="red"))
        plt.ylabel(colonne_x)
        plt.title(f"Boîte à moustaches de {colonne_x}")

    elif type_graphique == "nuage":
        if colonne_y:
            plt.scatter(df[colonne_x], df[colonne_y], color="green", alpha=0.6)
            plt.xlabel(colonne_x)
            plt.ylabel(colonne_y)
            plt.title(f"Répartiton de {colonne_x} selon {colonne_y}")
        else:
            print("Erreur : Veuillez fournir une colonne Y pour un nuage de points.")

    elif type_graphique == "courbe":
        if colonne_y:
            plt.plot(df[colonne_x], df[colonne_y], marker="o", linestyle="-", color="purple")
            plt.xlabel(colonne_x)
            plt.ylabel(colonne_y)
            plt.title(f"Répartiton de {colonne_y} en fonction de {colonne_x}")
            plt.xticks(rotation=45)
        else:
            print("Erreur : Veuillez fournir une colonne Y pour une courbe.")

    else:
        print("Type de graphique non reconnu. Options : 'histogramme', 'boîte', 'nuage', 'courbe'.")

    plt.grid(True)
    plt.show()


#-------------------------------------

counts = data2022['région administrative'].value_counts()

counts.plot(kind='bar')
plt.title("Cinémas par région")
plt.ylabel("Nombre")

# Étiquettes de données
for i, v in enumerate(counts):
    plt.text(i, v, str(v), ha='center', va='bottom')

plt.show()



#------------------------------------
data2022['entrées 2022'] = pd.to_numeric(data2022['entrées 2022'], errors='coerce')
# Moyenne par région
moyennes = data2022.groupby('région administrative')['entrées 2022'].mean().sort_values(ascending=False)


data2022['entrées 2022'] = pd.to_numeric(data2022['entrées 2022'], errors='coerce')
moyennes = data2022.groupby('région administrative')['entrées 2022'].mean().sort_values(ascending=False)


import numpy as np

# Coordonnées X
x = np.arange(len(moyennes))

# Tracer avec des barres plus fines (plus espacées)
plt.figure(figsize=(10, 6))
plt.bar(x, moyennes.values, width=0.5)
plt.title("Entrées moyennes en 2022 par région")
plt.ylabel("Entrées moyennes")
plt.xticks(x, moyennes.index, rotation=45, ha='right')

# Étiquettes
for i, v in enumerate(moyennes):
    plt.text(i, v, f"{int(v)}", ha='center', va='bottom')

plt.tight_layout()
plt.show()

#-----------------------------------------

types = data2022['type d\'établissement'].value_counts()

types.plot(kind='bar')
plt.title("Répartition des cinémas par type d’établissement")
plt.ylabel("Nombre")
plt.xticks(rotation=45)

# Étiquettes de données
for i, v in enumerate(types):
    plt.text(i, v, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.show()

#-----------------------------------------

## Agrégation des données, indicateurs et statistiques sur plusieurs années (tableaux et graphiques) + Export



def evolution_par_annee(d2018, d2019, d2020, d2021, d2022, modalite):
    """
    Calcule l'évolution annuelle d'une modalité numérique (ex. 'fauteuils', 'séances') 
    par département à partir des DataFrames fournis pour les années 2018 à 2022.

    Retourne un DataFrame où chaque ligne correspond à un département, 
    et chaque colonne à une année.

    Paramètres :
    ------------
    d2018, d2019, d2020, d2021, d2022 : pandas.DataFrame
        Données annuelles contenant les colonnes 'DEP' et la modalité choisie.

    modalite : str
        Nom de la colonne numérique à sommer (exemple : 'fauteuils', 'seances', etc.)

    Retour :
    --------
    pandas.DataFrame
        Tableau avec les départements en lignes et les années en colonnes.
    """
    donnees = {2018: d2018, 2019: d2019, 2020: d2020, 2021: d2021, 2022: d2022}
    df_final = pd.DataFrame()

    for annee, df in donnees.items():
        temp = df.groupby('DEP')[modalite].sum().astype(int)
        temp.name = f"{modalite}_{annee}"
        df_final = pd.concat([df_final, temp], axis=1)

    return df_final.reset_index()


evolution_fauteuil = evolution_par_annee(data2018, data2019, data2020, data2021, data2022, "fauteuils")
evolution_ecran = evolution_par_annee(data2018, data2019, data2020, data2021, data2022, "écrans")

def exporter_csv(df, nom_fichier):
    """
    Exporte un DataFrame en fichier CSV.

    Paramètres :
    ------------
    df (pandas.DataFrame) : Le DataFrame à exporter.
    nom_fichier (str)     : Le nom du fichier CSV de sortie (ex : 'resultats.csv').

    Retour :
    --------
    None
    """
    df.to_csv(nom_fichier, index=False, sep=';', encoding='utf-8-sig')
    print(f"Fichier exporté : {nom_fichier}")


exporter_csv(evolution_fauteuil, "C:/Users/Adam/Downloads/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES//evolution.csv")
