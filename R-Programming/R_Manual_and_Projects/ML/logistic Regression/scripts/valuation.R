# R-squared ja RMSE
r_squared <- summary(model)$r.squared
rmse <- sqrt(mean((data$Sales - data$Predicted_Sales)^2))

# Tulosta metriikat
cat("R²:", round(r_squared, 3), "\n")
cat("RMSE:", round(rmse, 3), "\n")
