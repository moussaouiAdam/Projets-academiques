##################################### CHARGEMENT DES DONNEES #####################################

import csv

def Charger_donnees(nom_du_fichier, ligne_depart = None, ligne_fin = None, *colonnes, filtre = None ):
    """
    Charge les données à partir d'un fichier CSV et les retourne sous forme de liste de dictionnaires.

   :param nom_du_fichier: (str) Le nom du fichier CSV à lire.
   :param ligne_depart: (int, optionnel) Indice de la première ligne à inclure (compris). Si None, commence au début.
   :param ligne_fin: (int, optionnel) Indice de la dernière ligne à inclure (non compris). Si None, va jusqu'à la fin.
   :param colonnes: (*str, optionnel) Noms des colonnes à inclure dans les résultats. Si vide, inclut toutes les colonnes.
   :param filtre: (tuple, optionnel) Filtre sous la forme (nom_colonne, valeur) pour ne conserver que les lignes où 
                  la colonne spécifiée a la valeur donnée.
   :return: (list of dict) Liste des lignes sélectionnées du fichier, chacune représentée comme un dictionnaire.
   """
    with open(nom_du_fichier,"r", encoding = 'ISO-8859-1') as fich: #ouverture en lecture
        data = csv.DictReader(fich, delimiter=";") #lecture- utilisation parseur
        lignes = list(data)
        # Sélectionner une plage de lignes si précisé
        if ligne_depart is not None and ligne_fin is not None:
            lignes = lignes[ligne_depart:ligne_fin+1]

        # Sélectionner seulement certaines colonnes si demandées
        if colonnes:
            lignes = [{col: ligne[col] for col in colonnes if col in ligne} for ligne in lignes]

        return lignes
    
    
# Exemple d'utilisation
fichier_csv = "data\data.csv"

# Charger toutes les données
donnees = Charger_donnees(fichier_csv)
#print(f"Nombre total de lignes : {len(donnees)}")

# Charger toutes les données ciematographique 2021

donnees2021 = Charger_donnees("data\Données cartographie 2021.csv")

# Charger toutes les données ciematographique 2020
donnees2020 = Charger_donnees("data\Données cartographie 2020 -.csv")

# Charger toutes les données ciematographique 2019
donnees2019 = Charger_donnees("data\Données Cartographie 2019.csv")

# Charger toutes les données ciematographique 2018
donnees2018 = Charger_donnees("data\DonnéesCartographie2018.csv")

# Charger une plage de lignes (exemple : 100 à 500)
# donnees_selection = Charger_donnees(fichier_csv, 100, 150)


#  # Charger certaines colonnes (exemple : 'nom', 'fauteuils')
# donnees_colonnes = Charger_donnees(fichier_csv, 100, 500, "nom", "fauteuils")

##################################### VISUALISATION DES DONNEES#####################################

def Apercu_donnees(data, nb_lignes=5):
    """
    Affiche un aperçu formaté d'une liste de dictionnaires représentant des données.

    Chaque dictionnaire est affiché ligne par ligne avec ses paires clé-valeur. 
    Par défaut, seules les 5 premières entrées sont affichées, sauf si un autre
    nombre est précisé via le paramètre `nb_lignes`.

    Paramètres :
    ----------
    data : list[dict]
        Liste contenant les dictionnaires à afficher.
    nb_lignes : int, optionnel
        Nombre de lignes (dictionnaires) à afficher. Par défaut : 5.

    Retour :
    -------
    None
        La fonction affiche les données à la console, mais ne retourne rien.
    """
    for i, salle in enumerate(data[:nb_lignes], start=1):
        print(f"Salle {i} :")
        for cle, valeur in salle.items():
            print(f"  {cle} : {valeur}")
    print("-" * 30)

#Apercu_donnees(donnees, nb_lignes=3)
##################################### TRAITEMENT DES DONNEES #####################################

