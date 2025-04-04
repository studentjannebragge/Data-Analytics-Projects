# Luo esimerkkidata
set.seed(123)
data <- data.frame(
  Advertising_Budget = runif(100, 10, 100), # Mainosbudjetti välillä 10-100
  Sales = runif(100, 5, 50)                # Myynti välillä 5-50
)

# Luo luokkamuuttuja (High tai Low myynnin perusteella)
data$Category <- ifelse(data$Sales > median(data$Sales), "High", "Low")
data$Category <- as.factor(data$Category)

# Tarkastele dataa
head(data)
