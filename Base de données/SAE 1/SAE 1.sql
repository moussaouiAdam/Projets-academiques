-- 1.	Lister tous les clients avec leur nom, localité et département.

SELECT CliNom, CliLocalite, CliDep
FROM client;


-- 2.	Afficher les informations de tous les médicaments disponibles avec leurs prix.

SELECT MedNom, MedPrix
FROM medicament;


-- 3.	Obtenir les noms et prix des traitements proposés par la clinique.

SELECT NomTrai, PrixTrai
FROM traitement;


-- 4.	Lister toutes les visites effectuées pour chaque animal, en montrant la date de visite et le type de suivi.

SELECT AniNom, VisSuivi, VisDate
FROM visite INNER JOIN Animal ON visite.VisAni = Animal.AniId;

-- 5.	Lister les informations de chaque animal, y compris la race, le sexe et la date de naissance.

SELECT AniNom, AniRace, AniSexe, AniDN
FROM Animal;


-- 6.	Récupérer les noms des clients et des animaux qu’ils possèdent.

SELECT client.CliNom, animal.AniNom
FROM client INNER JOIN animal ON client.CliNum =animal.Anicli;


-- 7.	Afficher les noms de tous les traitements administrés aux animaux de type « Chat ».

SELECT traitement.NomTrai, animal.AniType
FROM ((traitement INNER JOIN detailvisite ON traitement.CodeTrai = detailvisite.VisTrait) INNER JOIN visite ON detailvisite.VisNum = visite.VisNum) INNER JOIN animal ON visite.VisAni = animal.AniId
WHERE animal.AniType = "Chat";


-- 8.	Afficher les informations des animaux mâles 

SELECT *
FROM Animal
WHERE AniSexe = "M";


-- 9.	Récupérer la liste de tous les clients ayant un site web.

SELECT CliSiteWeb
FROM client
WHERE CliSiteWeb is not null;


-- 10.	Obtenir la liste des animaux stérilisés

SELECT AniNom, AniSteril
FROM animal
WHERE AniSteril = True;


-- 11.	Quels sont les médicaments et les dates de prescription aux chiens ainsi que les différents numéro et nom de chien? (Donner deux solution si c’est possible une avec imbrication de bloc et l’autre sans)

SELECT medicament.MedNom, visite.VisDate, animal.AniId, animal.AniNom
FROM ((medicament INNER JOIN detailvisite ON medicament.medcode = detailvisite.vismed) INNER JOIN visite ON detailvisite.visnum = visite.visnum) INNER JOIN animal ON visite.visani = animal.AniId
WHERE AniType = "Chien";


-- 12.	Quels sont les animaux n’ayant jamais eu de traitement?

SELECT animal.AniId, detailVisite.vismed
FROM (animal INNER JOIN visite ON animal.AniId = visite.visani) INNER JOIN detailvisite ON visite.visnum = detailvisite.visnum
WHERE detailVisite.vismed = "0000";

-- 13.	Quels sont les animaux n’ayant pas eu de visite

SELECT animal.AniNom, visite.VisDate
FROM visite RIGHT JOIN animal ON visite.visani = animal.AniId
WHERE visite.VisDate is null;

-- 14.	Donner pour chaque animal, son nom, sa race, et les différentes dates de visite à la clinique deux cas suivants 
-- a.	faire figurer dans le résultat de la requête que les animaux qui ont eu au moins une visite

SELECT Animal.AniNom, Animal.AniRace, COUNT(Visite.VisDate) AS ["Nb visite"]
FROM Animal LEFT JOIN Visite ON Animal.AniId = Visite.VisAni
GROUP BY Animal.AniNom, Animal.AniRace
HAVING COUNT (Visite.VisDate) >= 1;

-- b.	faire figurer dans le résultat de la requête tous les animaux

SELECT animal.AniNom, animal.AniRace, visite.VisDate
FROM animal LEFT JOIN visite ON visite.VisAni = animal.AniId;

-- 15.	Lister les traitements coûtant plus d’un prix (de votre choix).

SELECT NomTrai
FROM traitement
WHERE PrixTrai > 100;


-- 16.	Récupérer tous les clients ayant une remise supérieure à une remise donnée (de votre choix).

SELECT CliNom
FROM client
WHERE CliRemise>0.2;


-- 17.	Afficher les animaux décédés avec leur nom, type et date de naissance.

SELECT AniNom, AniType, AniDN, AniDecede
FROM animal
WHERE AniDecede = True;

-- 18.	Lister les clients enregistrés dans la clinique depuis plus de cinq ans.

