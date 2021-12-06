import pandas as pd
cities_df = pd.read_csv("Resources/cities.csv")

cities_df.to_html('Resources/cities.html', index=False)