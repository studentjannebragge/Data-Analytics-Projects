if (!require("caret")) install.packages("caret")
library(caret)

# Jaa data
set.seed(123)
index <- createDataPartition(data$Category, p = 0.7, list = FALSE)
train_data <- data[index, ]
test_data <- data[-index, ]
