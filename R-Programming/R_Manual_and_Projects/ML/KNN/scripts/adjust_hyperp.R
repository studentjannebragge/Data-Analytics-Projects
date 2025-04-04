# Kokeile eri k-arvoja ja valitse paras
k_values <- 1:20
rmse_values <- sapply(k_values, function(k) {
  model <- kknn(Sales ~ Advertising_Budget, train = train_data, test = test_data, k = k)
  sqrt(mean((test_data$Sales - model$fitted.values)^2))
})

# Parhaan k-arvon valinta
best_k <- k_values[which.min(rmse_values)]
cat("Paras k:", best_k, "\n")

# Visualisoi k:n vaikutus RMSE:hen
plot(k_values, rmse_values, type = "b", main = "k-arvon vaikutus RMSE:hen",
     xlab = "k (Lähimpien naapureiden lukumäärä)", ylab = "RMSE")
