import pandas as pd

df = pd.read_csv("global_electricity_production_data.csv")

# Parsiramo datume da budu tipa 'datetime'
df['date'] = pd.to_datetime(df['date'], format="%m/%d/%Y")

df2023 = df[df['date'].dt.year == 2023]

ugljen_treset_proizvedeni_plinovi = ((df2023['product'] == 'Coal, Peat and Manufactured Gasses')&(df2023['parameter'] == 'Net Electricity Production')).sum()
nafta_i_derivati = ((df2023['product'] == 'Oil and Petroleum Products')&(df2023['parameter'] == 'Net Electricity Production')).sum()
prirodni_plin = ((df2023['product'] == 'Natural Gas')&(df2023['parameter'] == 'Net Electricity Production')).sum()
goriva_obnovljivih_izvora = ((df2023['product'] == 'Combustible Renewables')&(df2023['parameter'] == 'Net Electricity Production')).sum()
hidro = ((df2023['product'] == 'Hydro')&(df2023['parameter'] == 'Net Electricity Production')).sum()
vjetar = ((df2023['product'] == 'Wind')&(df2023['parameter'] == 'Net Electricity Production')).sum()
solar = ((df2023['product'] == 'Solar')&(df2023['parameter'] == 'Net Electricity Production')).sum()
geotermalni = ((df2023['product'] == 'Geothermal')&(df2023['parameter'] == 'Net Electricity Production')).sum()
nuklearni = ((df2023['product'] == 'Nuclear')&(df2023['parameter'] == 'Net Electricity Production')).sum()
ostali = (((df2023['product'] == 'Other Combustible Non-Renewables')|(df2023['product'] == 'Other Renewables'))&(df2023['parameter'] == 'Net Electricity Production')).sum()

print(
    "\n"
    "Ugljen, treset i proizvedeni plinovi", " = ", ugljen_treset_proizvedeni_plinovi, "\n"
    "Nafta i derivati", " = ", nafta_i_derivati, "\n"
    "Prirodni plin", " = ", prirodni_plin, "\n"
    "Goriva obnovljivih izvora", " = ", goriva_obnovljivih_izvora, "\n"
    "Hidro", " = ", hidro, "\n"
    "Vjetar", " = ", vjetar, "\n"
    "Solar", " = ", solar, "\n"
    "Geotermalni", " = ", geotermalni, "\n"
    "Nuklearni", " = ", nuklearni, "\n"
    "Ostali", " = ", ostali, "\n"
)