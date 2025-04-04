# Skaalaa muuttujat välillä 0-1
if (!require("caret")) install.packages("caret")
library(caret)

# Skaalaus
scaled_data <- data
scaled_data[, 1:2] <- scale(data[, 1:2])

# Tarkasta skaalattu data
head(scaled_data)
