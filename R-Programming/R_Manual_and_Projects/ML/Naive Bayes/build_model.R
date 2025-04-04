# Asenna e1071-paketti, jos sitä ei ole
if (!require("e1071")) install.packages("e1071")
library(e1071)

# Rakenna Naive Bayes -malli
nb_model <- naiveBayes(Category ~ Advertising_Budget + Sales, data = train_data)

# Tarkastele mallia
print(nb_model)
