import pandas as pd

df = pd.read_csv("global_electricity_production_data.csv")

df['date'] = pd.to_datetime(df['date'], format="%m/%d/%Y")
df_solar_2023 = df[(df['product'] == 'Solar')&(df['date'].dt.year == 2023)]

#grupiramo po drzavama pa sumiramo njihove GwH proizedene - ima vise u godini, svaki mjesec 1, zato zbrajamo sve proizvodnje odredenih drzava u jednu vrijednost po drzavi
ukupno_drzave = df_solar_2023.groupby('country_name')['value'].sum().sort_values(ascending=False)

#.groupby daje series, pretvaramo natrag u dataframe
ukupno_drzave = ukupno_drzave.to_frame()

top10_solar = ukupno_drzave.head(10)

#racunamo kvartile, Q2 = medijan
Q2_lijevi = (top10_solar['value']).iloc[4]
Q2_desni = (top10_solar['value']).iloc[5]

Q2 = (Q2_lijevi + Q2_desni) / 2
Q1 = (top10_solar['value']).iloc[2]
Q3 = (top10_solar['value']).iloc[7]

#racunamo IQR
if Q3 > Q1:
  IQR = Q3 - Q1
else:
  IQR = Q1 - Q3

print("Q1: ", round(Q1, 3), " GWh")
print("Q2: ", round(Q2, 3), " GWh")
print("Q3: ", round(Q3, 3), " GWh\n")

print("IQR: ", round(IQR, 3), " GWh")