nouvelles_var = {
    'N° auto': 'num_auto',
    'nom': 'nom',
    'région administrative': 'region_administrative',
    'adresse': 'adresse',
    'code INSEE': 'code_INSEE',
    'commune': 'commune',
    'population de la commune': 'population_de_la_commune',
    'DEP': 'departement',
    'N°UU': 'num_UU',
    'unité urbaine': 'unite_urbaine',
    'population unité urbaine': 'population_unite_urbaine',
    'situation géographique': 'situation_geographique',
    'écrans': 'ecrans',
    "semaines d'activité": 'semaines_d_activite',
    'séances': 'seances',
    'évolution entrées': 'evolution_entrees',
    "tranche d'entrées": 'tranche_d_entrees',
    'programmateur': 'programmateur',
    'AE': 'AE',
    'catégorie Art et Essai': 'categorie_Art_et_Essai',
    'label Art et Essai': 'label_Art_et_Essai',
    'genre': 'genre',
    'multiplexe': 'multiplexe',
    'zone de la commune': 'zone_de_la_commune',
    'nombre de films programmés': 'nombre_de_films_programmes',
    'nombre de films inédits': 'nombre_de_films_inedits',
    'nombre de films en semaine 1': 'nombre_de_films_en_semaine_1',
    'PdM en entrées des films français': 'PdM_en_entrees_des_films_francais',
    'PdM en entrées des films américains': 'PdM_en_entrees_des_films_americains',
    'PdM en entrées des films européens': 'PdM_en_entrees_des_films_europeens',
    'PdM en entrées des autres films': 'PdM_en_entrees_des_autres_films',
    'films Art et Essai': 'films_Art_et_Essai',
    'PdM en entrées des films Art et Essai': 'PdM_en_entrees_des_films_Art_et_Essai'

}


def rennomer_variable(data, dict_vars):
    """
    Renomme les clés des dictionnaires selon une correspondance donnée.

    :param data: (list de dict) Liste de dictionnaires à modifier.
    :param dict_vars: (dict) Dictionnaire de correspondance {ancienne_clé: nouvelle_clé}.
    
    :return: (None) Modifie directement la liste de dictionnaires et affiche le résultat.
    """
    for var in dict_vars:
        for dic in data:
            if var in dic:
                dic[dict_vars[var]] = dic[var]
            del dic[var]
    print(data)

    
    
## Teste de la fonction rennomer
# rennomer_variable (donnees, nouvelles_var)
# rennomer_variable (donnees2021, nouvelles_var)
# rennomer_variable (donnees2020, nouvelles_var)
# rennomer_variable (donnees2019, nouvelles_var)
# rennomer_variable (donnees2018, nouvelles_var)


variable_a_retenir = ["num_auto"]
                    
def selectionne_variable(data, variable):
    """
    Supprime des clés dans chaque dictionnaire qui ne sont pas dans la liste spécifiée.

    :param data: (list de dict) Liste de dictionnaires à modifier.
    :param variable: (list of str) Liste des clés à conserver.
    
    :return: (list de dict) Liste de dictionnaires filtrés.
    """
    for dic in data:
        a_supprimer = [val for val in dic if val not in variable]
        for val in a_supprimer:
            del dic[val]
    return data


### Teste de la fonction filtre
#selectionne_variable(donnees, ["regionCNC", "fauteuils"])
                
                
def filtre(data, dict_condition):
    """
    Filtre une liste de dictionnaires en fonction de plusieurs conditions.

    :param data: (list of dict) Liste de dictionnaires à filtrer.
    :param dict_condition: (dict) Dictionnaire contenant les conditions de filtrage {clé: valeur}.
    
    :return: (list of dict) Liste des dictionnaires correspondant à toutes les conditions.
    """
    return [ligne for ligne in data if all(str(ligne.get(cle)) == str(valeur) for cle, valeur in dict_condition.items())]


## Teste de la fonction selectionne_variable
filtre (donnees, {"fauteuils": "722.0", "num_auto": "204"})
              
  
  
## TRAITEMENT DES ANOMALIES

