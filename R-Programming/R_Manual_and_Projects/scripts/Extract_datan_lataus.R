# Lataa data CSV-tiedostosta
sales_data <- read.csv("data/sales_data.csv", stringsAsFactors = FALSE)

# Tarkista datan ensimmäiset rivit
head(sales_data)

# Tarkista datan rakenne
str(sales_data)

# Tarkista, onko tiedostossa puuttuvia arvoja
sum(is.na(sales_data))
