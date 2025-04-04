# Tee ennusteet testidatalle
test_data$Predicted_Sales <- predict(tree_model, newdata = test_data)

# Tarkastele testidatan ennusteita
head(test_data)
