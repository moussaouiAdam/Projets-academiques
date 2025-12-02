# Chargement des bibliothèques
install.packages("tidyverse")
install.packages("ggplot2")
install.packages("dplyr")
install.packages("tidyverse")
library(tidyverse)
library(ggplot2)
library(dplyr)
library(tidyverse)

# ---------------- PROBLEMATIQUE ----------------

# Le matériel et la programmation des films suffisent-ils encore à attirer le public dans les cinéma aujourd’hui ?



data2022 <- read.csv("C:/Users/Adam/Downloads/Statistique/dataok/data.csv", sep=";", comment.char="#")
# Remplacer les valeurs vides ou "NA" sous forme de texte par NA réel
data2022[data2022 == ""] <- NA
data2022[data2022 == "NA"] <- NA
# Vérifier la présence de valeurs manquantes
sum(is.na(data2022)) # Nombre total de valeurs NA
colSums(is.na(data2022))  # Nombre de valeurs NA par colonne
mean(data2022$fauteuils, na.rm = TRUE)
# Structure du jeu de données
str(data2022)
# Affichage des premières lignes
head(data2022)


data2021 <- read.csv("C:/Users/Adam/Downloads/Statistique/dataok/data2021.csv", sep=";", comment.char="#")
# Remplacer les valeurs vides ou "NA" sous forme de texte par NA réel
data2021[data2021 == ""] <- NA
data2021[data2021 == "NA"] <- NA
# Vérifier la présence de valeurs manquantes
sum(is.na(data2021)) # Nombre total de valeurs NA
colSums(is.na(data2021))  # Nombre de valeurs NA par colonne
mean(data2021$fauteuils, na.rm = TRUE)
# Structure du jeu de données
str(data2021)
# Affichage des premières lignes
head(data2021)


data2020 <- read.csv("C:/Users/Adam/Downloads/Statistique/dataok/data2020.csv", sep=";", comment.char="#")
# Remplacer les valeurs vides ou "NA" sous forme de texte par NA réel
data2020[data2020 == ""] <- NA
data2020[data2020 == "NA"] <- NA
# Vérifier la présence de valeurs manquantes
sum(is.na(data2020)) # Nombre total de valeurs NA
colSums(is.na(data2020))  # Nombre de valeurs NA par colonne
mean(data2020$fauteuils, na.rm = TRUE)
# Structure du jeu de données
str(data2020)
# Affichage des premières lignes
head(data2020)


data2019 <- read.csv("C:/Users/Adam/Downloads/Statistique/dataok/data2019.csv", sep=";", comment.char="#")
# Remplacer les valeurs vides ou "NA" sous forme de texte par NA réel
data2019[data2019 == ""] <- NA
data2019[data2019 == "NA"] <- NA
# Vérifier la présence de valeurs manquantes
sum(is.na(data2019)) # Nombre total de valeurs NA
colSums(is.na(data2019))  # Nombre de valeurs NA par colonne
mean(data2019$fauteuils, na.rm = TRUE)
# Structure du jeu de données
str(data2019)
# Affichage des premières lignes
head(data2019)


data2018 <- read.csv("C:/Users/Adam/Downloads/Statistique/dataok/data2018.csv", sep=";", comment.char="#")
# Remplacer les valeurs vides ou "NA" sous forme de texte par NA réel
data2018[data2018 == ""] <- NA
data2018[data2018 == "NA"] <- NA
# Vérifier la présence de valeurs manquantes
sum(is.na(data2018)) # Nombre total de valeurs NA
colSums(is.na(data2018))  # Nombre de valeurs NA par colonne
mean(data2018$fauteuils, na.rm = TRUE)
# Structure du jeu de données
str(data2018)
# Affichage des premières lignes
head(data2018)

# ===============================
# PRÉTRAITEMENT DES DONNÉES
# ===============================

# Conversion en numérique pour éviter les erreurs (suppression des espaces)
data2018$entrees_2017 <- as.numeric(gsub(" ", "", data2018$entrees_2017))
data2018$entrees_2018 <- as.numeric(gsub(" ", "", data2018$entrees_2018))
data2019$entrees_2019 <- as.numeric(gsub(" ", "", data2019$entrees_2019))
data2020$entrees_2020 <- as.numeric(gsub(" ", "", data2020$entrees_2020))
data2021$entrees_2021 <- as.numeric(gsub(" ", "", data2021$entrees_2021))
data2022$entrees_2022 <- as.numeric(gsub(" ", "", data2022$entrees_2022))
data2022$entrees_2022 <- as.numeric(gsub(" ", "", data2022$entrees_2022))  # ligne en double, peut être supprimée

