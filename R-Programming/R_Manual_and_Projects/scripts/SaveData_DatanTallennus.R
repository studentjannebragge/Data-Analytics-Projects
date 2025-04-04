# 1. Tallennetaan puhdistettu data
write.csv(cleaned_data, "data/cleaned_sales_data.csv", row.names = FALSE)

# 2. Tallennetaan kategorioiden yhteenveto
write.csv(category_summary, "data/category_summary.csv", row.names = FALSE)

# 3. Tallennetaan tuloluokkien jakautuminen kategorioittain
write.csv(income_summary, "data/income_summary.csv", row.names = FALSE)

# Vahvistusviesti
cat("Data on tallennettu seuraaviin tiedostoihin:\n",
    "- data/cleaned_sales_data.csv\n",
    "- data/category_summary.csv\n",
    "- data/income_summary.csv\n")