SELECT CliNom, Clidepuis
FROM client
WHERE Clidepuis <= DATEADD("yyyy", -5, NOW());


-- 19.	Trouver tous les animaux de type « Chien » pesant plus d’une valeur donnée.

SELECT AniType, Poids
FROM Animal
WHERE AniType = "Chien" and Poids > 20;


-- 20.	Afficher les médicaments dont le prix est inférieur à la moyenne des prix.

SELECT MedNom, MedPrix
FROM medicament
WHERE MedPrix < (SELECT AVG(MedPrix) FROM medicament);

-- 21. R�cup�rer les visites pour lesquelles le paiement a �t� effectu� en liquide.

SELECT visite.VisNum, paiement.PaiTypeCode, paiement.PaiTypeLib
FROM paiement INNER JOIN visite ON paiement.PaiTypeCode = visite.VisTypepaie
WHERE paiement.PaiTypeCode = 2;

-- 22. Lister les animaux avec un commentaire associ� dans leur fiche.

SELECT AniNom, AniCommentaires
FROM Animal
WHERE AniCommentaires is not null;


-- 23.Trouver les animaux ayant des propri�taires dans un d�partement de votre choix.

SELECT animal.AniNom, client.CliDep
FROM animal INNER JOIN client ON animal.AniCli = client.CliNum
WHERE client.CliDep like "%34%";

-- 24.Compter le nombre total d'animaux trait�s par la clinique.

SELECT count(AniId)as Total animal
FROM Animal;

-- 25.Calculer le co�t total des m�dicaments disponibles.

SELECT sum(MedPrix)
FROM medicament;

-- 26.R�cup�rer le nombre de clients par d�partement.

SELECT CliDep AS ["Departement"], count(CliNum) AS ["Nombre de clients"]
FROM client
GROUP BY CliDep;

-- 27.Calculer la dur�e moyenne de vie des animaux dans la base.

SELECT AniDN
FROM animal;

-- 28. Trouver le nombre total de visites r�alis�es pour chaque animal.

SELECT animal.AniNom, count(VisDate)
FROM animal INNER JOIN visite ON animal.AniId = visite.visani
GROUP BY animal.AniNom;


-- 29. Afficher le nombre de m�dicaments administr�s par visite.

SELECT animal.AniNom, count(visite.VisDate) AS ["Nb de visite"]
FROM visite INNER JOIN animal ON visite.visani = animal.AniId
GROUP BY animal.AniNom;

-- 30. Calculer le nombre moyen de traitements par visite pour chaque animal.

SELECT animal.AniNom, visite.VisDate, count(NomTrai) AS ["Nb moyen de visite par traitement"]
FROM ((traitement INNER JOIN detailvisite ON traitement.codetrai = detailvisite.vistrait) INNER JOIN visite ON detailvisite.Visnum = visite.Visnum) INNER JOIN animal ON visite.VisAni = animal.AniId
GROUP BY animal.AniNom, visite.VisDate;

-- 31. Calculer le chiffre d'affaires total g�n�r� par les traitements.

SELECT sum(PrixTrai) AS ["chiffre d'affaires "]
FROM ((traitement INNER JOIN detailvisite ON traitement.codetrai = detailvisite.vistrait) INNER JOIN visite ON detailvisite.Visnum = visite.Visnum) INNER JOIN animal ON visite.VisAni = animal.AniId;

-- 32. Afficher la somme des remises accord�es � chaque client.

SELECT CliNom, sum(CliRemise)
FROM Client
group by CliNom


-- 33. R�cup�rer le co�t total des m�dicaments administr�s aux chats.

SELECT AniType, sum(MedPrix)
FROM ((medicament INNER JOIN detailvisite ON medicament.MedCode = detailvisite.VisMed) INNER JOIN visite ON detailvisite.VisNum = visite.VisNum) INNER JOIN animal ON visite.VisAni = animal.AniId
GROUP BY AniType
HAVING AniType = "Chat";

-- 34. Afficher les noms des animaux et les noms de leurs propri�taires.

SELECT AniNom, CliNom
FROM animal INNER JOIN client ON animal.AniCli =client.CliNum;

-- 35. R�cup�rer les noms des clients et les types d'animaux qu'ils poss�dent.

SELECT CliNom, AniType
FROM animal INNER JOIN client ON animal.AniCli =client.CliNum;

-- 36. Afficher les noms des animaux et les traitements qu�ils ont re�us.

SELECT animal.AniNom, traitement.NomTrai
FROM ((traitement INNER JOIN detailvisite ON traitement.codetrai = detailvisite.vistrait) INNER JOIN visite ON detailvisite.Visnum = visite.Visnum) INNER JOIN animal ON visite.VisAni = animal.AniId;

