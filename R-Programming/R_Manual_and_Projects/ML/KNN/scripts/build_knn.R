# Asenna kknn-paketti, jos sitä ei ole
if (!require("kknn")) install.packages("kknn")
library(kknn)

# Rakenna KNN-malli
knn_model <- kknn(Sales ~ Advertising_Budget, 
                  train = train_data, 
                  test = test_data, 
                  k = 5) # Käytetään 5 lähintä naapuria

# Ennusteet testidatalle
test_data$Predicted_Sales <- knn_model$fitted.values
