# Luo esimerkkidata
set.seed(123) # Aseta satunnaissiementä toistettavuuden varmistamiseksi
data <- data.frame(
  Advertising_Budget = runif(50, 10, 100), # Satunnaisia mainosbudjetteja välillä 10-100
  Sales = runif(50, 5, 50) # Satunnaisia myyntilukuja välillä 5-50
)

# Tarkastele dataa
head(data)
