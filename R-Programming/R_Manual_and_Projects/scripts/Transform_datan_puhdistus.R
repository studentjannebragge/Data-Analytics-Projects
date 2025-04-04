# Lataa tarvittavat paketit
library(dplyr)
library(lubridate)
library(tidyr)          

# 1. Poistetaan puuttuvat arvot
cleaned_data <- sales_data %>%
  drop_na()

# 2. Muutetaan päivämäärät oikeaan muotoon
cleaned_data <- cleaned_data %>%
  mutate(Date = as.Date(Date, format = "%Y-%m-%d"))

# 3. Lasketaan kokonaishinta
cleaned_data <- cleaned_data %>%
  mutate(TotalPrice = Quantity * Price)

# 4. Luodaan tuloluokkien sarake
cleaned_data <- cleaned_data %>%
  mutate(IncomeCategory = case_when(
    TotalPrice < 100 ~ "Low",
    TotalPrice >= 100 & TotalPrice < 500 ~ "Medium",
    TRUE ~ "High"
  ))

# Tarkista puhdistettu ja rikastettu data
head(cleaned_data)
