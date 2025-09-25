# Charger les donnÃ©es

import csv

def Charger_donnees(nom_du_fichier):
    """
    Charge les donnÃ©es Ã  partir d'un fichier CSV et les retourne sous forme de liste.
    :param nom_du_fichier: (str) Le nom du fichier Ã  lire.
    :return: (list of list) Les donnÃ©es lues.
    """
    with open(nom_du_fichier,"r", encoding = 'ISO-8859-1') as fich: #ouverture en lecture
        data = csv.reader(fich, delimiter=";") #lecture- utilisation parseur
        return list(data)
       
Effectif = Charger_donnees("data/effectif-metiers_sncf.csv")
Recrutement = Charger_donnees("data/recrutement-metiers-sncf.csv")
repartition_genre_effectif = Charger_donnees("data/repartition-genre-effectif.csv")

def Afficher_Donnees(datalist):

     """
     parmètre : datalist (liste)
     permet d'afficher la gande liste sous forme de petites listes 
     comptenant chacune les informations d'un enregistrement'
     """ 

     for ligne in datalist:
         if len(datalist[0]) >= 5:  # Vérifie qu'il y a au moins 5 colonnes
             print(f"{ligne[0]:<6}{ligne[1]:<60}{ligne[2]:<40}{ligne[3]:<8}{ligne[4]:<6}")
         else:
             print("Ligne incomplète")
    

# Renommer les variables
def renommer_variables(datalist):
    """
    Renomme les variables (en-tÃªtes) de la premiÃ¨re ligne de la liste de donnÃ©es.
    :param datalist: (list of list) DonnÃ©es, la premiÃ¨re ligne contient les variables.
    :return: (list of list) DonnÃ©es avec variables renommÃ©es.
    """
    if len(datalist) == 0 :
        print("Erreur : Aucune donnÃ©e ou en-tÃªtes introuvables.")
        return datalist

    print("\n=== Renommer les variables ===")
    for i in range(len(datalist[0])):
        variable = datalist[0][i]
        print(f"Variable actuelle : {variable}")
        nouveau_nom = input(f"Entrez un nouveau nom pour '{variable}' (ou appuyez sur EntrÃ©e pour conserver) : ")
        if nouveau_nom.strip():
            datalist[0][i] = nouveau_nom.strip()
    return datalist


# Trouver l'indice d'une variable
def index_variable(datalist, variable):
    """
    Trouve l'indice d'une variable donnÃ©e.
    :param datalist: (list of list) DonnÃ©es, la premiÃ¨re ligne contient les variables.
    :param variable: (str) Nom de la variable.
    :return: (int) Indice de la variable ou -1 si elle n'existe pas.
    """
    if len(datalist) == 0 or len(datalist[0]) == 0:
        print("Erreur : Aucune donnÃ©e ou en-tÃªtes introuvables.")
        return -1
    
    for i in range(len(datalist[0])):
        if datalist[0][i] == variable:
            return i
    print(f"La variable '{variable}' n'existe pas.")
    return -1


# Exporter les données
def exporter(datalist, file):
    """
    Exporte les données dans un fichier CSV.
    :param datalist: (list of list) Données à sauvegarder.
    :param file: (str) Nom du fichier de sortie.
    """
    import csv
    if len(datalist) == 0:
        print("Erreur : Aucune donnée à exporter.")
        return
    
    with open(file+".csv", mode='w', newline='', encoding = 'ISO-8859-1') as fichier:
        writer = csv.writer(fichier, delimiter = ";", lineterminator = "\n")
        for ligne in datalist:
            writer.writerow(ligne)
    print(f"Données exportées avec succès dans le fichier '{file}'.")
    
    
# Extraction avec un seul critère
def extraction_avec_critere_unique(liste_data, variable, valeur):
    """
    Filtre les données selon un critère unique pour une liste de listes.

    Paramètres :
        - liste_data : Liste de listes contenant les données.
        - variable : la variable correspondant a la valeur.
        - valeur : La valeur correspondant au critère.

    Renvoie :
        - Une liste contenant les sous-listes filtrées.
    """
    resultat = []  # Liste pour stocker les sous-listes qui correspondent au critère
    indice_critere = index_variable(liste_data, variable)
    for sous_liste in liste_data:
        if len(sous_liste) > indice_critere and sous_liste[indice_critere] == valeur:
            resultat.append(sous_liste)  # Ajouter la sous-liste au résultat
    return resultat


