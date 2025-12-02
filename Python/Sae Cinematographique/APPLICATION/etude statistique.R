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

# La concentration des établissements cinématographiques dans une zone donnée influence-t-elle la fréquentation moyenne de chaque cinéma ?

data <- read.csv("C:/Users/Adam/Downloads/Sae Mousaoui-Adam-Bououden-Yasmine/APPLICATION/data/data.csv", sep=";", comment.char="#")
# Remplacer les valeurs vides ou "NA" sous forme de texte par NA réel
data[data == ""] <- NA
data[data == "NA"] <- NA

# Vérifier la présence de valeurs manquantes
sum(is.na(data)) # Nombre total de valeurs NA
colSums(is.na(data))  # Nombre de valeurs NA par colonne

mean(data$fauteuils, na.rm = TRUE)


# Structure du jeu de données
str(data)
# Affichage des premières lignes
head(data)

# ---------------- ANALYSE UNIVARIÉE ----------------

# Diagramme en barres des régions
ggplot(data, aes(x = fct_infreq(region_administrative))) +
  geom_bar(fill="darkgreen") +
  coord_flip() +
  labs(title = "Répartition des nombre de cinémas selon la région", x = "Région", y = "Nombre de cinémas")


ggplot(data, aes(x = zone_de_la_commune)) +
  geom_bar(fill = "forestgreen") +
  labs(title = "Répartition des cinémas selon la zone de commune",
       x = "Zone", y = "Nombre de cinémas")

# ---------------- ANALYSE BIVARIÉE ----------------

# Corrélation entre le nombre de fauteuils et le nombre d’entrées
ggplot(data, aes(x = fauteuils, y = entrees_2022)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method="lm", se=FALSE, color="red") +
  labs(title = "Répartition des fauteuils selon les Entrées en 2022", x = "Nombre de fauteuils", y = "Entrées en 2022")

data$ecrans <- as.numeric(as.character(data$ecrans))

ggplot(data, aes(x = ecrans, y = entrees_2022)) +
  geom_jitter(alpha = 0.5, color = "green4", width = 0.3) +
  geom_smooth(method = "lm", color = "black") +
  labs(title = "Nombre d’écrans vs fréquentation",
       x = "Nombre d’écrans", y = "Entrées 2022")


# ---------------- Tableau de indicateus important  ----------------


# Nombre de cinémas par zone géographique (par exemple par code_commune)
cinemas_par_zone <- data %>%
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

# ---------------- CORRELATION  ----------------

# Corrélation entre densité (par population) et fréquentation moyenne
cor.test(cinemas_par_zone$densite_cinemas_population,
         cinemas_par_zone$freq_moyenne_par_cinema,
         method = "pearson")

# L’analyse de corrélation ne met pas en évidence de lien significatif entre la densité de cinémas (rapportée à la population) et la fréquentation moyenne par établissement au niveau départemental (r = -0.17, p = 0.11). On observe une tendance négative modérée, qui pourrait suggérer un effet de concurrence, mais celle-ci n’est pas statistiquement significative.




cinemas_par_zone$densite_cat <- cut(
  cinemas_par_zone$densite_cinemas_population,
  breaks = quantile(cinemas_par_zone$densite_cinemas_population, probs = c(0, 1/3, 2/3, 1), na.rm = TRUE),
  labels = c("faible", "moyenne", "forte"),
  include.lowest = TRUE
)


ggplot(cinemas_par_zone, aes(x = densite_cat, y = freq_moyenne_par_cinema)) +
  geom_boxplot(fill = "skyblue") +
  labs(
    title = "Fréquentation moyenne par cinéma selon la densité de cinémas",
    x = "Densité de cinémas (catégorie)",
    y = "Fréquentation moyenne"
  )


lm1 <- lm(freq_moyenne_par_cinema ~ densite_cinemas_population, data = cinemas_par_zone)
summary(lm1)



# ---------------- Carte France repartiton freq par cinema selon dep ----------------

install.packages("sf")
install.packages("viridis")
library(sf)
library(viridis)

# Charger la carte des départements
france_dep <- st_read("https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson")

# Harmoniser le code département dans cinemas_par_zone
cinemas_par_zone <- cinemas_par_zone %>%
  mutate(code = sprintf("%02d", as.numeric(departement)))

# Fusion des données avec la carte
france_dep_data <- france_dep %>%
  left_join(cinemas_par_zone, by = c("code" = "code"))

# Calcul des centroids pour placer les labels
centroids <- st_centroid(france_dep_data)

# Création de la carte avec la fréquentation moyenne en remplissage et le nombre de cinémas en label
ggplot(france_dep_data) +
  geom_sf(aes(fill = freq_moyenne_par_cinema), color = "white", size = 0.2) +
  geom_sf_text(data = centroids, aes(label = nb_cinemas), size = 3, color = "black") +
  scale_fill_viridis_c(option = "plasma", na.value = "grey90") +
  labs(
    title = "Fréquentation moyenne et nombre de cinémas par département",
    fill = "Fréquentation\nmoyenne"
  ) +
  theme_minimal()