import pandas as pd

df = pd.read_csv("global_electricity_production_data.csv")

df['date'] = pd.to_datetime(df['date'], format="%m/%d/%Y")
df_solar_2023 = df[(df['product'] == 'Solar')&(df['date'].dt.year == 2023)]

#grupiramo po drzavama pa sumiramo njihove GwH proizedene - ima vise u godini, svaki mjesec 1, zato zbrajamo sve proizvodnje odredenih drzava u jednu vrijednost po drzavi
ukupno_drzave = df_solar_2023.groupby('country_name')['value'].sum().sort_values(ascending=False)

#.groupby daje series, pretvaramo natrag u dataframe
ukupno_drzave = ukupno_drzave.to_frame()

top10_solar = ukupno_drzave.head(10)

#racunamo medijan, pocinje se od indexa 0 do 9
lijevi = top10_solar.iloc[4]
desni = top10_solar.iloc[5]

medijan = (lijevi['value'] + desni['value']) / 2
print("Medijan: ", medijan, " GWh")