def valeur_manquante(data, colonne=None):
    """
    Compte le nombre de valeurs manquantes ("", "NA") dans une liste de dictionnaires.

    Si une colonne est spécifiée, seules les valeurs de cette colonne sont vérifiées.
    Sinon, toutes les colonnes de chaque dictionnaire sont prises en compte.

    Paramètres :
    data (list) : Liste de dictionnaires représentant des enregistrements de données.
    colonne (str, optionnel) : Nom de la colonne à vérifier. Si None, toutes les colonnes sont analysées.

    Retour :
    int : Nombre de valeurs manquantes détectées.
    """
    nb = 0
    for dic in data:
        for cle, valeur in dic.items():
            if colonne is not None:
                if cle == colonne:
                    if valeur == "" or valeur == "NA":
                        nb += 1
            elif valeur == "" or valeur == "NA":
                nb += 1      
    return nb

## test de la focntion valeur_manquante
#valeur_manquante(donnees, colonne=None)


from statistics import median

def mediane(data, colonne):
    """
    Calcule la médiane des valeurs numériques d'une colonne spécifiée dans une liste de dictionnaires.

    Les valeurs non convertibles en float (comme des chaînes vides ou du texte) sont ignorées.

    Paramètres :
    data (list) : Liste de dictionnaires représentant des enregistrements de données.
    colonne (str) : Nom de la colonne sur laquelle calculer la médiane.

    Retour :
    float ou None : La médiane des valeurs numériques de la colonne, ou None si aucune donnée valide n’est trouvée.
    """
    l = []
    for dic in data:
        for cle, valeur in dic.items():
            if cle == colonne:
                try:
                    l.append(float(valeur))
                except (ValueError, TypeError):
                    continue
    if not l:
        print("Aucune donnée numérique trouvée dans la colonne.")
        return None
    return median(l)



####teste de la fonction median 
# mediane(donnees, "num_auto")


def remplacer_val_manquante(data, colonne=None, remplace_par=None):
    """
    Remplace les valeurs manquantes ("" ou "NA") par une valeur spécifiée dans une liste de dictionnaires.

    Si une colonne est spécifiée, seules les valeurs manquantes de cette colonne sont remplacées.
    Sinon, la recherche et le remplacement s'appliquent à toutes les colonnes de chaque dictionnaire.

    Paramètres :
    data (list) : Liste de dictionnaires représentant des enregistrements de données.
    colonne (str, optionnel) : Nom de la colonne à traiter. Si None, toutes les colonnes sont traitées.
    remplace_par (any, optionnel) : Valeur à utiliser pour remplacer les données manquantes. Par défaut : None.

    Retour :
    list : Liste de dictionnaires avec les valeurs manquantes remplacées.
    """
    for dic in data:
        for cle, valeur in dic.items():
            if colonne is not None:
                if cle == colonne:
                    if valeur == "" or valeur == "NA":
                        dic[cle] = remplace_par
            elif valeur == "" or valeur == "NA":
                dic[cle] = remplace_par
    return data

## test de la fonction remplacer_val_manquante

remplacer_val_manquante(donnees)


import statistics

def describe(data):
    """
    Affiche des statistiques descriptives de base pour chaque colonne numérique d'une liste de dictionnaires.

    Pour chaque colonne contenant des valeurs numériques (convertibles en float), la fonction calcule :
    - le nombre de valeurs valides (count),
    - la moyenne (mean),
    - la valeur minimale (min),
    - la valeur maximale (max),
    - la médiane (median),
    - l'écart-type (standard deviation),
    - le nombre de valeurs manquantes (missing).

    Paramètres :
    ------------
    data (list) : Liste de dictionnaires représentant des enregistrements de données.
                  Chaque dictionnaire correspond à une ligne, avec les colonnes comme clés.

    Retour :
    --------
    None : La fonction affiche directement les résultats, elle ne retourne pas de valeur.
    """
    # Construction des colonnes à partir des lignes
    columns = {}
    for row in data:
        for key, value in row.items():
            columns.setdefault(key, []).append(value)

    # Calculs statistiques pour les colonnes numériques
    for col, values in columns.items():
        numeric_values = []
        missing_count = 0

        for v in values:
            try:
                numeric_values.append(float(v))
            except:
                missing_count += 1

        if len(numeric_values) == 0:
            continue

        count = len(numeric_values)
        mean = statistics.mean(numeric_values)
        minimum = min(numeric_values)
        maximum = max(numeric_values)
        median = statistics.median(numeric_values)
        std_dev = statistics.stdev(numeric_values) if count > 1 else 0.0  # stdev needs at least 2 values

        print(f"{col}:")
        print(f"  count   = {count}")
        print(f"  mean    = {round(mean, 2)}")
        print(f"  min     = {minimum}")
        print(f"  max     = {maximum}")
        print(f"  median  = {round(median, 2)}")
        print(f"  écart-type = {round(std_dev, 2)}")
        print(f"  nombre valeurs manquantes = {missing_count}")
        print()