# Remplacement de la virgule par un point pour les PdM des films américains
data2019$PdM_en_entrees_des_films_americains <- gsub(",", ".", data2019$PdM_en_entrees_des_films_americains)
data2020$PdM_en_entrees_des_films_americains <- gsub(",", ".", data2020$PdM_en_entrees_des_films_americains)
data2021$PdM_en_entrees_des_films_americains <- gsub(",", ".", data2021$PdM_en_entrees_des_films_americains)
data2022$PdM_en_entrees_des_films_americains <- gsub(",", ".", data2022$PdM_en_entrees_des_films_americains)
data2018$PdM_en_entrees_des_films_americains <- gsub(",", ".", data2018$PdM_en_entrees_des_films_americains)

# Conversion en numérique des PdM américains
data2019$PdM_en_entrees_des_films_americains <- as.numeric(data2019$PdM_en_entrees_des_films_americains)
data2020$PdM_en_entrees_des_films_americains <- as.numeric(data2020$PdM_en_entrees_des_films_americains)
data2021$PdM_en_entrees_des_films_americains <- as.numeric(data2021$PdM_en_entrees_des_films_americains)
data2022$PdM_en_entrees_des_films_americains <- as.numeric(data2022$PdM_en_entrees_des_films_americains)
data2018$PdM_en_entrees_des_films_americains <- as.numeric(data2018$PdM_en_entrees_des_films_americains)

# Conversion en numérique des PdM des films français
data2022$PdM_en_entrees_des_films_francais <- as.numeric(gsub(",", ".", data2022$PdM_en_entrees_des_films_francais))
data2021$PdM_en_entrees_des_films_francais <- as.numeric(gsub(",", ".", data2021$PdM_en_entrees_des_films_francais))
data2020$PdM_en_entrees_des_films_francais <- as.numeric(gsub(",", ".", data2020$PdM_en_entrees_des_films_francais))
data2019$PdM_en_entrees_des_films_francais <- as.numeric(gsub(",", ".", data2019$PdM_en_entrees_des_films_francais))
data2018$PdM_en_entrees_des_films_francais <- as.numeric(gsub(",", ".", data2018$PdM_en_entrees_des_films_francais))

# Conversion en numérique pour les séances
data2022$seances <- as.numeric(gsub(" ", "", data2022$seances))
data2021$seances <- as.numeric(gsub(" ", "", data2021$seances))
data2020$seances <- as.numeric(gsub(" ", "", data2020$seances))
data2019$seances <- as.numeric(gsub(" ", "", data2019$seances))
data2018$seances <- as.numeric(gsub(" ", "", data2018$seances))

# ---------------- Tableau de indicateus important  ----------------


# Nombre de cinémas par zone géographique (par exemple par code_commune)
cinemas_par_zone <- data2022 %>%
  group_by(departement) %>%
  summarise(
    nb_cinemas = n(),
    total_entrees = sum(entrees_2021, na.rm = TRUE),
    population = first(population_de_la_commune),
  ) %>%
  mutate(
    densite_cinemas_population = nb_cinemas / population * 10000,
    freq_moyenne_par_cinema = total_entrees / nb_cinemas
  )

# ===============================
# CALCUL DES TOTAUX D’ENTRÉES PAR ANNÉE
# ===============================

totaux_entrees <- data.frame(
  annee = 2017:2022,
  entrees = c(
    sum(data2018$entrees_2017, na.rm = TRUE),
    sum(data2018$entrees_2018, na.rm = TRUE),
    sum(data2019$entrees_2019, na.rm = TRUE),
    sum(data2020$entrees_2020, na.rm = TRUE),
    sum(data2021$entrees_2021, na.rm = TRUE),
    sum(data2022$entrees_2022, na.rm = TRUE)
  )
)

# ===============================
# GRAPHIQUE : ENTRÉES EN SALLE
# ===============================

install.packages("scales")
library(scales)

