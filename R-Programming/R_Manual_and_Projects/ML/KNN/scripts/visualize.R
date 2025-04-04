if (!require("ggplot2")) install.packages("ggplot2")
library(ggplot2)

# Scatterplot: Todelliset vs. Ennustetut arvot
ggplot(test_data, aes(x = Sales, y = Predicted_Sales)) +
  geom_point(color = "blue") +
  geom_abline(slope = 1, intercept = 0, color = "red", linetype = "dashed") +
  labs(title = "KNN: Todelliset vs. Ennustetut Myyntiarvot",
       x = "Todelliset Myyntiarvot",
       y = "Ennustetut Myyntiarvot")
