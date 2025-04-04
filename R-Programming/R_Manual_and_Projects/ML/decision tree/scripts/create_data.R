# Luo esimerkkidata
set.seed(123)
data <- data.frame(
  Advertising_Budget = runif(50, 10, 100), # Satunnaisia mainosbudjetteja
  Sales = runif(50, 5, 50) # Satunnaisia myyntilukuja
)

# Tarkastele dataa
head(data)
