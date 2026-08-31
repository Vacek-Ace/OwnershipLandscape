import json
import os
import subprocess

def create_notebook():
    nb = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.13.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    def add_md(source):
        nb["cells"].append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [line + "\n" for line in source.strip().split("\n")]
        })

    def add_code(source):
        nb["cells"].append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [line + "\n" for line in source.strip().split("\n")]
        })

    # ==================== CELL 0: TITLE & INTRO ====================
    add_md("""# Análisis Dinámico y Configuracional del Ownership Landscape (OL) en las Cinco Grandes Ligas Europeas (2019-2024)

## 1. Introducción y Marco Metodológico

El concepto de **Ownership Landscape (OL)** (Paisaje de Propiedad) propone entender la estructura de propiedad de una liga no como la mera agregación estática de propietarios aislados, sino como una **configuración colectiva con propiedades emergentes propias** (Fiss, 2007). 

En el fútbol europeo contemporáneo, coexisten modelos tradicionales arraigados en el control social (clubes de socios), modelos privados locales, consorcios transnacionales, firmas de capital riesgo y fondos soberanos. Este estudio analiza la evolución de estos paisajes a través de dos niveles simultáneos de cambio:
1. **La rotación deportiva**: El impacto de ascensos y descensos en la estructura de la Primera División.
2. **Las transacciones corporativas longitudinales**: El cambio dinámico de dueño y modelo de control dentro de los propios clubes a lo largo del tiempo.

---

### Regla de Corte Temporal para la Asignación de Temporadas
Para modelar fielmente la disponibilidad de capital y la planificación del ciclo competitivo anual, se establece como **hito temporal de corte el cierre de la ventana de transferencias de verano (1 de septiembre)** de cada año:
* Toda adquisición, toma de control o fusión formalmente cerrada (**`Fecha de cierre`**) antes o el 1 de septiembre de un año $Y$ se imputa a la temporada que inicia ese verano ($Y$/$Y+1$).
* Toda operación cerrada con posterioridad al 1 de septiembre (otoño, invierno o mitad de campaña) mantiene el modelo previo durante esa temporada y surte efecto formal a partir de la siguiente temporada ($Y+1$/$Y+2$).

---

### Preguntas de Investigación Abordadas (RQs):
* **RQ1**: ¿Cómo se operacionaliza cuantitativamente el Ownership Landscape a nivel macro a través de proporciones composicionales, diversidad (Entropía de Shannon), concentración (HHI) y multipropiedad (MCO)?
* **RQ2**: ¿Cómo difieren los landscapes de propiedad entre las cinco grandes ligas europeas (Bundesliga, LaLiga, Ligue 1, Premier League y Serie A) y cómo han evolucionado longitudinalmente entre las temporadas 2019-2020 y 2024-2025?""")

    # ==================== CELL 1: SETUP & IMPORTS ====================
    add_code("""import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.spatial import procrustes
from scipy.stats import spearmanr

# Configuración visual para publicaciones académicas
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['figure.titlesize'] = 15
warnings.filterwarnings('ignore')

# Paleta de colores oficial por modelo de propiedad
MODEL_COLORS = {
    'member-owned': '#2ca02c',       # Verde bosque (Democrático / Socios)
    'domestic private': '#1f77b4',   # Azul institucional (Privado local)
    'foreign private': '#ff7f0e',    # Naranja (Privado extranjero)
    'investment fund': '#9467bd',    # Púrpura (Fondos de inversión)
    'hybrid': '#8c564b',             # Marrón (Híbrido / Mixto)
    'corporate-MCO': '#d62728',      # Rojo (Multipropiedad corporativa)
    'state-linked': '#e377c2',       # Rosa / Geopolítico (Vinculado a Estado)
    'unknown': '#7f7f7f'             # Gris neutro (No identificado / Ruido)
}

# Paleta por ligas
LEAGUE_COLORS = {
    'Bundesliga': '#000000',
    'LaLiga': '#ee1c25',
    'Ligue 1': '#091c3e',
    'Premier League': '#38003c',
    'Serie A': '#008fd7'
}

print("Entorno científico y paletas configurados correctamente.")""")

    # ==================== CELL 2: LOAD DATA ====================
    add_md("""## 2. Carga del Panel de Propiedad Dinámica y Auditoría Longitudinal (2019-2024)

Cargamos el dataset micro que integra la participación activa de los clubes en Primera División junto con su clasificación de propiedad exacta y dinámica en cada temporada.""")

    add_code("""# Cargar el dataset dinámico club-temporada
df_clubs = pd.read_csv('../data/dynamic_club_season_ownership.csv')

print(f"Total observaciones club-temporada activas: {len(df_clubs)}")
print(f"Total clubes únicos analizados: {df_clubs['club_id'].nunique()}")
print(f"Temporadas analizadas: {sorted(df_clubs['season'].unique())}")
print(f"Ligas incluidas: {df_clubs['league'].unique().tolist()}")

# Vista previa
df_clubs[['club_name', 'league', 'season', 'ownership_model', 'ultimate_owner', 'mco', 'state_link']].head(10)""")

    # ==================== CELL 3: OPERATIONALIZATION ====================
    add_md("""## 3. Operacionalización Cuantitativa del Ownership Landscape (RQ1)

A partir de la distribución de clubes en cada liga-temporada, calculamos las métricas macro-configuracionales del Ownership Landscape:

1. **Proporciones Composicionales ($p_i$)**: 
   $$p_{i,l,t} = \\frac{n_{i,l,t}}{N_{l,t}} \\quad \\text{con} \\quad \\sum_{i=1}^K p_{i,l,t} = 1.0$$
2. **Entropía de Shannon ($H$)**: Mide la diversidad, dispersión y grado de equilibrio del landscape:
   $$H_{l,t} = - \\sum_{i=1}^K p_{i,l,t} \\ln(p_{i,l,t})$$
3. **Índice Herfindahl-Hirschman ($HHI$)**: Mide el grado de concentración o monopolización de modelos:
   $$HHI_{l,t} = \\sum_{i=1}^K p_{i,l,t}^2$$
4. **Tasa de Multipropiedad ($MCO\\ Rate$)**: Proporción de clubes integrados en redes multipropiedad.
5. **Tasa de Vínculo Estatal ($State\\ Link\\ Rate$)**: Proporción de clubes con vínculos geopolíticos soberanos.""")

    add_code("""# Cargar la matriz agregada liga-temporada
df_ol = pd.read_csv('../data/dynamic_ownership_landscape.csv')

models = [
    'member-owned', 'domestic private', 'foreign private', 
    'investment fund', 'hybrid', 'corporate-MCO', 
    'state-linked', 'unknown'
]

print(f"Matriz de Ownership Landscape: {df_ol.shape[0]} observaciones (5 ligas x 6 temporadas)")
df_ol[['league', 'season', 'n_clubs', 'entropy', 'hhi', 'mco_rate', 'state_link_rate']].head(10)""")

    # ==================== CELL 4: PROFILES & DESCRIPTIVE SNAPSHOT ====================
    add_md("""## 4. Análisis Descriptivo y Comparativa de Perfiles por Liga (Snapshot 2024)

Comparamos la foto inicial de la muestra (2019) con el cierre del estudio (2024) para identificar las transformaciones estructurales de cada liga.""")

    add_code("""# Tabla comparativa 2019 vs 2024
summary_table = []
for league in sorted(df_ol['league'].unique()):
    row_19 = df_ol[(df_ol['league'] == league) & (df_ol['season'] == 2019)].iloc[0]
    row_24 = df_ol[(df_ol['league'] == league) & (df_ol['season'] == 2024)].iloc[0]
    
    # Encontrar modelo dominante en 2024
    props_24 = {m: row_24[f'prop_{m}'] for m in models}
    dom_mod = max(props_24, key=props_24.get)
    dom_pct = props_24[dom_mod] * 100
    
    summary_table.append({
        'Liga': league,
        'Clubes': f"{row_19['n_clubs']} -> {row_24['n_clubs']}",
        'Entropía (2019 -> 2024)': f"{row_19['entropy']:.3f} -> {row_24['entropy']:.3f}",
        'HHI (2019 -> 2024)': f"{row_19['hhi']:.3f} -> {row_24['hhi']:.3f}",
        'MCO Rate (2019 -> 2024)': f"{row_19['mco_rate']*100:.1f}% -> {row_24['mco_rate']*100:.1f}%",
        'State Link (2019 -> 2024)': f"{row_19['state_link_rate']*100:.1f}% -> {row_24['state_link_rate']*100:.1f}%",
        'Modelo Dominante 2024': f"{dom_mod} ({dom_pct:.1f}%)"
    })

pd.DataFrame(summary_table)""")

    add_md("""### Visualización del Perfil de Propiedad por Liga (Temporada 2024)

El siguiente gráfico de barras apiladas ilustra la composición exacta del Ownership Landscape al cierre de la temporada 2024-2025.""")

    add_code("""df_2024 = df_ol[df_ol['season'] == 2024].copy().sort_values('league', ascending=False)
prop_cols = [f'prop_{m}' for m in models]

fig, ax = plt.subplots(figsize=(13, 6.5))
left = np.zeros(len(df_2024))

for m in models:
    col = f'prop_{m}'
    values = df_2024[col].values * 100
    ax.barh(df_2024['league'], values, left=left, label=m, color=MODEL_COLORS[m], edgecolor='white', height=0.65)
    left += values

ax.set_xlabel('Proporción de Clubes en Primera División (%)', fontweight='bold')
ax.set_title('Perfil Configuracional del Ownership Landscape por Liga (Temporada 2024-2025)', pad=15, fontweight='bold')
ax.set_xlim(0, 100)
ax.legend(title='Modelo de Propiedad', bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True)
plt.tight_layout()

# Exportar imagen a images/
os.makedirs('../images', exist_ok=True)
plt.savefig('../images/ownership_profiles_2024.png', dpi=300, bbox_inches='tight')
plt.show()""")

    add_md("""### Interpretación de los Perfiles de Propiedad (Snapshot 2024)
* **Bundesliga (Landscape Tradicional y Homogéneo)**: Dominancia absoluta del modelo democrático (`member-owned`: $66.7\\%$), blindado por la regla del 50+1. Es el entorno más concentrado y menos financiarizado de Europa.
* **Premier League (Ecosistema Global y Financiarizado)**: Máxima penetración de capital transnacional y multipropiedad (`corporate-MCO`: $30.0\\%$, `foreign private`: $15.0\\%$, `investment fund`: $15.0\\%$). La tasa de MCO alcanza un récord del **$60.0\\%$** (12 de 20 clubes integrados en grupos multi-club).
* **LaLiga (Landscape Híbrido y Diverso)**: Coexistencia equilibrada de clubes de socios ($20.0\\%$), propiedad privada nacional ($25.0\\%$), extranjera ($15.0\\%$) y fondos ($10.0\\%$), alcanzando el mayor índice de diversidad del continente ($H = 1.805$).
* **Serie A y Ligue 1 (Privatización y Penetración de Fondos)**: Progresivo retroceso del empresariado familiar doméstico tradicional ante la entrada masiva de fondos de inversión internacionales y vehículos de capital riesgo.""")

    # ==================== CELL 5: LONGITUDINAL TRENDS ====================
    add_md("""## 5. Evolución Temporal de Diversidad, Concentración y Multipropiedad (2019-2024 - RQ2)

Analizamos las trayectorias longitudinales de las tres variables configuracionales clave a lo largo de las 6 temporadas.""")

    add_code("""fig, axes = plt.subplots(1, 3, figsize=(21, 6))

# Panel 1: Entropía de Shannon (Diversidad)
for league, color in LEAGUE_COLORS.items():
    data = df_ol[df_ol['league'] == league]
    axes[0].plot(data['season'], data['entropy'], marker='o', linewidth=2.5, label=league, color=color)
axes[0].set_title('A. Entropía de Shannon (Diversidad)', fontweight='bold')
axes[0].set_xlabel('Temporada')
axes[0].set_ylabel('Índice de Entropía ($H$)')
axes[0].set_xticks(range(2019, 2025))
axes[0].grid(True, alpha=0.3)

# Panel 2: Índice Herfindahl-Hirschman (Concentración)
for league, color in LEAGUE_COLORS.items():
    data = df_ol[df_ol['league'] == league]
    axes[1].plot(data['season'], data['hhi'], marker='s', linewidth=2.5, label=league, color=color)
axes[1].set_title('B. Concentración (Índice HHI)', fontweight='bold')
axes[1].set_xlabel('Temporada')
axes[1].set_ylabel('Índice HHI')
axes[1].set_xticks(range(2019, 2025))
axes[1].grid(True, alpha=0.3)

# Panel 3: Tasa de Multipropiedad (MCO Rate)
for league, color in LEAGUE_COLORS.items():
    data = df_ol[df_ol['league'] == league]
    axes[2].plot(data['season'], data['mco_rate'] * 100, marker='^', linewidth=2.5, label=league, color=color)
axes[2].set_title('C. Penetración de Multipropiedad (MCO %)', fontweight='bold')
axes[2].set_xlabel('Temporada')
axes[2].set_ylabel('% Clubes en Redes MCO')
axes[2].set_xticks(range(2019, 2025))
axes[2].grid(True, alpha=0.3)

axes[2].legend(title='Liga', bbox_to_anchor=(1.05, 1), loc='upper left', frameon=True)
plt.tight_layout()

# Exportar imagen a images/
plt.savefig('../images/temporal_indices.png', dpi=300, bbox_inches='tight')
plt.show()""")

    add_md("""### Interpretación de la Dinámica Longitudinal
1. **La Simetría de los Indicadores (El Espejo Matemático)**: Las curvas de Entropía y HHI reflejan trayectorias inversas y simétricas. La Bundesliga se mantiene plana en el extremo de alta concentración ($HHI \\approx 0.48$) y baja diversidad ($H \\approx 1.05$), mientras que LaLiga y la Premier League lideran consistentemente la diversidad ($H > 1.75$, $HHI < 0.19$).
2. **El Aumento Estructural de la Multipropiedad (MCO)**: La penetración de redes multi-club es un fenómeno en expansión acelerada en cuatro de las cinco ligas, alcanzando el **$60.0\\%$** en la Premier League, el **$30.0\\%$** en la Serie A, el **$27.8\\%$** en la Ligue 1 y el **$25.0\\%$** en LaLiga. La Bundesliga permanece inalterada en su nivel mínimo ($5.6\\%$), blindada institucionalmente.""")

    # ==================== CELL 6: PCA SECTION ====================
    add_md("""## 6. Trayectorias Configuracionales del OL: Análisis de Componentes Principales (PCA)

Para capturar la estructura multidimensional del Ownership Landscape sin colapsarla en un único índice escalar, aplicamos un **Análisis de Componentes Principales (PCA)** sobre las proporciones de los 8 modelos de propiedad estandarizadas.

---

### 6.1. Cargas de los Componentes Principales (Loadings)""")

    add_code("""# Estandarización y PCA
X = df_ol[prop_cols]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
coords = pca.fit_transform(X_scaled)
df_ol['PC1'] = coords[:, 0]
df_ol['PC2'] = coords[:, 1]

# Varianza explicada
var_pc1 = pca.explained_variance_ratio_[0] * 100
var_pc2 = pca.explained_variance_ratio_[1] * 100
var_total = var_pc1 + var_pc2

print(f"Varianza explicada PC1: {var_pc1:.2f}%")
print(f"Varianza explicada PC2: {var_pc2:.2f}%")
print(f"Varianza acumulada (PC1 + PC2): {var_total:.2f}%")

# Tabla de Cargas (Loadings)
loadings = pd.DataFrame(
    pca.components_.T, 
    index=[m.replace('prop_', '') for m in prop_cols], 
    columns=[f'PC1 ({var_pc1:.1f}%)', f'PC2 ({var_pc2:.1f}%)']
)
loadings""")

    add_md("""#### Interpretación de las Dimensiones:
*   **Componente Principal 1 (PC1 - Eje de Gobernanza Democrática vs. Financiarización/Privatización)**: 
    * *Cargas positivas fuertes*: `member-owned` ($+0.558$).
    * *Cargas negativas fuertes*: `foreign private` ($-0.480$), `investment fund` ($-0.391$) y `domestic private` ($-0.357$).
    * *Significado*: Separa los entornos basados en el control social democrático y la tradición comunitaria (derecha) de los paisajes basados en la inversión de capital privado y financiero (izquierda).
*   **Componente Principal 2 (PC2 - Eje de Estructuras Transnacionales e Híbridas vs. Privatización Uniclub Doméstica)**:
    * *Cargas positivas fuertes*: `hybrid` ($+0.529$), `corporate-MCO` ($+0.491$) y `state-linked` ($+0.225$).
    * *Cargas negativas fuertes*: `domestic private` ($-0.500$) y `unknown` ($-0.375$).
    * *Significado*: Separa las ligas que albergan estructuras corporativas supra-club transnacionales y modelos híbridos (arriba) de aquellas basadas en clubes comerciales individuales independientes (abajo).""")

    add_md("""---

### 6.2. Definición de los Cuadrantes del Espacio Configuracional

La intersección de los ejes neutros ($PC1=0$ y $PC2=0$) define cuatro cuadrantes analíticos:

*   **Cuadrante I (Superior Derecho: PC1 > 0, PC2 > 0) - Modelo Democrático con Estructuras Híbridas**: Entornos que combinan un fuerte control social de socios con fórmulas corporativas híbridas y marcas globales (ej. Bundesliga moderna y LaLiga híbrida).
*   **Cuadrante II (Superior Izquierdo: PC1 < 0, PC2 > 0) - Financiarización Transnacional y Multipropiedad (MCO)**: Paisajes altamente financiarizados y comercializados con penetración masiva de redes multi-club transnacionales o influencia geopolítica soberana (ej. Premier League).
*   **Cuadrante III (Inferior Derecho: PC1 > 0, PC2 < 0) - Democrático Tradicional Uniclub Puro**: Modelo tradicional del fútbol continental con clubes de socios independientes y aislados de redes corporativas.
*   **Cuadrante IV (Inferior Izquierdo: PC1 < 0, PC2 < 0) - Privatización Comercial Uniclub Doméstica**: Ligas dominadas por propietarios privados locales o individuales de cartera única, sin agregación en grandes grupos multipropiedad (ej. Serie A histórica y Ligue 1 tradicional).""")

    add_md("""---

### 6.3. Espacio Configuracional del PCA y Trayectorias Longitudinales (2019-2024)

Proyectamos las 30 observaciones liga-temporada en el plano bidimensional y conectamos cronológicamente cada liga con vectores direccionales.""")

    add_code("""plt.figure(figsize=(14, 9.5))

# Dibujar cuadrantes y ejes neutros
plt.axhline(0, color='grey', linestyle='--', linewidth=1.2, alpha=0.7)
plt.axvline(0, color='grey', linestyle='--', linewidth=1.2, alpha=0.7)

# Etiquetas de los cuadrantes
plt.text(2.6, 2.5, 'Cuadrante I\\n(Democrático / Híbrido)', fontsize=11, color='darkgreen', alpha=0.6, ha='center', style='italic')
plt.text(-2.2, 2.5, 'Cuadrante II\\n(Financiarización Transnacional MCO)', fontsize=11, color='darkred', alpha=0.6, ha='center', style='italic')
plt.text(2.6, -2.7, 'Cuadrante III\\n(Democrático Uniclub)', fontsize=11, color='darkgreen', alpha=0.6, ha='center', style='italic')
plt.text(-2.2, -2.7, 'Cuadrante IV\\n(Privatización Uniclub Doméstica)', fontsize=11, color='navy', alpha=0.6, ha='center', style='italic')

# Trazar puntos y flechas direccionales por liga
for league, color in LEAGUE_COLORS.items():
    data = df_ol[df_ol['league'] == league].sort_values('season')
    x = data['PC1'].values
    y = data['PC2'].values
    seasons = data['season'].values
    
    # Dibujar puntos
    plt.scatter(x, y, color=color, s=80, zorder=4)
    
    # Dibujar flechas entre temporadas consecutivas
    for i in range(len(x) - 1):
        plt.annotate(
            '', xy=(x[i+1], y[i+1]), xytext=(x[i], y[i]),
            arrowprops=dict(arrowstyle="->", color=color, lw=2.2, alpha=0.85, mutation_scale=15)
        )
    
    # Etiquetar inicio (2019) y fin (2024)
    plt.text(x[0], y[0] - 0.15, f"{league} '19", fontsize=10, fontweight='bold', color=color, ha='center')
    plt.text(x[-1], y[-1] + 0.12, f"{league} '24", fontsize=10, fontweight='bold', color=color, ha='center')

plt.xlabel(f'PC1: Eje de Gobernanza Democrática vs. Financiarización/Privatización ({var_pc1:.1f}% varianza)', fontweight='bold')
plt.ylabel(f'PC2: Eje de Redes Transnacionales e Híbridas vs. Privatización Uniclub ({var_pc2:.1f}% varianza)', fontweight='bold')
plt.title('Trayectorias Configuracionales del Ownership Landscape en las Cinco Grandes Ligas (PCA 2019-2024)', pad=15, fontweight='bold')
plt.xlim(-3.0, 3.8)
plt.ylim(-3.3, 3.0)
plt.tight_layout()

# Exportar imagen a images/
plt.savefig('../images/pca_trajectories.png', dpi=300, bbox_inches='tight')
plt.show()""")

    add_md("""### Análisis Detallado de Trayectorias por Liga (2019-2024)
* **Bundesliga (Blindaje Institucional en el Lado Derecho)**: Ubicada firmemente en el extremo derecho ($PC1 > 2.6$). Refleja la estabilidad absoluta conferida por la regla del 50+1, desplazándose levemente hacia arriba en 2023-2024 por la restauración de derechos de voto del e.V. en el Hoffenheim.
* **Premier League (Consolidación en el Cuadrante II de la Globalización MCO)**: Situada en la parte superior izquierda ($PC2 > 2.0$, $PC1 < 0$). Combina la total ausencia de clubes de socios con la mayor concentración mundial de redes de multipropiedad y capital transnacional.
* **LaLiga (Equilibrio Híbrido en el Cuadrante I)**: Ubicada en la zona central superior ($PC1 > 0$, $PC2 > 0.5$). Sus clubes de socios tradicionales actúan como ancla hacia la derecha, mientras que sus modelos híbridos y la entrada de grupos como City Football Group la proyectan hacia el eje superior.
* **Serie A (La Gran Transformación Ascendente)**: Exhibe la trayectoria más espectacular del fútbol europeo. Inicia profundamente en el Cuadrante IV en 2019 ($PC1 = -0.72, PC2 = -2.88$, dominada por dueños locales familiares) y **asciende verticalmente hacia el eje neutro en 2024** ($PC2 = -0.43$), reflejando la colonización de la liga por fondos norteamericanos (Milan, Roma, Atalanta, Genoa, Fiorentina, Inter).
* **Ligue 1 (De la Privatización Local a las Redes Internacionales)**: Inicia en el Cuadrante IV ($PC2 = -2.37$) y asciende de forma continuada ($PC2 = -0.21$ en 2024), impulsada por la compra recurrente de clubes franceses por grupos transnacionales (Strasbourg, Toulouse, Lyon, Troyes).""")

    # ==================== CELL 7: ROBUSTNESS & SENSITIVITY ====================
    add_md("""---

### 6.4. Validación de Robustez: PCA Composicional (CLR) y Análisis de Procrustes

Para verificar que la restricción de suma unitaria ($1.0$) de los datos composicionales y la categoría *unknown* no introducen sesgos, aplicamos la transformación **Centered Log-Ratio (CLR)** (Pawlowsky-Glahn et al., 2015) y el test de similitud de **Procrustes**.""")

    add_code("""# 1. Transformación CLR (Centered Log-Ratio)
X_coda = df_ol[prop_cols].drop(columns=['prop_unknown'])
X_coda = X_coda.div(X_coda.sum(axis=1), axis=0) + 1e-5
X_coda = X_coda.div(X_coda.sum(axis=1), axis=0)

log_X = np.log(X_coda)
clr_X = log_X.sub(log_X.mean(axis=1), axis=0)
clr_scaled = scaler.fit_transform(clr_X)

pca_clr = PCA(n_components=2)
coords_clr = pca_clr.fit_transform(clr_scaled)

# 2. Correlaciones entre PCA convencional y CLR-PCA
corr_pearson = np.corrcoef(coords[:, 0], coords_clr[:, 0])[0, 1]
corr_spearman, _ = spearmanr(coords[:, 0], coords_clr[:, 0])

# 3. Test de Procrustes
_, _, disparity = procrustes(coords, coords_clr)
procrustes_sim = np.sqrt(1 - disparity)

print("=== RESULTADOS DE VALIDACIÓN Y ROBUSTEZ ===")
print(f"Correlación de Pearson en PC1 (Convencional vs. CLR): {abs(corr_pearson):.4f}")
print(f"Correlación de Spearman en PC1 (Convencional vs. CLR): {abs(corr_spearman):.4f}")
print(f"Similitud geométrica de Procrustes (R): {procrustes_sim:.4f}")
print(f"Disparidad residual de Procrustes (D): {disparity:.4f}")""")

    # ==================== CELL 8: CONCLUSIONS ====================
    add_md("""## 7. Discusión y Conclusiones Finales

El análisis dinámico y configuracional del **Ownership Landscape** en las cinco grandes ligas europeas (2019-2024) permite extraer las siguientes conclusiones fundamentales:

1. **La Estructura de Propiedad es un Fenómeno Colectivo y Dinámico (RQ1)**:
   El constructo del Ownership Landscape operacionalizado a través de proporciones composicionales, Entropía de Shannon ($H$), HHI y Análisis de Componentes Principales (PCA) demuestra ser un marco analítico altamente robusto y reproducible para tipificar los regímenes competitivos del fútbol europeo. La integración de 44 operaciones corporativas de cambio de control junto a la rotación deportiva revela que las ligas son ecosistemas en constante reconfiguración institucional.

2. **Divergencia Estructural entre Regímenes Ligueros (RQ2)**:
   * **El Modelo Proteccionista Alemán**: La Bundesliga constituye un caso único de estabilidad institucional. La regla del 50+1 opera como un cortafuegos eficaz que preserva la gobernanza democrática ($66.7\\%$) e impide la penetración masiva de fondos especulativos o redes multipropiedad ($5.6\\%$).
   * **El Polo de Financiarización Británico**: La Premier League representa la frontera de la globalización corporativa, liderando la penetración de multipropiedad ($60.0\\%$) y configurando un entorno dominado por fondos de inversión y consorcios transnacionales.
   * **La Gran Transición Italiana y Francesa**: La Serie A y la Ligue 1 han experimentado una profunda transformación longitudinal, transitando desde paisajes de privatización uniclub doméstica tradicional hacia ecosistemas colonizados por firmas de inversión internacionales y grupos multi-club.
   * **La Vía Híbrida Española**: LaLiga mantiene un landscape equilibrado y de máxima diversidad, donde conviven clubes de socios, capital privado nacional y compras selectivas en red.

3. **Implicaciones de Política Regulatoria y Gobernanza**:
   El auge imparable de las redes de multipropiedad (MCO) y los fondos transnacionales plantea desafíos críticos para la integridad de las competiciones europeas (UEFA). Este estudio aporta una base cuantitativa para evaluar el impacto de las regulaciones de control financiero y restricciones de multipropiedad en la sostenibilidad y el equilibrio competitivo del fútbol global.""")

    # Save to notebooks folder
    os.makedirs("notebooks", exist_ok=True)
    out_path = "notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    
    print(f"Successfully generated {out_path} with {len(nb['cells'])} cells.")

if __name__ == "__main__":
    create_notebook()
