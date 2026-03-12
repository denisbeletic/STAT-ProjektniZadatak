import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("global_electricity_production_data.csv")

df['date'] = pd.to_datetime(df['date'], format="%m/%d/%Y")
df_solar_2023 = df[(df['product'] == 'Solar')&(df['date'].dt.year == 2023)]

#grupiramo po drzavama pa sumiramo njihove GwH proizedene - ima vise u godini, svaki mjesec 1, zato zbrajamo sve proizvodnje odredenih drzava u jednu vrijednost po drzavi
ukupno_drzave = df_solar_2023.groupby('country_name')['value'].sum().sort_values(ascending=False)

#.groupby daje series, pretvaramo natrag u dataframe
ukupno_drzave = ukupno_drzave.to_frame()

top10_solar = ukupno_drzave.head(10)

#spremamo vrijednosti proizvodnje
vrijednosti = top10_solar['value']
pretinci_val = [0, 75000, 150000, 225000, 300000, 375000, 450000, 525000]

pretinci_str = [] #radi label-a
for x in pretinci_val:
  pretinci_str.append(str(x))

plt.figure(figsize=(8,5))
plt.hist(vrijednosti, bins=pretinci_val, color='#00ffcc', edgecolor='black')
plt.xticks(pretinci_val, pretinci_str) #ovo postavlja label-s na granicama pretinaca
plt.title('Histogram proizvodnje e.e. iz solarnih izvora u 2023.')
plt.xlabel('Količina prozivedene e.e. (GWh)')
plt.ylabel('Broj država')
plt.grid(axis='y', alpha=0.35)
plt.show()