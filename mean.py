import pandas as pd

df = pd.read_csv("global_electricity_production_data.csv")

df['date'] = pd.to_datetime(df['date'], format="%m/%d/%Y")
df_solar_2023 = df[(df['product'] == 'Solar')&(df['date'].dt.year == 2023)]

#grupiramo po drzavama pa sumiramo njihove GwH proizedene - ima vise mjerenja u godini, svaki mjesec 1, zato zbrajamo sve proizvodnje odredenih drzava u jednu vrijednost po drzavi
ukupno_drzave = df_solar_2023.groupby('country_name')['value'].sum().sort_values(ascending=False)

#.groupby daje series, pretvaramo natrag u dataframe
ukupno_drzave = ukupno_drzave.to_frame()

top10_solar = ukupno_drzave.head(10)

#racunamo srednju vrijednost
mean = 0
for x in top10_solar['value']:
    mean += x
mean /= 10

print("10 država koje su proizvele najviše električne energije preko solarnih izvora u 2023. (u GWh): \n\n", top10_solar)
print("\n", "Prosječna proizvodnja struje gore navedenih država:", round(mean, 3), " GWh") #zaokruzujemo na 3 decimale