-- 37. Obtenir le nom de chaque client et le nombre de visites qu�il a effectu�es.

SELECT client.CliNom, count(VisDate)
FROM (client INNER JOIN animal ON client.CliNum = animal.AniCli) INNER JOIN visite ON animal.AniId = visite.VisAni
GROUP BY client.CliNom;

-- 38. Lister les m�dicaments prescrits lors des visites, en incluant les d�tails de chaque visite.

SELECT medicament.MedNom, visite.VisDate, detailvisite.VisType, visite.VisSuivi, visite.VisTypepaie, detailvisite.VisTrait
FROM (medicament INNER JOIN detailvisite ON medicament.MedCode = detailvisite.VisMed) INNER JOIN visite ON detailvisite.VisNum = visite.VisNum;

-- 39. Afficher les clients avec leur localit� et le nombre d'animaux qu'ils poss�dent.

SELECT client.CliNom, client.CliLocalite, count(AniNom) AS ["Nombre d'animaux"]
FROM animal INNER JOIN client ON animal.AniCli =client.CliNum
GROUP BY client.CliNom, client.CliLocalite;

-- 40. R�cup�rer les noms des clients et les visites effectu�es pour chacun de leurs animaux.

SELECT client.CliNom, visite.VisDate, animal.AniNom
FROM (client INNER JOIN animal ON client.CliNum =animal.AniCli) INNER JOIN visite ON animal.AniId = visite.VisAni;



-- 41. Afficher les d�tails de toutes les visites avec les traitements administr�s et m�dicaments utilis�s.

SELECT Visite.VisDate, DetailVisite.VisNum, DetailVisite.VisLig, DetailVisite.VisType, DetailVisite.VisMed, Traitement.NomTrai, Medicament.MedNom
FROM Visite INNER JOIN (Medicament INNER JOIN (Traitement INNER JOIN DetailVisite ON Traitement.CodeTrai = DetailVisite.VisTrait) ON Medicament.MedCode = DetailVisite.VisMed) ON Visite.VisNum = DetailVisite.VisNum;


-- 42. Obtenir la liste des clients avec le montant total de leurs factures de visites.

SELECT client.CliNom, sum(MedPrix) AS ["montant total de leurs factures"]
FROM (((client INNER JOIN animal ON client.clinum = animal.anicli) INNER JOIN visite ON animal.AniId = visite.Visani) INNER JOIN detailvisite ON visite.visnum = detailvisite.visnum) INNER JOIN medicament ON detailvisite.vismed = medicament.medcode
GROUP BY client.CliNom;

-- 43. R�cup�rer la liste des visites et des m�dicaments prescrits pour chaque visite.

SELECT visite.VisDate, medicament.MedNom
FROM (medicament INNER JOIN detailvisite ON medicament.MedCode = detailvisite.VisMed) INNER JOIN visite ON detailvisite.VisNum = visite.VisNum
GROUP BY visite.VisDate, medicament.MedNom;

-- 44. Trouver les noms des clients dont le nom commence par la lettre � M �.

SELECT CliNom
FROM client
WHERE CliNom like "M%";

-- 45. Afficher les m�dicaments administr�s � des animaux d�un type de votre choix.

SELECT medicament.medNom, animal.aninom, animal.anitype
FROM ((animal INNER JOIN visite ON animal.aniId = visite.visani) INNER JOIN detailvisite ON visite.visnum = detailvisite.visnum) INNER JOIN medicament ON detailvisite.vismed = medicament.medcode
WHERE animal.anitype = "Chien";

-- 46. Lister les visites de suivi effectu�es apr�s le premier semestre 2020.

SELECT visite.VisNum, visite.VisAni, visite.VisDate, DetailVisite.VisType, visite.VisDateSuivi
FROM Visite INNER JOIN DetailVisite ON Visite.VisNum = DetailVisite.VisNum
WHERE  visite.VisDate > #2020-06-30#;	 


--47. R�cup�rer les clients ayant au moins deux animaux.

SELECT CliNom, count(AniNom) AS ["Nonbre d'animaux"]
FROM client INNER JOIN animal ON client.clinum = animal.anicli
GROUP BY CliNom
HAVING count(AniNom) >= 2;

-- 48. Afficher les clients ayant une balance de compte n�gative.


-- 49. Trouver tous les animaux ayant re�u un traitement sp�cifique de votre choix.