#describe(donnees)


##################################### TABLEAU STATISTIQUE #####################################
def tableau_nb_cinema_par_dep(donnees): # La fonction tableau_nb_cinema_par_region compte le nombre de cinémas par région dans les données fournies.
    """
    Compte le nombre de cinémas par département à partir des données fournies.

    Cette fonction parcourt une liste de dictionnaires où chaque dictionnaire représente un cinéma,
    identifie le département associé à chaque cinéma, puis calcule le nombre total de cinémas par département.

    Paramètre :
        donnees (list): Liste de dictionnaires contenant des informations sur les cinémas,
                        avec au moins la clé 'departement'.

    Retour :
        list: Une liste de dictionnaires, chaque dictionnaire contenant :
              - 'departement' : le code du département,
              - 'Nombre de cinema' : le nombre total de cinémas dans ce département.
    """
    tab = {}

    for dic in donnees:
        Dep = dic['departement']
        if Dep in tab:
            tab[Dep]["Nombre de cinema"] += 1
        else:
            tab[Dep] ={
                "departement": Dep,
                "Nombre de cinema": 1
                    }
    return list(tab.values())



def tableau_repartion_materiels(donnees): #La fonction tableau_repartion calcule, pour chaque département, la somme des valeurs d'une modalité donnée (comme le nombre d’écrans, d’entrées, etc.).
    """
    Calcule la répartition d'une modalité numérique (ex. : nombre d’écrans, d’entrées) par département.

    Pour chaque dictionnaire de la liste d'entrée, la fonction récupère la valeur associée à une clé donnée (la modalité),
    l'associe au département concerné, puis additionne les valeurs pour obtenir un total par département.

    Paramètres :
        donnees (list): Liste de dictionnaires contenant des données sur les départements et la modalité.
                        Chaque dictionnaire doit contenir une clé 'DEP' pour le département,
                        et une clé correspondant à la modalité à agréger.
        modalité (str): Le nom de la modalité dont les valeurs doivent être additionnées par département.

    Retour :
        list: Une liste contenant un seul dictionnaire :
              - Les clés sont les départements (code 'DEP'),
              - Les valeurs sont la somme des valeurs numériques de la modalité pour chaque département.
              - Une entrée "Departement": "Nombre de <modalité>" est incluse en tête pour servir d'en-tête.
    """


    tab = {}
    for dic in donnees:
        Dep = dic['departement']
        ecrans = float(dic['ecrans'])
        fauteuils = float(dic['fauteuils'])
        if Dep not in tab:
            tab[Dep] = {
            "departement": Dep,  # Tu peux remplacer par nom complet si disponible
            "Nombre d'ecran": ecrans,
            "Nombre de fauteuil": fauteuils
        }
        else:
            tab[Dep]['Nombre de fauteuil'] += fauteuils
            tab[Dep]["Nombre d'ecran"] += ecrans
    return list(tab.values())

############Appel####################
#tableau_materiel = tableau_repartion_materiels(donnees)
 
 
 
 

