# Laske RMSE
rmse <- sqrt(mean((test_data$Sales - test_data$Predicted_Sales)^2))

# Tulosta RMSE
cat("RMSE päätöspuulle:", round(rmse, 3), "\n")