SELECT animal.AniNom, traitement.NomTrai
FROM ((animal INNER JOIN visite ON animal.aniId = visite.visani) INNER JOIN detailvisite ON visite.visnum = detailvisite.visnum) INNER JOIN traitement ON detailvisite.vistrait = traitement.codetrai
WHERE traitement.NomTrai = "Amputation d'un membre";

-- 50. Lister les animaux n�s avant une ann�e de votre choix.

SELECT AniNom, AniDN
FROM animal
WHERE AniDN < #2015-01-01#;

-- 51. Trouver les clients dont les animaux ont �t� trait�s avec un m�dicament sp�cifique.

SELECT client.CliNom, medicament.MedNom
FROM (((client INNER JOIN animal ON client.CliNum = animal.anicli) INNER JOIN visite ON animal.aniId = visite.visani) INNER JOIN detailvisite ON visite.visnum = detailvisite.visnum) INNER JOIN medicament ON detailvisite.vismed = medicament.medcode
WHERE medicament.MedNom = "Aspirine - 100 mg";

-- 52. Afficher les clients ayant effectu� au moins une visite au cours du dernier mois.


-- 53. Obtenir la liste des clients qui n'ont effectu� aucune visite depuis leur enregistrement.

SELECT CliNom, count(visdate)
FROM (client LEFT JOIN animal ON client.clinum = animal.anicli) LEFT JOIN visite ON animal.AniId = visite.Visani
GROUP BY CliNom
HAVING count(visdate) = 0;

-- 54. Trouver les clients ayant effectu� le plus grand nombre de visites (top 5).

SELECT TOP 5 CliNom, count(visdate)
FROM (client INNER JOIN animal ON client.clinum = animal.anicli) INNER JOIN visite ON animal.AniId = visite.Visani
GROUP BY CliNom
ORDER BY count(visdate) DESC;

-- 55. Requ�te pour d�terminer les animaux ayant eu plus de trois traitements diff�rents en un an.

SELECT A.AniNom, COUNT(*) AS NbTraitements, YEAR(V.VisDate) AS Annee
FROM (Animal AS A
INNER JOIN Visite AS V ON A.AniId = V.VisAni)
INNER JOIN (SELECT DISTINCT DV.VisNum, DV.VisTrait
            FROM DetailVisite AS DV) AS UniqueDetails
ON V.VisNum = UniqueDetails.VisNum
GROUP BY A.AniNom, YEAR(V.VisDate)
HAVING COUNT(*) > 3;


-- 56. Calcul du chiffre d�affaires par trimestre de l'ann�e 2021, pour chaque type de traitement.

SELECT Traitement.NomTrai AS TypeTraitement, FORMAT(Visite.VisDate, "yyyy 'T'Q") AS Trimestre, SUM(Traitement.PrixTrai) AS ChiffreAffaires
FROM
    (Traitement
    INNER JOIN DetailVisite ON Traitement.CodeTrai = DetailVisite.VisTrait)
    INNER JOIN Visite ON DetailVisite.VisNum = Visite.VisNum
WHERE YEAR(Visite.VisDate) = 2021
GROUP BY Traitement.NomTrai, FORMAT(Visite.VisDate, "yyyy 'T'Q")
ORDER BY Traitement.NomTrai, Trimestre;


-- 57. Requ�te donnant la liste des animaux ayant pris le m�me m�dicament plus de trois fois dans l'ann�e.


-- 58. Requ�te pour calculer le co�t total des traitements administr�s sur une p�riode donn�e.

SELECT Traitement.NomTrai AS TypeTraitement, SUM(Traitement.PrixTrai) AS CoutTotalTraitement
FROM Visite INNER JOIN (Traitement INNER JOIN DetailVisite ON Traitement.CodeTrai = DetailVisite.VisTrait) ON Visite.VisNum = DetailVisite.VisNum
where Visite.VisDate BETWEEN #2021-01-01# AND #2021-12-31#
GROUP BY Traitement.NomTrai
ORDER BY CoutTotalTraitement DESC;



-------Partie 2 
--- 1.	Rapports d’activité générale

-- B

SELECT year(visdate) as Annee,  month(visdate) as mois , Count(Visite.VisNum) AS CompteDeVisDate
FROM Visite
where year(visdate) = year(date())-4 or year(visdate) = year(date())-3
group by year(visdate), month(visdate)

-- Analyse Croisée 

transform count(Visite.VisNum)
select month(VisDate) as mois
from Visite 
group by month(VisDate)
PIVOT year(VisDate);

--- C

Select top 1 DetailVisite.VisMed, count(detailVisite.VisNum) as CompteDeVisNum
FROM DetailVisite
Where VisMed <> "0000"
group by VisMed, visTrait 
order by count(detailVisite.VisNum) desc
 