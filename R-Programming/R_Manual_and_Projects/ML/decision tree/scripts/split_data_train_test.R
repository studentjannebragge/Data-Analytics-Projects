# Asenna caret-paketti, jos sitä ei ole
if (!require("caret")) install.packages("caret")
library(caret)

# Jaa data treeni- (70%) ja testijoukkoon (30%)
set.seed(123)
index <- createDataPartition(data$Sales, p = 0.7, list = FALSE)
train_data <- data[index, ]
test_data <- data[-index, ]
