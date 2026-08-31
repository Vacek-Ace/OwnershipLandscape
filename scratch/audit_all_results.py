import pandas as pd
import numpy as np

# Load the dynamic club-season dataset
df_clubs = pd.read_csv('data/dynamic_club_season_ownership.csv')
total_obs = len(df_clubs)

print("==================================================================")
print("1. CUANTIFICACIÓN EXHAUSTIVA DE 'UNKNOWN' POR LIGA Y TEMPORADA")
print("==================================================================")

# Count unknowns per club-season
unknown_mask = df_clubs['ownership_model'] == 'unknown'
total_unknown = unknown_mask.sum()
pct_total_unknown = (total_unknown / total_obs) * 100

print(f"Total observaciones club-temporada: {total_obs}")
print(f"Total observaciones 'unknown': {total_unknown} ({pct_total_unknown:.2f}% de la muestra total)")
print(f"Total observaciones resueltas (K=7): {total_obs - total_unknown} ({100 - pct_total_unknown:.2f}% de la muestra total)")

# Table of unknown counts and percentages by league and season
piv_unknown_count = df_clubs.pivot_table(
    index='season', 
    columns='league', 
    values='ownership_model', 
    aggfunc=lambda x: (x == 'unknown').sum(),
    fill_value=0
)

piv_total_count = df_clubs.pivot_table(
    index='season', 
    columns='league', 
    values='ownership_model', 
    aggfunc='count',
    fill_value=0
)

piv_unknown_pct = (piv_unknown_count / piv_total_count) * 100

print("\n--- Conteo de Clubes 'Unknown' por Liga y Temporada ---")
print(piv_unknown_count.to_string())

print("\n--- Porcentaje de 'Unknown' sobre el Total de la Liga (%) ---")
print(piv_unknown_pct.round(2).to_string())

# List of the exact 8 club-season cases
print("\n--- Detalle de los 8 Casos 'Unknown' en el Panel ---")
unknown_detail = df_clubs[unknown_mask][['season', 'league', 'club_id', 'club_name', 'ultimate_owner', 'owner_type']]
print(unknown_detail.to_string(index=False))

print("\n==================================================================")
print("2. AUDITORÍA COMPLETA DE TODOS LOS RESULTADOS DEL LANDSCAPE (K=7)")
print("==================================================================")
df_ol = pd.read_csv('data/dynamic_ownership_landscape.csv')
substantive_models = [
    'member-owned', 'domestic private', 'foreign private', 
    'investment fund', 'hybrid', 'corporate-MCO', 
    'state-linked'
]

print("\n--- Tabla de Proporciones 2024 (K=7) ---")
df_2024 = df_ol[df_ol['season'] == 2024]
for _, r in df_2024.iterrows():
    print(f"\n>> {r['league']} (N_sub={int(r['n_sub_clubs'])}, N_total={int(r['n_clubs'])}):")
    for m in substantive_models:
        print(f"   - {m}: {r[f'prop_{m}']*100:.1f}% ({int(r[f'count_{m}'])} clubes)")

print("\n--- Métricas Longitudinales (2019 vs 2024) ---")
for league in sorted(df_ol['league'].unique()):
    r19 = df_ol[(df_ol['league'] == league) & (df_ol['season'] == 2019)].iloc[0]
    r24 = df_ol[(df_ol['league'] == league) & (df_ol['season'] == 2024)].iloc[0]
    print(f"\n>> {league}:")
    print(f"   - Entropía (H): {r19['entropy']:.3f} (2019) -> {r24['entropy']:.3f} (2024)")
    print(f"   - HHI: {r19['hhi']:.3f} (2019) -> {r24['hhi']:.3f} (2024)")
    print(f"   - MCO Rate: {r19['mco_rate']*100:.1f}% (2019) -> {r24['mco_rate']*100:.1f}% (2024)")
    print(f"   - State Link Rate: {r19['state_link_rate']*100:.1f}% (2019) -> {r24['state_link_rate']*100:.1f}% (2024)")