def extraire_plus_criteres(data):
    """
    Extrait les données en appliquant plusieurs critères de filtrage successifs.

    L'utilisateur peut ajouter un ou plusieurs critères en interagissant avec le programme.
    Chaque critère correspond à une colonne et une valeur spécifique à filtrer.

    Paramètres :
    data (list) : Liste de listes représentant un tableau de données.

    Retourne :
    list : Liste contenant les sous-ensembles de données filtrés pour chaque critère appliqué.
    """
    resultat = []
    choix = int(input('Taper 1 pour ajouter un critere, sinon taper 0 :'))
    while len(data) > 0 and choix == 1:
        variable = str(input("Entrez le nom de la variable :"))
        i_variable = index_variable(data,variable)	
        valeur = str(input("Entrez la valeur de la variable que vous voulez filtre :"))
        donne = extraction_avec_critere_unique(data, variable, valeur)
        resultat.append(donne)
        choix = int(input('Taper 1 pour ajouter un critere, sinon taper 0 :'))  
    return resultat




# Extraction avec deux critère
def extraction_avec_deux_criteres(liste_data, variable1, valeur1, variable2, valeur2):
    """
    Filtre les données selon deux critères pour une liste de listes.

    Paramètres :
        - liste_data : Liste de listes contenant les données.
        - indice_critere1 : L'indice de la première colonne à utiliser comme critère.
        - valeur1 : La valeur du premier critère.
        - indice_critere2 : L'indice de la deuxième colonne à utiliser comme critère.
        - valeur2 : La valeur du deuxième critère.

    Renvoie :
        - Une liste contenant les sous-listes filtrées.
    """
    resultat = []  # Liste pour stocker les sous-listes qui correspondent aux critères
    indice_critere1 = index_variable(liste_data, variable1)
    indice_critere2 = index_variable(liste_data, variable2)
    for sous_liste in liste_data:
        if (len(sous_liste) > max(indice_critere1, indice_critere2) and 
            sous_liste[indice_critere1] == valeur1 and 
            sous_liste[indice_critere2] == valeur2):
            resultat.append(sous_liste)  # Ajouter la sous-liste au résultat
    return resultat


# Retourne toutes les valeurs de la colonne variable.
def les_valeurs(data, variable):
    """
    Retourne toutes les valeurs de la colonne correspondant à l'indice donné.

    Paramètres :
    data (list) : Liste de listes représentant un tableau de données.
    variable (int) : Indice de la colonne à extraire.
    i_varibale (str) : indice de la variable
    Retourne :
    list : Liste contenant les valeurs de la colonne spécifiée.
    """
    colonne = []
    i_varibale = index_variable(data, variable)
    for liste in data[1:]:
        for sous_liste in range(len(liste)):
            if sous_liste == i_varibale:
                colonne.append(liste[sous_liste])
    return colonne


# Retourne les modalités d’une variable qualitative
def les_modalites(data, variable_quali):
    """
    Retourne les modalités uniques d'une variable qualitative spécifiée.

    Paramètres :
    data (list) : Liste de listes représentant un tableau de données.
    variable_quali (int) : Indice de la colonne qualitative.

    Retourne :
    list : Liste des modalités uniques de la colonne spécifiée.
    """
    variable = []
    i_variable = index_variable(data, variable_quali)
    for liste in data[1:]:
        for sous_liste in range(len(liste)):
            if sous_liste == i_variable :
                if liste[i_variable] != "":
                    if liste[i_variable] not in variable: 
                        variable.append(liste[i_variable])
    return variable

#les_modalites(Effectif, "Metier")

# Retourne la valeur maximale d’une variable quantitative passée en paramètre
def max_variable(data, variable_quanti):
    """
    Retourne la valeur maximale d'une variable quantitative spécifiée.

    Paramètres :
    data (list) : Liste de listes représentant un tableau de données.
    variable_quanti (int) : Indice de la colonne quantitative.

    Retourne :
    int : Valeur maximale de la colonne spécifiée.
    """
    i_varibale = index_variable(data, variable_quanti)
    maxi = data[1][i_varibale]
    for liste in data[1:]:
        for sous_liste in range(len(liste)):
            if sous_liste == i_varibale:
                if int(liste[i_varibale]) > int(maxi):
                    maxi = liste[i_varibale]
    return maxi