ggplot(totaux_entrees, aes(x = annee, y = entrees)) +
  geom_line(color = "blue", size = 1.2) +
  geom_point(size = 3.5, color = "red") +
  geom_text(
    aes(label = paste0(round(entrees / 1e6, 1), " M")),
    vjust = -0.8, size = 4.5, fontface = "bold", color = "black"
  ) +
  scale_y_continuous(labels = label_number(scale = 1e-6, suffix = " M")) +
  labs(
    title = "Répartition du nombre d’entrées en salles de cinéma en France par année",
    x = "Année", y = "Nombre total d'entrées"
  ) +
  theme_minimal(base_size = 13)

# ===============================
# NOMBRE DE FILMS PAR SEMAINE
# ===============================

resume_films_semaine <- data.frame(
  annee = 2018:2022,
  films_par_semaine = c(
    sum(data2018$nombre_de_films_en_semaine_1, na.rm = TRUE),
    sum(data2019$nombre_de_films_en_semaine_1, na.rm = TRUE),
    sum(data2020$nombre_de_films_en_semaine_1, na.rm = TRUE),
    sum(data2021$nombre_de_films_en_semaine_1, na.rm = TRUE),
    sum(data2022$nombre_de_films_en_semaine_1, na.rm = TRUE)
  )
)

ggplot(resume_films_semaine, aes(x = annee, y = films_par_semaine)) +
  geom_line(color = "blue", size = 1.2) +
  geom_point(size = 3.5, color = "red") +
  geom_text(
    aes(label = format(films_par_semaine, big.mark = " ", scientific = FALSE)),
    vjust = -0.8, size = 4.5, fontface = "bold", color = "black"
  ) +
  scale_y_continuous(labels = label_number(big.mark = " ")) +
  labs(
    title = "Évolution du nombre de films en France par année",
    x = "Année", y = "Nombre total de films"
  ) +
  theme_minimal(base_size = 13)

# ===============================
# NOMBRE DE FILMS INÉDITS
# ===============================

resume_films_inedit <- data.frame(
  annee = 2018:2022,
  films_inedit = c(
    sum(data2018$nombre_de_films_inedits, na.rm = TRUE),
    sum(data2019$nombre_de_films_inedits, na.rm = TRUE),
    sum(data2020$nombre_de_films_inedits, na.rm = TRUE),
    sum(data2021$nombre_de_films_inedits, na.rm = TRUE),
    sum(data2022$nombre_de_films_inedits, na.rm = TRUE)
  )
)

ggplot(resume_films_inedit, aes(x = annee, y = films_inedit)) +
  geom_line(color = "blue", size = 1.2) +
  geom_point(size = 3.5, color = "red") +
  geom_text(
    aes(label = format(films_inedit, big.mark = " ", scientific = FALSE)),
    vjust = -0.8, size = 4.5, fontface = "bold", color = "black"
  ) +
  scale_y_continuous(labels = label_number(big.mark = " ")) +
  labs(
    title = "Évolution du nombre total de films inédits en France par année",
    x = "Année", y = "Nombre total de films inédits"
  ) +
  theme_minimal(base_size = 13)

# ===============================
# PART DE MARCHÉ DES FILMS AMÉRICAINS
# ===============================

resume_film_americain <- data.frame(
  annee = 2018:2022,
  films_americain = c(
    round(mean(data2018$PdM_en_entrees_des_films_americains, na.rm = TRUE),2),
    round(mean(data2019$PdM_en_entrees_des_films_americains, na.rm = TRUE),2),
    round(mean(data2020$PdM_en_entrees_des_films_americains, na.rm = TRUE),2),
    round(mean(data2021$PdM_en_entrees_des_films_americains, na.rm = TRUE),2),
    round(mean(data2022$PdM_en_entrees_des_films_americains, na.rm = TRUE),2)
  )
)

ggplot(resume_film_americain, aes(x = as.factor(annee), y = films_americain)) +
  geom_col(fill = "steelblue") +
  geom_text(
    aes(label = paste0(round(films_americain, 1), " %")),
    vjust = -0.5, size = 4.5, fontface = "bold", color = "black"
  ) +
  scale_y_continuous(labels = label_number(suffix = " %", big.mark = " ")) +
  labs(
    title = "Évolution de la part de marché moyenne des films américains en France par année",
    x = "Année", y = "Part de marché moyenne (films américains)"
  ) +
  theme_minimal(base_size = 13)

# ===============================
# PART DE MARCHÉ DES FILMS FRANÇAIS
# ===============================

