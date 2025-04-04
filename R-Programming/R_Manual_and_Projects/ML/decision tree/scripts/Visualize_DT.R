# Asenna rpart.plot-paketti, jos sitä ei ole
if (!require("rpart.plot")) install.packages("rpart.plot")
library(rpart.plot)

# Piirrä päätöspuu
rpart.plot(tree_model, type = 3, fallen.leaves = TRUE, main = "Päätöspuu")