def tableau_repartion_programmation(donnees):
    """
    Calcule la répartition moyenne de la programmation cinématographique par département.

    Cette fonction agrège les données relatives aux séances, semaines d'activité, nombre de films par semaine,
    ainsi que la part de marché moyenne des films français et américains pour chaque département.
    Elle utilise le nombre de cinémas par département pour calculer les parts de marché moyennes.

    Paramètre :
        donnees (list): Liste de dictionnaires contenant des informations sur la programmation cinématographique,
                        avec au moins les clés suivantes : 'departement', 'seances', 'semaines_d_activite',
                        'nombre_de_films_en_semaine_1', 'PdM_en_entrees_des_films_francais',
                        'PdM_en_entrees_des_films_americains'.

    Retour :
        list: Une liste de dictionnaires, chaque dictionnaire correspondant à un département, avec les clés :
              'departement', 'seances', 'semaines d'activite', 'nombre de films en semaine',
              'Part des marchés moyen des films FR', 'Part des marchés moyen des films AM'.
              Les valeurs des parts de marché sont des moyennes par cinéma arrondies à deux décimales.
              Les autres valeurs numériques sont arrondies à l'entier le plus proche.
    """

    nbcine = tableau_nb_cinema_par_dep(donnees)
    # Convertir nbcine en dict {departement: nombre_de_cinema} pour accès rapide
    nbcine_dict = {d['departement']: d['Nombre de cinema'] for d in nbcine}

    tab = {}
    for dic in donnees:
        Dep = dic['departement']
        seances = float(dic['seances'])
        semaines_d_activite = float(dic['semaines_d_activite'])
        nombre_de_films_en_semaine_1 = float(dic['nombre_de_films_en_semaine_1'])
        PdM_fr = float(dic['PdM_en_entrees_des_films_francais'].replace(',', '.'))
        PdM_am = float(dic['PdM_en_entrees_des_films_americains'].replace(',', '.'))

        if Dep not in tab: 
            tab[Dep] = {
                'departement': Dep,
                "seances": seances,
                "semaines d'activite": semaines_d_activite,
                "nombre de films en semaine": nombre_de_films_en_semaine_1,
                "Part des marchés moyen des films FR": PdM_fr,
                "Part des marchés moyen des films AM": PdM_am
            }
        else:
            tab[Dep]['seances'] += seances
            tab[Dep]["semaines d'activite"] += semaines_d_activite
            tab[Dep]["nombre de films en semaine"] += nombre_de_films_en_semaine_1
            tab[Dep]['Part des marchés moyen des films FR'] += PdM_fr
            tab[Dep]['Part des marchés moyen des films AM'] += PdM_am

    # Après avoir rempli tab, on normalise et arrondit
    for dep in tab:
        if dep in nbcine_dict and nbcine_dict[dep] != 0:
            tab[dep]["Part des marchés moyen des films FR"] /= nbcine_dict[dep]
            tab[dep]["Part des marchés moyen des films AM"] /= nbcine_dict[dep]

        tab[dep]["Part des marchés moyen des films FR"] = round(tab[dep]["Part des marchés moyen des films FR"], 2)
        tab[dep]["Part des marchés moyen des films AM"] = round(tab[dep]["Part des marchés moyen des films AM"], 2)
        tab[dep]["seances"] = round(tab[dep]["seances"])
        tab[dep]["semaines d'activite"] = round(tab[dep]["semaines d'activite"])
        tab[dep]["nombre de films en semaine"] = round(tab[dep]["nombre de films en semaine"])

    return list(tab.values())

############Appel####################
tableau_prog=tableau_repartion_programmation(donnees)




def tableau_repartion_frequentation(donnees):
    """
    Calcule la répartition de la fréquentation cinématographique par département.

    Cette fonction agrège le nombre total d'entrées en 2022 ainsi que le nombre total de semaines
    d'activité pour chaque département à partir des données fournies.

    Paramètre :
        donnees (list): Liste de dictionnaires contenant des informations sur la fréquentation,
                        avec au moins les clés suivantes : 'departement', 'entrees_2022', 'semaines_d_activite'.

    Retour :
        list: Une liste de dictionnaires, chaque dictionnaire représentant un département avec les clés :
              'departement', "Nombre d'entrées", "Nombre de semaine d'activité".
              Les valeurs sont des totaux cumulés par département.
    """

    tab={}
    for dic in donnees:
        Dep = dic['departement']
        entrees_2022 = float(dic['entrees_2022'])
        semaines_d_activite = float(dic['semaines_d_activite'])
        if Dep not in tab :
            tab[Dep]= {
                'departement': Dep,
               "Nombre d'entrées": entrees_2022,
                "Nombre de semaine d'activité": semaines_d_activite
                }
        else:
            tab[Dep]["Nombre d'entrées"] += entrees_2022
            tab[Dep]["Nombre de semaine d'activité"] += semaines_d_activite
    return list(tab.values())
            
