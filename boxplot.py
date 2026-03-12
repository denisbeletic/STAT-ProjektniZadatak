import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("global_electricity_production_data.csv")

df['date'] = pd.to_datetime(df['date'], format="%m/%d/%Y")

def dohvati_solar_proizvodnje(sample_countries, year):  #koristimo funkciju kako ne bi morali kopirati kod
  result = pd.DataFrame()
  for country in sample_countries:
    temp_df = df[(df['product'] == 'Solar')&(df['date'].dt.year == year)&(df['country_name'] == country)]
    temp_df = temp_df.groupby('country_name')['value'].sum().sort_values(ascending=False)
    result = pd.concat([result, temp_df], ignore_index=False) #appendanje dohvacenog retka
    result['year'] = year #dodajemo proslijedenu godinu u df, trebati ce nam poslije za labels u boxplot-u
  result = result.sort_values(by = 'value', ascending=False)  #opcionalno, sortira silazno
  return result

sample_drzave = ["Italy", "Korea", "Spain", "Australia", "Brazil", "Germany", "Japan", "India", "United States", "China"]

drzave2023 = dohvati_solar_proizvodnje(sample_drzave, 2023)
drzave2022 = dohvati_solar_proizvodnje(sample_drzave, 2022)
drzave2021 = dohvati_solar_proizvodnje(sample_drzave, 2021)
drzave2020 = dohvati_solar_proizvodnje(sample_drzave, 2020)
drzave2019 = dohvati_solar_proizvodnje(sample_drzave, 2019)
drzave2018 = dohvati_solar_proizvodnje(sample_drzave, 2018)

sve_drzave = [drzave2018, drzave2019, drzave2020, drzave2021, drzave2022, drzave2023]

#uzima vrijednosti stupaca za plot-anje svakog skupa podataka kao box u grafu
podaci = [df['value'] for df in sve_drzave]
#uzima godinu svakog skupa za prikaz kao label
labels = [df['year'].iloc[0] for df in sve_drzave]

plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
plt.boxplot(podaci, tick_labels=labels, whis = [0, 100], showfliers = False)
plt.ylabel('Količina proizvedene e.e. (u GWh)')
plt.title('Boxplot - proizvodnje e.e. iz solarnih izvora kroz godine za određene države')

#radi povecavanja broja label-a na y-osi
y_os = plt.gca()
y_os.yaxis.set_major_locator(plt.MaxNLocator(nbins=24)) 

plt.show()