# Retourne la valeur minimale d’une variable quantitative passée en paramètre
def min_variable(data, variable_quanti):
    """
    Retourne la valeur minimale d'une variable quantitative spécifiée.

    Paramètres :
    data (list) : Liste de listes représentant un tableau de données.
    variable_quanti (int) : Indice de la colonne quantitative.

    Retourne :
    int : Valeur minimale de la colonne spécifiée.
    """
    i_varibale = index_variable(data, variable_quanti)
    mini = data[1][i_varibale]
    for liste in data[1:]:
        for sous_liste in range(len(liste)):
            if sous_liste == i_varibale:
                if int(liste[i_varibale]) < int(mini):
                    mini = liste[i_varibale]
    return mini


# Retourne la valeur moyenne d’une variable quantitative passée en paramètre
def moyenne_variable(data, variable_quanti):
    """
    Retourne la valeur moyenne d'une variable quantitative spécifiée.

    Paramètres :
    data (list) : Liste de listes représentant un tableau de données.
    variable_quanti (int) : Indice de la colonne quantitative.

    Retourne :
    float : Moyenne des valeurs de la colonne spécifiée.
    """
    somme = 0
    nb_valeur = 0
    i_varibale = index_variable(data, variable_quanti)
    for liste in data[1:]:
             if liste[i_varibale] != " ":
                nb_valeur += 1
                somme += int(liste[i_varibale])
    return (somme)/nb_valeur


# Retourne la somme des valeurs d’une variable quantitative passée en paramètre    
def total_variable(data, variable_quanti):
    """
    Retourne la somme des valeurs d'une variable quantitative spécifiée.

    Paramètres :
    data (list) : Liste de listes représentant un tableau de données.
    variable_quanti (int) : Indice de la colonne quantitative.

    Retourne :
    int : Somme des valeurs de la colonne spécifiée.
    """
    somme = 0
    i_varibale = index_variable(data, variable_quanti)
    for liste in data[1:]:
        for sous_liste in range(len(liste)):
            if sous_liste == i_varibale:
                somme += int(liste[sous_liste])
    return somme



# Retourne la somme des effectifs
def effectif_trois_critere(data, variable1, critere1, variable2, critere2, variable3, critere3):
    """
    Calcule et retourne l'effectif total pour une combinaison de trois critères donnés.

    Paramètres :
    data (list) : Liste de listes représentant un tableau de données.
    variable1 (str) : Nom de la première variable à filtrer.
    critere1 (str) : Valeur du critère pour la première variable.
    variable2 (str) : Nom de la deuxième variable à filtrer.
    critere2 (str) : Valeur du critère pour la deuxième variable.
    variable3 (str) : Nom de la troisième variable à filtrer.
    critere3 (str) : Valeur du critère pour la troisième variable.

    Retourne :
    int : Somme des effectifs correspondant aux trois critères spécifiés.
    """
    somme = 0
    i_variable1 = data[0].index(variable1)
    i_variable2 = data[0].index(variable2)
    i_variable3 = data[0].index(variable3)
    for liste in data[1:]:
        if liste[i_variable1] == critere1 and liste[i_variable2] == critere2 and liste[i_variable3] == critere3:
            somme += int(liste[4])
    return somme



def effectif_deux_critere(data, variable1, critere1, variable2, critere2):
    """
    Calcule et retourne l'effectif total pour une combinaison de deux critères donnés.

    Paramètres :
    data (list) : Liste de listes représentant un tableau de données.
    variable1 (str) : Nom de la première variable à filtrer.
    critere1 (str) : Valeur du critère pour la première variable.
    variable2 (str) : Nom de la deuxième variable à filtrer.
    critere2 (str) : Valeur du critère pour la deuxième variable.

    Retourne :
    int : Somme des effectifs correspondant aux deux critères spécifiés.
    """
    somme = 0
    i_variable1 = data[0].index(variable1)
    i_variable2 = data[0].index(variable2)
    for liste in data[1:]:
        if liste[i_variable1] == critere1 and liste[i_variable2] == critere2:
            somme += int(liste[4])
    return somme


import os

