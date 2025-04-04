# Lataa dplyr-paketti (jos ei jo ladattu)
library(dplyr)

# 1. Yhteenveto kategorioittain
category_summary <- cleaned_data %>%
  group_by(Category) %>%
  summarise(
    TotalSales = sum(TotalPrice),
    AveragePrice = mean(Price),
    TotalQuantity = sum(Quantity)
  )

# Näytä kategorioiden yhteenveto
print(category_summary)

# 2. Tuloluokkien jakautuminen kategorioittain
income_summary <- cleaned_data %>%
  group_by(Category, IncomeCategory) %>%
  summarise(
    Count = n(),
    TotalSales = sum(TotalPrice)
  )

# Näytä tuloluokkien jakautuminen
print(income_summary)