############Appel####################
tableau_freq=tableau_repartion_frequentation(donnees)



def ratio_fauteuils_par_commune(donnees):
    """
    Calcule, pour chaque commune, le ratio entre le nombre de fauteuils de cinéma et la population.

    La fonction regroupe les données par code INSEE de commune, additionne le nombre de fauteuils si plusieurs
    entrées concernent la même commune, puis calcule le ratio fauteuils/population.
    Le ratio est arrondi à 8 décimales. Si la population est nulle, le ratio est fixé à 0.

    Paramètre :
        donnees (list): Liste de dictionnaires contenant au minimum les clés suivantes :
                        - 'code_INSEE' : code de la commune,
                        - 'fauteuils' : nombre de fauteuils dans la commune,
                        - 'population_de_la_commune' : population de la commune.

    Retour :
        list: Une liste de dictionnaires, chacun représentant une commune avec les clés :
              - 'commune' : code INSEE de la commune,
              - 'Population' : population de la commune,
              - 'Nombre de fauteuil' : total de fauteuils dans la commune,
              - 'Ratio fauteuil/population' : ratio calculé (arrondi à 8 chiffres après la virgule).
    """
    tab = {}
    
    for dic in donnees:
        code_insee = dic['code_INSEE']
        fauteuils = float(dic['fauteuils'])
        population = float(dic['population_de_la_commune'])

        if code_insee not in tab:
            tab[code_insee] = {
                'commune': code_insee,  # Tu peux remplacer par nom complet si disponible
                'Population': population,
                'Nombre de fauteuil': fauteuils
            }
        else:
            tab[code_insee]['Nombre de fauteuil'] += fauteuils

    # Calcul du ratio fauteuils/population
    for commune in tab.values():
        pop = commune['Population']
        fauteuils = commune['Nombre de fauteuil']
        if pop > 0:
            commune['Ratio fauteuil/population'] = round(fauteuils / pop, 8)
        else:
            commune['Ratio fauteuil/population'] = 0

    return list(tab.values())



def nb_cine_par_tranche (donnees) :
    """
    Compte le nombre de cinémas pour chaque tranche d’entrées.

    La fonction parcourt une liste de dictionnaires, repère la clé 'tranche_d_entrees',
    et compte le nombre d’occurrences pour chaque modalité de tranche d’entrées.
    Le résultat est stocké dans un dictionnaire dont la première entrée sert d’en-tête.

    Paramètre :
        donnees (list): Liste de dictionnaires contenant au moins la clé 'tranche_d_entrees'
                        correspondant à une classification des cinémas par volume d’entrées.

    Retour :
        list: Une liste contenant un seul dictionnaire :
              - La première entrée est : {"Tranche d'entrées": "Nombre de cinéma"},
              - Les autres paires clé-valeur correspondent à chaque tranche d’entrées
                et au nombre de cinémas dans cette tranche.
    """
    tab={}
    tab={"Tranche d'entrées": "Nombre de cinéma"}
    for dic in donnees : 
        for cle , valeurs in dic.items() :
            if cle == "tranche_d_entrees" :
                if valeurs in tab:
                    tab[valeurs]=tab[valeurs]+1
                else :
                    tab[valeurs] = 1
    return [tab]


################################ TABLEAU DE FREQUENCE ######################################


def tableau_frequence(donnees):
    """
    Calcule la fréquence relative du nombre de séances de cinéma par département.

    La fonction additionne le nombre total de séances pour chaque département, puis calcule
    la part (fréquence relative) de chaque département par rapport au total des séances
    enregistrées dans les données.

    Paramètre :
        donnees (list): Liste de dictionnaires contenant les clés suivantes :
                        - 'DEP' : code du département,
                        - 'seances' : nombre de séances de cinéma dans ce département.

    Retour :
        dict: Un dictionnaire où :
              - les clés sont les départements (code 'DEP'),
              - les valeurs sont les fréquences relatives (valeurs entre 0 et 1),
                représentant la proportion des séances de chaque département par rapport au total.
    """
    tab = {}
    total = 0

    # 1. Accumuler les séances par département
    tab['departement'] = "frquence"
    for dic in donnees:
        dep = dic['departement']
        seances = float(dic['seances'])

        if dep not in tab:
            tab[dep] = 0
        tab[dep] += seances
        total += seances

    # 2. Calculer la fréquence relative
    for dep in tab:
        if dep != "departement":
            tab[dep] = tab[dep] / total if total != 0 else 0

    return [tab]


