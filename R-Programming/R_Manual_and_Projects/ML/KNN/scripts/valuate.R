# RMSE (Root Mean Squared Error)
rmse <- sqrt(mean((test_data$Sales - test_data$Predicted_Sales)^2))

# Tulosta RMSE
cat("RMSE KNN-mallille:", round(rmse, 3), "\n")
