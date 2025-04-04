# Asenna rpart-paketti, jos sitä ei ole
if (!require("rpart")) install.packages("rpart")
library(rpart)

# Luo päätöspuumalli
tree_model <- rpart(Sales ~ Advertising_Budget, data = train_data, method = "anova")

# Tulosta puun yhteenveto
summary(tree_model)
