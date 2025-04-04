# Scatterplot ennustetuille luokille
if (!require("ggplot2")) install.packages("ggplot2")
library(ggplot2)

ggplot(test_data, aes(x = Advertising_Budget, y = Sales, color = Predicted_Category)) +
  geom_point(size = 3) +
  labs(title = "Naive Bayes: Luokittelu Asiakasryhmiin",
       x = "Mainosbudjetti (€)",
       y = "Myynti (€)") +
  scale_color_manual(values = c("red", "blue"))
