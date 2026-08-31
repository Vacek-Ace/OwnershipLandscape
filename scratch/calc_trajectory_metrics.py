import pandas as pd
import numpy as np

df_ol = pd.read_csv('data/dynamic_ownership_landscape.csv')
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

substantive_models = [
    'member-owned', 'domestic private', 'foreign private', 
    'investment fund', 'hybrid', 'corporate-MCO', 
    'state-linked'
]
prop_cols = [f'prop_{m}' for m in substantive_models]

X = df_ol[prop_cols]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
coords = pca.fit_transform(X_scaled)
df_ol['PC1'] = coords[:, 0]
df_ol['PC2'] = coords[:, 1]

print("=== COORDENADAS Y TRAYECTORIAS EXACTAS ===")
stats_list = []
for league in sorted(df_ol['league'].unique()):
    sub = df_ol[df_ol['league'] == league].sort_values('season')
    x = sub['PC1'].values
    y = sub['PC2'].values
    
    x0, y0 = x[0], y[0]
    xf, yf = x[-1], y[-1]
    dx = xf - x0
    dy = yf - y0
    
    # Net distance
    net_dist = np.sqrt(dx**2 + dy**2)
    
    # Total path distance (sum of annual steps)
    step_dists = [np.sqrt((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2) for i in range(len(x)-1)]
    total_path = sum(step_dists)
    
    stats_list.append({
        'Liga': league,
        'Inicio 2019 (x, y)': f"({x0:.3f}, {y0:.3f})",
        'Cierre 2024 (x, y)': f"({xf:.3f}, {yf:.3f})",
        'Vector Neto (Δx, Δy)': f"({dx:+.3f}, {dy:+.3f})",
        'Distancia Neta': round(net_dist, 3),
        'Distancia Total Recorrida': round(total_path, 3),
        'Cuadrante Inicio -> Fin': f"{'Q-III' if x0>0 and y0<0 else 'Q-I' if x0>0 and y0>0 else 'Q-II' if x0<0 and y0>0 else 'Q-IV'} -> {'Q-III' if xf>0 and yf<0 else 'Q-I' if xf>0 and yf>0 else 'Q-II' if xf<0 and yf>0 else 'Q-IV'}"
    })

df_stats = pd.DataFrame(stats_list)
print(df_stats.to_string(index=False))