def creer_dossier(nom_dossier):
    """
    Crée un dossier avec le nom spécifié s'il n'existe pas déjà.

    Paramètres :
    nom_dossier (str) : Chemin ou nom du dossier à créer.

    Actions :
    - Si le dossier n'existe pas, il est créé, et un message de confirmation est affiché.
    - Si le dossier existe déjà, un message indique qu'il est déjà présent.

    Retourne :
    None
    """
    if not os.path.exists(nom_dossier):
        os.makedirs(nom_dossier)
        print(f"Le dossier '{nom_dossier}' a été créé avec succès.")
    else:
        print(f"Le dossier '{nom_dossier}' existe déjà.")


creer_dossier("EXPORT/STATISTIQUES/Repartition_sexe ")
creer_dossier("EXPORT/STATISTIQUES/Repartition_sexe/Par_annee ")
creer_dossier("EXPORT/STATISTIQUES/Repartition_sexe/Par_metier ")
creer_dossier("EXPORT/STATISTIQUES/Repartition_sexe/Par_contrat ")
creer_dossier("EXPORT/STATISTIQUES/Evolution _effectif ")
creer_dossier("EXPORT/STATISTIQUES/Comparaison ")
exporter(repartition_genre_effectif, "EXPORT/STATISTIQUES/Comparaison/repartition_genre_effectif")


# Repartiton
def repartition_annee(data, data1, variable, critere):
    """
    Calcule et retourne la répartition des effectifs par métier pour une année donné.

    Paramètres :
    data (list) : Liste de listes représentant un tableau de données principal.
    data1 (list) : Liste de listes représentant un second tableau de données.
    variable (str) : Nom de la variable à analyser (exemple : "Année").
    critere (str) : Valeur du critère à analyser (exemple : "2023").

    Retourne :
    list : Tableau contenant :
           - Les en-têtes ("Metier", "Effectif_Total", "Effectif_H", "Effectif_F", etc.)
           - Les données pour chaque métier, incluant les effectifs totaux, masculins, féminins, et les recrutements pour chaque sexe.
    """
    En_tete = ["Metier", "Effectif_Total", "Effectif_H", "Effectif_F", "Recrutement_total", "Recrutement_H", "Recrutement_F"]
    print(f"Repartition de {critere}")
    variable1 = En_tete[0]
    lesmodalites = les_modalites(data, variable1)
    Resultat = []
    Resultat.append(En_tete) 
    for modalite in lesmodalites:
        l = [modalite]
        l1 = effectif_trois_critere(data, variable, critere, "Metier", modalite, "Sexe", "Homme")
        l2 = effectif_trois_critere(data, variable, critere, "Metier", modalite, "Sexe", "Femme")
        l3 = effectif_trois_critere(data1, variable, critere, "Metier", modalite, "Sexe", "Homme")
        l4 = effectif_trois_critere(data1, variable, critere, "Metier", modalite, "Sexe", "Femme")
        l.append(str(l1 + l2))
        l.append(str(l1))
        l.append(str(l2))
        l.append(str(l3 + l4))
        l.append(str(l3))
        l.append(str(l4))
        Resultat.append(l)
    return Resultat


repartition_2020 = repartition_annee(Effectif, Recrutement, "Annee", "2020")
repartition_2019 = repartition_annee(Effectif, Recrutement, "Annee", "2019")

exporter(repartition_2020, "EXPORT/STATISTIQUES/Repartition_sexe/Par_annee/Repartition_2020")
exporter(repartition_2019, "EXPORT/STATISTIQUES/Repartition_sexe/Par_annee/Repartition_2019")

