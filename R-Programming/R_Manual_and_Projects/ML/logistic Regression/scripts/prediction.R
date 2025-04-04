# Lisää mallin ennusteet dataan
data$Predicted_Sales <- predict(model)

# Visualisoi malli
ggplot(data, aes(x = Advertising_Budget, y = Sales)) +
  geom_point() +
  geom_line(aes(y = Predicted_Sales), color = "blue") +
  labs(title = "Lineaarinen Regressio: Mainosbudjetti ja Myynti",
       x = "Mainosbudjetti (€)",
       y = "Myynti (€)")
