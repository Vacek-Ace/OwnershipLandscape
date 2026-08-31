import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('data/dynamic_ownership_landscape.csv')
cols = [c for c in df.columns if c.startswith('prop_')]
print("Proportion columns:", cols)

X = df[cols]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
coords = pca.fit_transform(X_scaled)
df['PC1'] = coords[:, 0]
df['PC2'] = coords[:, 1]

print("\n=== PCA EXPLAINED VARIANCE ===")
print(f"PC1: {pca.explained_variance_ratio_[0]*100:.2f}%")
print(f"PC2: {pca.explained_variance_ratio_[1]*100:.2f}%")
print(f"Total Cumulative: {np.sum(pca.explained_variance_ratio_)*100:.2f}%")

print("\n=== PCA LOADINGS ===")
loadings = pd.DataFrame(pca.components_.T, index=cols, columns=['PC1', 'PC2'])
print(loadings.to_string())

print("\n=== LEAGUE TRAJECTORIES IN 2D SPACE ===")
for league, grp in df.groupby('league'):
    print(f"\n--- {league} ---")
    print(grp[['season', 'PC1', 'PC2', 'entropy', 'hhi', 'mco_rate']].to_string(index=False))

