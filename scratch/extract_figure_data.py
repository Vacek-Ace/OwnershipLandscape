import pandas as pd
import numpy as np

# Load the dynamic datasets
df_ol = pd.read_csv('data/dynamic_ownership_landscape.csv')
df_clubs = pd.read_csv('data/dynamic_club_season_ownership.csv')

models = [
    'member-owned', 'domestic private', 'foreign private', 
    'investment fund', 'hybrid', 'corporate-MCO', 
    'state-linked', 'unknown'
]

print("==================================================================")
print("1. DATOS EXACTOS DE FIGURA 1: PERFILES DE PROPIEDAD 2024 (SNAPSHOT)")
print("==================================================================")
df_2024 = df_ol[df_ol['season'] == 2024].copy()
prop_cols = [f'prop_{m}' for m in models]
summary_2024 = []

for _, r in df_2024.iterrows():
    league = r['league']
    n_clubs = int(r['n_clubs'])
    row_dict = {'Liga': league, 'Total Clubes': n_clubs}
    for m in models:
        pct = r[f'prop_{m}'] * 100
        cnt = int(r[f'count_{m}'])
        row_dict[m] = f"{pct:.1f}% ({cnt})"
    summary_2024.append(row_dict)

df_sum_2024 = pd.DataFrame(summary_2024)
print(df_sum_2024.to_string(index=False))

print("\n==================================================================")
print("2. DATOS EXACTOS DE FIGURA 2: EVOLUCIÓN TEMPORAL (2019-2024)")
print("==================================================================")
print("\n--- Panel A: Entropía de Shannon (Diversidad) ---")
piv_entropy = df_ol.pivot(index='season', columns='league', values='entropy')
print(piv_entropy.round(3).to_string())

print("\n--- Panel B: Índice HHI (Concentración) ---")
piv_hhi = df_ol.pivot(index='season', columns='league', values='hhi')
print(piv_hhi.round(3).to_string())

print("\n--- Panel C: Tasa MCO (% Multipropiedad) ---")
piv_mco = df_ol.pivot(index='season', columns='league', values='mco_rate') * 100
print(piv_mco.round(1).to_string())

print("\n--- Panel D: Tasa de Vínculo Estatal (% State Link) ---")
piv_state = df_ol.pivot(index='season', columns='league', values='state_link_rate') * 100
print(piv_state.round(1).to_string())

print("\n==================================================================")
print("3. DATOS EXACTOS DE FIGURA 3: PCA Y TRAYECTORIAS (2019-2024)")
print("==================================================================")
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X = df_ol[prop_cols]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
coords = pca.fit_transform(X_scaled)
df_ol['PC1'] = coords[:, 0]
df_ol['PC2'] = coords[:, 1]

print("Cargas (Loadings):")
loadings = pd.DataFrame(pca.components_.T, index=models, columns=['PC1', 'PC2'])
print(loadings.round(3).to_string())

print("\nCoordenadas por Liga y Temporada (PC1, PC2):")
piv_pc1 = df_ol.pivot(index='season', columns='league', values='PC1')
piv_pc2 = df_ol.pivot(index='season', columns='league', values='PC2')

for league in sorted(df_ol['league'].unique()):
    print(f"\n>> {league}:")
    sub = df_ol[df_ol['league'] == league][['season', 'PC1', 'PC2', 'entropy', 'hhi', 'mco_rate']]
    print(sub.round(3).to_string(index=False))
