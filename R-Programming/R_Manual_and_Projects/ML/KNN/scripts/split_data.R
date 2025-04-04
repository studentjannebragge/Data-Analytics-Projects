# Jaa data
set.seed(123)
index <- createDataPartition(scaled_data$Sales, p = 0.7, list = FALSE)
train_data <- scaled_data[index, ]
test_data <- scaled_data[-index, ]
