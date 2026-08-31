import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.spatial import procrustes
from scipy.stats import spearmanr

# 1. Load active club seasons and landscape
df_clubs = pd.read_csv('data/dynamic_club_season_ownership.csv')
excel_path = 'data/raw/DEFINITIVA. football_club_ownership_audit_2019_2025.xlsx'
xl = pd.ExcelFile(excel_path)
df_own = xl.parse('Ownership_Dataset')

# Substantive models (K = 7)
substantive_models = [
    'member-owned', 'domestic private', 'foreign private', 
    'investment fund', 'hybrid', 'corporate-MCO', 
    'state-linked'
]

print(f"Substantive models ({len(substantive_models)}): {substantive_models}")

# 2. Build the 7-model dynamic landscape
landscape_7_rows = []

for (league, season), grp in df_clubs.groupby(['league', 'season']):
    # Filter or count substantive models
    # Exclude unknown from denominator
    sub_grp = grp[grp['ownership_model'].isin(substantive_models)]
    n_sub_clubs = len(sub_grp)
    n_total_clubs = len(grp)
    
    counts = grp['ownership_model'].value_counts()
    
    # Proportions re-normalized over the 7 substantive models
    props = {f'prop_{m}': counts.get(m, 0) / n_sub_clubs for m in substantive_models}
    
    # Entropy over K=7
    p_vals = np.array([props[f'prop_{m}'] for m in substantive_models if props[f'prop_{m}'] > 0])
    entropy = - np.sum(p_vals * np.log(p_vals))
    
    # HHI over K=7
    hhi = np.sum([props[f'prop_{m}']**2 for m in substantive_models])
    
    # MCO rate
    mco_rate = (grp['mco'] == 1).sum() / n_total_clubs
    
    # State link rate
    state_link_rate = (grp['state_link'] > 0).sum() / n_total_clubs
    
    row_data = {
        'league': league,
        'season': season,
        'n_clubs': n_total_clubs,
        'n_sub_clubs': n_sub_clubs,
        'entropy': entropy,
        'hhi': hhi,
        'mco_rate': mco_rate,
        'state_link_rate': state_link_rate
    }
    for m in substantive_models:
        row_data[f'prop_{m}'] = props[f'prop_{m}']
        row_data[f'count_{m}'] = counts.get(m, 0)
        
    landscape_7_rows.append(row_data)

df_ol_7 = pd.DataFrame(landscape_7_rows)
df_ol_7.to_csv('data/dynamic_ownership_landscape.csv', index=False, encoding='utf-8')
print("Successfully updated data/dynamic_ownership_landscape.csv with K=7 substantive models!")

# 3. PCA on 7 substantive models
prop_cols_7 = [f'prop_{m}' for m in substantive_models]
X7 = df_ol_7[prop_cols_7]
scaler = StandardScaler()
X7_scaled = scaler.fit_transform(X7)

pca7 = PCA(n_components=2)
coords7 = pca7.fit_transform(X7_scaled)
df_ol_7['PC1'] = coords7[:, 0]
df_ol_7['PC2'] = coords7[:, 1]

var_pc1 = pca7.explained_variance_ratio_[0] * 100
var_pc2 = pca7.explained_variance_ratio_[1] * 100
var_total = var_pc1 + var_pc2

print("\n=== PCA ON 7 SUBSTANTIVE MODELS ===")
print(f"PC1 Variance: {var_pc1:.2f}%")
print(f"PC2 Variance: {var_pc2:.2f}%")
print(f"Cumulative Variance: {var_total:.2f}%")

loadings7 = pd.DataFrame(pca7.components_.T, index=substantive_models, columns=['PC1', 'PC2'])
print("\nLoadings:")
print(loadings7.round(3).to_string())

print("\nTrajectories:")
for league, grp in df_ol_7.groupby('league'):
    print(f"\n>> {league}:")
    print(grp[['season', 'PC1', 'PC2', 'entropy', 'hhi', 'mco_rate']].round(3).to_string(index=False))