def repartition_metier_ou_contrat(data, data1, variable, critere):
    """
    Calcule et retourne la répartition des effectifs selon un type de contrat ou un métier donné.

    Paramètres :
    data (list) : Liste de listes représentant un tableau de données principal.
    data1 (list) : Liste de listes représentant un second tableau de données.
    variable (str) : Nom de la variable à analyser (exemple : "Contrat" ou "Métier").
    Critere (str) : Valeur du critère à analyser.

    Retourne :
    list : Tableau contenant :
           - Les en-têtes ("Contrat", "Effectif_total", "Effectif_H", "Effectif_F", etc.).
           - Les données pour chaque modalité, incluant les effectifs totaux, masculins, féminins, et les recrutements pour chaque sexe.
    """
    En_tete = ["Annee", "Effectif_total", "Effectif_H", "Effectif_F" ,"Recrutement_total", "Recrutement_H" ,"Recrutement_F"]
    print(f"Repartition de {variable}")
    variable1 = En_tete[0]
    lesmodalites = les_modalites(data, variable1)
    Resultat = []
    Resultat.append(En_tete) 
    for modalite in lesmodalites:
        l = [modalite]
        l1 = effectif_trois_critere(data,"Annee", modalite, variable, critere, "Sexe", "Homme")
        l2 = effectif_trois_critere(data, "Annee", modalite, variable, critere, "Sexe", "Femme")
        l3 = effectif_trois_critere(data1, "Annee", modalite, variable, critere, "Sexe", "Homme")
        l4 = effectif_trois_critere(data1, "Annee", modalite, variable, critere, "Sexe", "Femme")
        l.append(str(l1 + l2))
        l.append(str(l1))
        l.append(str(l2))
        l.append(str(l3 + l4))
        l.append(str(l3))
        l.append(str(l4))
        Resultat.append(l)
    return Resultat

repartition_metier_ou_contrat(Effectif, Recrutement, "Contrat", "Cadre permanent")

repartition_par_Manager_de_proximite_maitrise = repartition_metier_ou_contrat(Effectif, Recrutement, "Metier", "Manager de proximité, maitrise")
repartition_par_Conducteurs = repartition_metier_ou_contrat(Effectif, Recrutement, "Metier", "Conducteurs")
repartition_par_Cadre_permanent = repartition_metier_ou_contrat(Effectif, Recrutement, "Contrat", "Cadre permanent")
repartition_par_Contractuels = repartition_metier_ou_contrat(Effectif, Recrutement, "Contrat", "Contractuels")

exporter(repartition_par_Manager_de_proximite_maitrise, "EXPORT/STATISTIQUES/Repartition_sexe/Par_metier/repartition_par_Manager_de_proximite_maitrise")
exporter(repartition_par_Conducteurs, "EXPORT/STATISTIQUES/Repartition_sexe/Par_metier/repartition_par_Conducteurs")
exporter(repartition_par_Cadre_permanent, "EXPORT/STATISTIQUES/Repartition_sexe/Par_contrat/repartition_par_Cadre_permanent")
exporter(repartition_par_Contractuels, "EXPORT/STATISTIQUES/Repartition_sexe/Par_contrat/repartition_par_Contractuels")
exporter(repartition_par_Contractuels, "EXPORT/STATISTIQUES/Comparaison/repartition_par_Contractuels")
exporter(repartition_par_Cadre_permanent, "EXPORT/STATISTIQUES/Comparaison/repartition_par_Cadre_permanent")

def evolution_par_metier_ou_sexe(data, variable):
    """
    Calcule et retourne l'évolution des effectifs par métier ou par sexe sur plusieurs années.

    Paramètres :
    data (list) : Liste de listes représentant un tableau de données.
    variable (str) : Nom de la variable à analyser (exemple : "Metier" ou "Sexe").

    Retourne :
    list : Tableau contenant :
           - Les en-têtes incluant les années et une colonne pour l'effectif moyen par métier.
           - Les effectifs par métier ou par sexe pour chaque année.
           - Une ligne supplémentaire contenant les effectifs totaux pour chaque année.
    """
    print(f"Repartition de l'effectif de l'année selon le metier")
    lesmodalites_annee = les_modalites(data, "Annee")
    lesmodalites_metier = les_modalites(data, variable)
    Resultat = []
    effectif_total = []
    lesmodalites_annee.insert(0, "Métier")
    Resultat.append(lesmodalites_annee)
    lesmodalites_annee.append("effectif_moyen")
    lesmodalites_metier.append("effectif_total")
    for modalite in range(len(lesmodalites_metier) - 1):
        l = [lesmodalites_metier[modalite]]
        for i in range(1, len(lesmodalites_annee) - 1):
            l1 = effectif_deux_critere(data, "Annee", lesmodalites_annee[i], variable, lesmodalites_metier[modalite])
            l.append(str(l1))
        Resultat.append(l)
    for modalite in Resultat[1:]:
        effectif_moyen = 0
        somme = 0
        nb_note = 0
        for metier_eff in modalite[1:]:
            nb_note += 1
            somme += int(metier_eff)
        effectif_moyen = somme / nb_note
        modalite.append(effectif_moyen)
    for modalites in Resultat[0][1:]:
        eff = total_variable(Resultat, modalites)
        effectif_total.append(eff)
    effectif_total.insert(0, "Effectif Total")
    Resultat.append(effectif_total)
    
    return Resultat



