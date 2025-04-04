# Scatterplot klustereille
ggplot(data, aes(x = Advertising_Budget, y = Sales, color = Cluster)) +
  geom_point(size = 3) +
  labs(title = "K-Means Klusterointi: Asiakassegmentit",
       x = "Mainosbudjetti (€)",
       y = "Myynti (€)") +
  scale_color_manual(values = c("red", "blue", "green"))
