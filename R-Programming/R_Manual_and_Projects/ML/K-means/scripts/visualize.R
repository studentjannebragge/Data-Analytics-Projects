if (!require("ggplot2")) install.packages("ggplot2")
library(ggplot2)

# Scatterplot
ggplot(data, aes(x = Advertising_Budget, y = Sales)) +
  geom_point() +
  labs(title = "Asiakastiedot: Mainosbudjetti ja Myynti",
       x = "Mainosbudjetti (€)",
       y = "Myynti (€)")
