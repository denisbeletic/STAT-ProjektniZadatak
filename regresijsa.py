import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv("global_electricity_production_data.csv")

df['date'] = pd.to_datetime(df['date'], format="%m/%d/%Y")

def dohvati_solar_proizvodnje(country, sample_years):  #koristimo funkciju kako ne bi morali kopirati kod
  result = pd.DataFrame()
  for year in sample_years:
    temp_df = df[(df['product'] == 'Solar')&(df['date'].dt.year == year)&(df['country_name'] == country)]
    temp_df = temp_df.groupby('country_name')['value'].sum().reset_index()
    temp_df['year'] = year
    result = pd.concat([result, temp_df], ignore_index=True) #appendanje dohvacenog retka
  result = result.sort_values(by = 'value', ascending=False)
  return result

sample_godine = [2018, 2019, 2020, 2021, 2022, 2023]

hrvatska_solar = dohvati_solar_proizvodnje("Croatia", sample_godine)

print(hrvatska_solar)

x_os = hrvatska_solar['year'].values.reshape(-1, 1) # Scikit-learn ocekuje 2D array, odnosno array od 1 stupca sa svim
y_os = hrvatska_solar['value'].values               # retcima za x, -1 dopusta NumPy-u da odredi broj redaka

model = LinearRegression()
model.fit(x_os, y_os)

pravac = model.coef_[0] * hrvatska_solar['year'] + model.intercept_   # y = nagib(a) * x + odsječak(b)

plt.figure(figsize=(8, 5))
sns.set_style("whitegrid")
plt.scatter(hrvatska_solar['year'], y_os, color='orange', s=45, label='Stvarni podaci')
plt.plot(hrvatska_solar['year'], pravac, color='red', linewidth=2, label='Regresija')
plt.title("Regresijski pravac solarne proizvodnje - Hrvatska")
plt.xlabel('Godina')
plt.ylabel('GWh')
plt.legend()
plt.tight_layout()
plt.show()