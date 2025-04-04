# Confusion Matrix
conf_matrix <- confusionMatrix(test_data$Predicted_Category, test_data$Category)

# Tulosta tulokset
print(conf_matrix)