################################ AGREGATION ######################################


def evolution_par_annee(d2018, d2019, d2020, d2021, d2022, modalité):
    """
    Calcule l'évolution annuelle d'une modalité numérique (ex. 'fauteuils', 'séances') 
    par département à partir des données fournies pour les années 2018 à 2021.

    La fonction retourne une liste de dictionnaires, chaque dictionnaire correspondant 
    à une année, au format :
        [{'Département': 'Nombre de <modalité> <année>', '75': total, '59': total, ...}, ...]

    Paramètres :
    ------------
    d2018, d2019, d2020, d2021 : list
        Listes de dictionnaires contenant les données pour chaque année.
        Chaque dictionnaire doit contenir au moins les clés :
        - 'departement' (code département)
        - la clé correspondant à la modalité (ex. 'fauteuils', 'séances')

    modalité : str
        Nom de la clé dans les dictionnaires indiquant la valeur numérique à sommer 
        (exemple : 'fauteuils', 'séances', etc.)

    Retour :
    --------
    list
        Liste de dictionnaires, un par année, avec le format :
        {'Département': 'Nombre de <modalité> <année>', '75': total, '59': total, ...}
    """
    donnees = {2018: d2018, 2019: d2019, 2020: d2020, 2021: d2021, 2022: d2022}
    resultats = []

    for annee in donnees:
        tab = {"Département": f"Nombre de {modalité} {annee}"}
        for dic in donnees[annee]:
            if "departement" in dic and modalité in dic:
                dep = dic["departement"]
                val = dic[modalité]
                try:
                    nb = int(val)
                except:
                    continue
                if dep in tab:
                    tab[dep] += nb
                else:
                    tab[dep] = nb
        resultats.append(tab)

    return resultats

### TEST
## evolution_fauteuil = evolution_par_annee(donnees2018, donnees2019, donnees2020, donnees2021, donnees, "fauteuils")
## evolution_ecran = evolution_par_annee(donnees2018, donnees2019, donnees2020, donnees2021, donnees, "ecrans")

####################### Exporter les données ################################

def exporterdict(datadict, file):
    """
    Exporte les données dans un fichier CSV.
    :param datalist: (list of list) Données à sauvegarder.
    :param file: (str) Nom du fichier de sortie.
    """
    import csv

    if len(datadict) == 0:
        print("Erreur : Aucune donnée à exporter.")
        return
    
    keys = datadict[0].keys()
    
    with open(file+".csv", mode='w', newline='', encoding = 'ISO-8859-1') as fichier:
        writer = csv.writer(fichier, delimiter = ";", lineterminator = "\n")
        writer.writerow(keys)
        
        for i in datadict :
            liste=[]
            for cle, valeur in i.items():

                liste.append(valeur)
            writer.writerow(liste)
        print(f"Données exportées avec succès dans le fichier '{file}'.")
         
  
#exporterdict(nom, "//ad.univ-lille.fr/Etudiants/Homedir-etu/346300/Documents/SEMESTRE 2/SAE/python/Sae Mousaoui-Adam-Bououden-Yasmine/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES/nbcinema_region")
#n = ratio_fauteuils_par_commune(donnees)
#exporterdict(prg, "//ad.univ-lille.fr/Etudiants/Homedir-etu/346300/Documents/SEMESTRE 2/SAE/python/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES/progof")
# exporterdict(evolution_ecran, "C:/Users/Adam/Downloads/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES/evolution_ecran")
#exporterdict(tableau_freq, "C:/Users/yasmi/OneDrive/Documents/SEMESTRE 2/SAE/python/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES/tableau_freq")


####################### MENU GENERAL ################################

def menu_general():
    """
    Affiche le menu principal de l'application cinéma.
    Retour :
        int : Le choix de l'utilisateur.
    """
    print("\n========= MENU GENERAL - CINEMA =========")
    print("1. Description des Données")
    print("2. Visualisation des Données")
    print("3. Statistiques & Indicateurs")
    print("4. Analyse d’Évolution")
    print("0. Quitter")
    print("=========================================")
    return int(input("Veuillez entrer votre choix : "))


