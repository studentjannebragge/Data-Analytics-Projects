# Tee ennusteet testidatalle
test_data$Predicted_Category <- predict(nb_model, test_data)

# Tarkastele ennusteita
head(test_data)
