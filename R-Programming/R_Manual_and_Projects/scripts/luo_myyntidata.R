# Luo myyntidata
set.seed(123)  # Jotta tulokset ovat toistettavia

sales_data <- data.frame(
  Date = sample(seq(as.Date("2023-01-01"), as.Date("2023-12-31"), by = "day"), 100, replace = TRUE),
  Product = sample(c("Product A", "Product B", "Product C"), 100, replace = TRUE),
  Category = sample(c("Electronics", "Groceries", "Clothing"), 100, replace = TRUE),
  Quantity = sample(1:20, 100, replace = TRUE),
  Price = round(runif(100, 5, 100), 2)
)

# Tarkista data
head(sales_data)

# Luo "data"-kansio, jos sitä ei ole olemassa
if (!dir.exists("data")) {
  dir.create("data")
}

# Tallenna data "data"-kansioon CSV-tiedostona
write.csv(sales_data, file = "data/sales_data.csv", row.names = FALSE)

# Ilmoitus tallennuksesta
cat("Data tallennettu kansioon: data/sales_data.csv\n")
