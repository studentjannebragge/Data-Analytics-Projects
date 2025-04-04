# Paranneltu päätöspuun visualisointi
rpart.plot(tree_model,
           type = 3,                  # Näyttää haarojen keskimääräiset arvot
           fallen.leaves = TRUE,      # Lehdet putoavat tasaiselle linjalle
           extra = 101,               # Näyttää enemmän tietoa (esim. ennusteet ja määrät)
           box.palette = "RdYlGn",    # Väritä solmut (vihreästä punaiseen)
           shadow.col = "gray",       # Lisää varjoja laatikoihin
           main = "Päätöspuun Visualisointi")
