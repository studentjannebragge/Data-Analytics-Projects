# Laske WCSS (Within-Cluster Sum of Squares) eri klusterimäärille
wcss <- sapply(1:10, function(k) {
  kmeans(data_scaled, centers = k, nstart = 25)$tot.withinss
})

# Visualisoi WCSS
plot(1:10, wcss, type = "b", pch = 19, frame = FALSE,
     xlab = "Klusterien määrä",
     ylab = "WCSS (Within-Cluster Sum of Squares)",
     main = "Elbow Method")