repartition_par_contrat_metier = evolution_par_metier_ou_sexe(Effectif,"Metier")
repartition_par_contrat_sexe = evolution_par_metier_ou_sexe(Effectif,"Sexe")

exporter(repartition_par_contrat_metier, "EXPORT/STATISTIQUES/Evolution _effectif/repartition_par_contrat_metier")
exporter(repartition_par_contrat_sexe, "EXPORT/STATISTIQUES/Evolution _effectif/repartition_par_contrat_sexe")

    
#---------------------------- Programme principal ----------------------------------------

def menu_general():
    """
    Affiche le menu principal de l'application.
    Retourne :
        int : Le choix de l'utilisateur.
    """
    print("\n--------- MENU GENERAL ---------------")
    print("1. Données : Description globale (qualité & quantité)")
    print("2. Visualisation : Affichage des données")
    print("3. Extraction Données : Sélection de données et Exports")
    print("4. Indicateurs & statistiques : Affichage / Exports Stat")
    print("5. Vérification Résultats Répartition Sexe : Affichage / Export (comparaison)")
    print("0. FIN")
    print("---------------------------------------")
    choix = int(input("Veuillez entrer votre choix : "))
    return choix


def gestion_choix(choix):
    """
    Gère le choix de l'utilisateur en fonction du menu principal.
    Paramètre :
        choix (int) : Le choix de l'utilisateur.
    """
    if choix == 1:
        print("\n=== Description des Données ===")
        print(f"Effectif : {len(Effectif)} lignes, {len(Effectif[0])} colonnes.")
        print(f"Recrutement : {len(Recrutement)} lignes, {len(Recrutement[0])} colonnes.")
        print(f"Répartition Genre : {len(repartition_genre_effectif)} lignes, {len(repartition_genre_effectif[0])} colonnes.")

    elif choix == 2:
        print("\n=== Visualisation des Données ===")
        dataset = input("Quel base données voulez-vous afficher ? (Effectif/Recrutement) : ").strip().lower()
        if dataset == "effectif":
            Afficher_Donnees(Effectif)
        elif dataset == "recrutement":
            Afficher_Donnees(Recrutement)
        else:
            print("Choix invalide.")

    elif choix == 3:
        print("\n=== Extraction de Données ===")
        dataset = input("Sur base de données voulez-vous travailler ? (Effectif/Recrutement) : ").strip().lower()
        if dataset == "effectif":
            data = Effectif
        elif dataset == "recrutement":
            data = Recrutement
        else:
            print("Choix invalide.")
            return

        
        resultat = extraire_plus_criteres(data)
        fichier_export = input("Entrez le nom du fichier pour exporter les résultats : ")
        exporter(resultat, f"EXPORT/Extraction/{fichier_export}")

    elif choix == 4:
        print("\n=== Indicateurs & Statistiques ===")
        dataset = input("Sur quel base de données voulez-vous travailler ? (Effectif/Recrutement) : ").strip().lower()
        if dataset == "effectif":
            data = Effectif
        elif dataset == "recrutement":
            data = Recrutement
        else:
            print("Choix invalide.")
            return

        variable = input("Entrez une variable quantitative pour calculer la (moyenne,max,min) : ")
        print(f"Moyenne : {moyenne_variable(data, variable)}")
        print(f"Maximum : {max_variable(data, variable)}")
        print(f"Minimum : {min_variable(data, variable)}")

    elif choix == 5:
        print("\n=== Vérification Répartition Sexe ===")
        annee = input("Entrez l'année pour la répartition (ex : 2020) : ")
        repartition = repartition_annee(Effectif, Recrutement, "Annee", annee)
        fichier_export = input("Entrez le nom du fichier pour exporter les résultats : ")
        exporter(repartition, f"EXPORT/STATISTIQUES/Repartition_sexe/Par_annee/{fichier_export}")
        print(f"Répartition exportée pour l'année {annee}.")

    elif choix == 0:
        print("\n=== Fin du Programme ===")
        exit()

    else:
        print("Choix invalide. Veuillez réessayer.")


# Programme principal
while True:
    choix = menu_general()
    gestion_choix(choix)

    