import csv
import pandas as pd

profs_df = pd.read_csv("./csrankings.csv")

# all google scholar pages needing to be scraped
file = open("./google-scholar-links.csv", "w", encoding="utf-8")
file.write("name,google scholar link\n")
for index, row in profs_df.iterrows():
    if row['scholarid'] != 'NOSCHOLARPAGE':
        file.write(row['name'] + ",https://scholar.google.com/citations?user=" + row['scholarid'] + "&hl=en&oi=ao" + "\n")
file.close()