resume_film_fr <- data.frame(
  annee = 2018:2022,
  films_fr = c(
    round(mean(data2018$PdM_en_entrees_des_films_francais, na.rm = TRUE),2),
    round(mean(data2019$PdM_en_entrees_des_films_francais, na.rm = TRUE),2),
    round(mean(data2020$PdM_en_entrees_des_films_francais, na.rm = TRUE),2),
    round(mean(data2021$PdM_en_entrees_des_films_francais, na.rm = TRUE),2),
    round(mean(data2022$PdM_en_entrees_des_films_francais, na.rm = TRUE),2)
  )
)

ggplot(resume_film_fr, aes(x = as.factor(annee), y = films_fr)) +
  geom_col(fill = "#0072B2") +
  geom_text(
    aes(label = paste0(round(films_fr, 1), " %")),
    vjust = -0.5, size = 4.5, fontface = "bold", color = "black"
  ) +
  scale_y_continuous(labels = label_number(suffix = " %", big.mark = " ")) +
  labs(
    title = "Évolution de la part de marché moyenne des films français en France par année",
    x = "Année", y = "Part de marché moyenne (films français)"
  ) +
  theme_minimal(base_size = 13)

# ===============================
# ÉVOLUTION DES SÉANCES
# ===============================

resume_seance <- data.frame(
  annee = 2018:2022,
  seance = c(
    sum(data2018$seances, na.rm = TRUE),
    sum(data2019$seances, na.rm = TRUE),
    sum(data2020$seances, na.rm = TRUE),
    sum(data2021$seances, na.rm = TRUE),
    sum(data2022$seances, na.rm = TRUE)
  )
)

ggplot(resume_seance, aes(x = annee, y = seance)) +
  geom_line(color = "#0072B2", size = 1.2) +
  geom_point(size = 3.5, color = "#D55E00") +
  geom_text(
    aes(label = format(seance, big.mark = " ", scientific = FALSE)),
    vjust = -0.8, size = 4.5, fontface = "bold", color = "black"
  ) +
  scale_y_continuous(labels = label_number(big.mark = " ")) +
  labs(
    title = "Évolution du nombre de séances par année en France",
    x = "Année", y = "Nombre de séances"
  ) +
  theme_minimal(base_size = 13)

# ===============================
# ÉVOLUTION DES FAUTEUILS
# ===============================

resume_fauteuil <- data.frame(
  annee = 2018:2022,
  fauteuil = c(
    sum(data2018$fauteuils, na.rm = TRUE),
    sum(data2019$fauteuils, na.rm = TRUE),
    sum(data2020$fauteuils, na.rm = TRUE),
    sum(data2021$fauteuils, na.rm = TRUE),
    sum(data2022$fauteuils, na.rm = TRUE)
  )
)

ggplot(resume_fauteuil, aes(x = annee, y = fauteuil)) +
  geom_line(color = "#0072B2", size = 1.2) +
  geom_point(size = 3.5, color = "#D55E00") +
  geom_text(
    aes(label = format(fauteuil, big.mark = " ", scientific = FALSE)),
    vjust = -0.8, size = 4.5, fontface = "bold", color = "black"
  ) +
  scale_y_continuous(labels = label_number(big.mark = " ")) +
  labs(
    title = "Évolution du nombre de fauteuils par année en France",
    x = "Année", y = "Nombre de fauteuils"
  ) +
  theme_minimal(base_size = 13)

# ===============================
# CARTE DE FRANCE - CINÉMAS PAR DÉPARTEMENT
# ===============================

install.packages("sf")
install.packages("viridis")
library(sf)
library(viridis)

# Charger carte des départements simplifiée
france_dep <- st_read("https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson")

# Harmoniser les codes départementaux
cinemas_par_zone <- cinemas_par_zone %>%
  mutate(code = sprintf("%02d", as.numeric(departement)))

# Fusion données carte + cinéma
france_dep_data <- france_dep %>%
  left_join(cinemas_par_zone, by = c("code" = "code"))

# Centroides pour positionner les labels
centroids <- st_centroid(france_dep_data)

# Création de la carte
ggplot(france_dep_data) +
  geom_sf(aes(fill = freq_moyenne_par_cinema), color = "white", size = 0.2) +
  geom_sf_text(data = centroids, aes(label = nb_cinemas), size = 3, color = "black") +
  scale_fill_viridis_c(option = "plasma", na.value = "grey90") +
  labs(
    title = "Fréquentation moyenne et nombre de cinémas par département en 2022",
    fill = "Fréquentation\nmoyenne"
  ) +
  theme_minimal()

