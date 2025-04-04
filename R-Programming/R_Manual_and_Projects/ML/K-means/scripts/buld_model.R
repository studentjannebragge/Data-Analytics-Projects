# Suorita K-Means klusterointi
set.seed(123)
kmeans_model <- kmeans(data_scaled, centers = 3, nstart = 25)

# Lisää klusterit alkuperäiseen dataan
data$Cluster <- as.factor(kmeans_model$cluster)

# Tarkastele klusteroitua dataa
head(data)