def gestion_choix(choix):
    if choix == 1:
        print("\n=== DESCRIPTION DES DONNEES ===")
        print(f"Nombre total de lignes : {len(donnees)}")
        print(f"Nombre de colonnes : {len(donnees[0]) if donnees else 0}")
        print(f"Valeurs manquantes (toutes colonnes) : {valeur_manquante(donnees)}")

    elif choix == 2:
        print("\n=== VISUALISATION DES DONNEES ===")
        nb = int(input("Combien de lignes souhaitez-vous afficher ? "))
        Apercu_donnees(donnees, nb_lignes=nb)

    elif choix == 3:
        print("\n=== STATISTIQUES & INDICATEURS ===")
        print("1. Statistiques descriptives")
        print("2. Nombre de cinémas par département")
        print("3. Répartition d’une modalité par département")
        print("4. Ratio fauteuil/population par commune")
        print("5. Fréquence des séances par département")
        print("6. Nombre de cinémas par tranche d’entrées")
        print("7. Répartition du matériel par département")
        print("8. Répartition de la programmation par département")
        print("9. Répartition de la fréquentation par département")
        sous_choix = int(input("Votre choix : "))

        if sous_choix == 1:
            describe(donnees)
        elif sous_choix == 2:
            resultat = tableau_nb_cinema_par_dep(donnees)
            print(resultat)
            exporterdict(resultat, "C:/Users/Adam/Downloads/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES//nb_cinemas_par_departement")
        elif sous_choix == 3:
            mod = input("Nom de la modalité à répartir (ex: ecrans, fauteuils, seances) : ")
            resultat = tableau_repartion_materiels(donnees)  # à adapter si modalité personnalisée
            print(resultat)
            exporterdict(resultat, f"EXPORT/STATISTIQUES/repartition_{mod}")
        elif sous_choix == 4:
            resultat = ratio_fauteuils_par_commune(donnees)
            print(resultat)
            exporterdict(resultat, "C:/Users/Adam/Downloads/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES//ratio_fauteuils_par_commune")
        elif sous_choix == 5:
            resultat = tableau_frequence(donnees)
            print(resultat)
            exporterdict(resultat, "C:/Users/Adam/Downloads/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES//frequence_seances_par_departement")
        elif sous_choix == 6:
            resultat = nb_cine_par_tranche(donnees)
            print(resultat)
            exporterdict(resultat, "C:/Users/Adam/Downloads/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES//nb_cine_par_tranche")
        elif sous_choix == 7:
            resultat = tableau_repartion_materiels(donnees)
            print(resultat)
            exporterdict(resultat, "C:/Users/Adam/Downloads/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES//repartition_materiels")
        elif sous_choix == 8:
            resultat = tableau_repartion_programmation(donnees)
            print(resultat)
            exporterdict(resultat, "C:/Users/Adam/Downloads/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES//repartition_programmation")
        elif sous_choix == 9:
            resultat = tableau_repartion_frequentation(donnees)
            print(resultat)
            exporterdict(resultat, "C:/Users/Adam/Downloads/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES//repartition_frequentation")
        else:
            print("Choix invalide.")

    elif choix == 4:
        print("\n=== EVOLUTION ANNUELLE (2018-2022) ===")
        mod = input("Nom de la modalité à étudier (ex: fauteuils, ecrans, seances) : ")
        resultats = evolution_par_annee(donnees2018, donnees2019, donnees2020, donnees2021, donnees, mod)
        for ligne in resultats:
            print(ligne)
        exporterdict(resultats, f"C:/Users/Adam/Downloads/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/EXPORT/STATISTIQUES//evolution_{mod}")

    elif choix == 0:
        print("\nFin du programme.")
        exit()

    else:
        print("Choix invalide. Veuillez réessayer.")


        
# Programme principal
if __name__ == "__main__":
    while True:
        choix = menu_general()
        gestion_choix(choix)


                                                                                                                                                                                                                                                            




















    
