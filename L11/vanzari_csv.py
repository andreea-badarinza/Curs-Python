import pandas as pd

# 1. Încarcă fișierul CSV
fisier = "vanzari.csv"  # Înlocuiește cu calea către fișierul tău CSV
df = pd.read_csv(fisier, parse_dates=['data_vanzarii'])

# Verificăm primele rânduri
print(df.head())

# 2. Cele mai vandute produse pe luna
df['luna'] = df['data_vanzarii'].dt.month
df['an'] = df['data_vanzarii'].dt.year
vanzari_lunar = df.groupby(['an', 'luna', 'produs'])['cantitate_vanduta'].sum().reset_index()
vanzari_lunar = vanzari_lunar.sort_values(['an', 'luna', 'cantitate_vanduta'], ascending=[True, True, False])
print("\nCele mai vandute produse pe luna:")
print(vanzari_lunar)

# 3. Venitul total pe fiecare produs
df['venit'] = df['cantitate_vanduta'] * df['pret']
venit_pe_produs = df.groupby('produs')['venit'].sum().reset_index()
print("\nVenitul total pe produs:")
print(venit_pe_produs)

# 4. Filtrare vânzări între două date
start_date = '2024-01-01'
end_date = '2024-03-31'
filtrat = df[(df['data_vanzarii'] >= start_date) & (df['data_vanzarii'] <= end_date)]
print(f"\nVanzari între {start_date} și {end_date}:")
print(filtrat)

# 5. Venitul mediu lunar
venit_mediu_lunar = df.groupby(['an', 'luna'])['venit'].mean().reset_index()
print("\nVenitul mediu lunar:")
print(venit_mediu_lunar)
