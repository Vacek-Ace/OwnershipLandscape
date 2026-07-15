import os
import subprocess

docs_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape\docs"
metodo_es = os.path.join(docs_dir, "metodologia_ownership_landscape.md")
metodo_en = os.path.join(docs_dir, "methodology_ownership_landscape.md")

# New Spanish PCA Section
new_pca_es = """## 6. Análisis de Componentes Principales (PCA)

El PCA se utiliza para reducir la dimensionalidad de la matriz de proporciones $\\mathbf{P}$ y representar en un plano bidimensional las diferencias configuracionales de las 30 observaciones liga-temporada.

### 6.1. Cargas de los Componentes Principales (Loadings)

Para comprender la estructura geométrica del espacio configuracional, se calculan las cargas de las variables en los dos primeros componentes principales (PC1 y PC2), los cuales explican de forma conjunta el **$72.5\\%$** de la varianza acumulada de la estructura de propiedad:

| Modelo de Propiedad | Carga PC1 ($48.0\\%$) | Carga PC2 ($24.5\\%$) |
| :--- | :---: | :---: |
| **Member-owned** (`prop_member-owned`) | $-0.463$ | $-0.247$ |
| **Domestic private** (`prop_domestic private`) | $+0.448$ | $-0.270$ |
| **Foreign private** (`prop_foreign private`) | $+0.441$ | $+0.143$ |
| **Investment fund** (`prop_investment fund`) | $+0.484$ | $+0.086$ |
| **Hybrid** (`prop_hybrid`) | $-0.359$ | $+0.279$ |
| **Corporate-MCO** (`prop_corporate-MCO`) | $+0.040$ | $+0.630$ |
| **State-linked** (`prop_state-linked`) | $-0.134$ | $+0.445$ |
| **Unknown** (`prop_unknown`) | $-0.091$ | $-0.406$ |

#### Interpretación de las Dimensiones:
*   **Componente Principal 1 (PC1 - Eje de Internacionalización y Financiarización)**: Este eje (que explica el $48.0\\%$ de la varianza) discrimina entre modelos basados en el capital financiero e internacional y aquellos de control social y tradicional. Los valores **positivos** en este eje están determinados por lógicas comerciales avanzadas: fondos de inversión ($+0.484$), capital privado nacional ($+0.448$) y capital privado extranjero ($+0.441$). Por el contrario, los valores **negativos** representan el blindaje de la gobernanza asociativa: clubes de socios ($-0.463$) y modelos mixtos híbridos ($-0.359$).
*   **Componente Principal 2 (PC2 - Eje de Estructuras Transnacionales y Geopolíticas)**: Este eje (que explica el $24.5\\%$ de la varianza) separa las ligas que albergan estructuras de propiedad complejas integradas en redes supra-club de aquellas compuestas por entidades uniclub tradicionales. Los valores **positivos** corresponden a estructuras corporativas de multipropiedad (`corporate-MCO`: $+0.630$) y vehículos con vínculos estatales o geopolíticos soberanos (`state-linked`: $+0.445$). Los valores **negativos** señalan la dominancia de clubes individuales independientes y tradicionales (`unknown`: $-0.406$, `domestic private`: $-0.270$, y `member-owned`: $-0.247$).

---

### 6.2. Espacio Configuracional: Definición de los Cuadrantes

La intersección de los ejes PC1 y PC2 delimita **cuatro cuadrantes configuracionales** bien definidos que representan diferentes lógicas competitivas y modelos de negocio:

*   **Cuadrante I (Superior Derecho: PC1 > 0, PC2 > 0) - Financiarización Transnacional MCO**: Representa paisajes de propiedad altamente financiarizados (fondos de inversión, propietarios extranjeros) que además están integrados de forma masiva en redes multipropiedad (MCO) o bajo la influencia directa de estados soberanos. Es el cuadrante de la globalización corporativa y las marcas globales.
*   **Cuadrante II (Superior Izquierdo: PC1 < 0, PC2 > 0) - Híbrido / Colectivo con Redes**: Representa paisajes de propiedad que conservan una fuerte base de control social o democrático local (valores negativos de PC1) pero que incorporan lógicas corporativas superiores, participación híbrida o una penetración moderada de redes de multipropiedad (valores positivos de PC2). LaLiga española (debido a su fuerte presencia de clubes híbridos y de socios, combinada con compras controladas de MCO como el Girona) y la Premier League en sus años de menor financiarización extrema se ubican en este cuadrante.
*   **Cuadrante III (Inferior Izquierdo: PC1 < 0, PC2 < 0) - Democrático y Tradicional Uniclub**: Representa el modelo clásico del fútbol europeo: clubes gobernados democráticamente por sus socios locales que operan de forma independiente como entidades locales individuales, aislados de multipropiedades transnacionales o vehículos soberanos.
*   **Cuadrante IV (Inferior Derecho: PC1 > 0, PC2 < 0) - Privatización Comercial Uniclub**: Ligas dominadas por propietarios privados (nacionales o extranjeros) y vehículos financieros institucionales, pero estructuradas en torno a clubes que actúan como entidades comerciales independientes y de cartera individual, sin agregarse en grandes redes MCO transnacionales.

---

### 6.3. Análisis de Trayectorias y Cambios de Cuadrante (2019-2024)

Proyectando las coordenadas (*scores*) de las 30 observaciones liga-temporada en este plano, visualizamos las trayectorias longitudinales mediante vectores direccionales (flechas) de 2019 a 2024:

![Historical Configurational Trajectories of Ownership Landscapes (PCA 2019-2024)](../images/pca_trajectories.png)

A través del mapa bidimensional, se devela la existencia de senderos evolutivos dependientes de la trayectoria (*path dependency*) de cada liga:

*   **Bundesliga (Estabilidad Absoluta en el Cuadrante III)**: Inmóvil en la esquina inferior izquierda del plano (PC1 $\\approx -3.3$ y PC2 subiendo ligeramente de $-1.18$ a $-0.51$). Esto demuestra la extraordinaria efectividad institucional de la regla del 50+1 como blindaje contra la entrada de capital de riesgo y la multipropiedad transnacional, manteniendo su landscape bajo el modelo tradicional democrático y uniclub.
*   **LaLiga (Oscilación entre los Cuadrantes II y III)**: Se desplaza exclusivamente en la mitad izquierda del plano (PC1 siempre negativo), oscilando entre el Cuadrante II y el Cuadrante III. Inicia en 2019 en el Cuadrante II ($y = +0.21$), cae al Cuadrante III en 2020-2021 (alcanzando su punto más bajo en $y = -0.50$ debido al ascenso de clubes tradicionales), y retorna al Cuadrante II en 2024 ($y = +0.17$). Sus clubes de socios actúan como un ancla estructural a la izquierda, preservando su carácter híbrido y socialmente arraigado.
*   **Premier League (Trayectoria en los Cuadrantes II y I)**: Se mantiene de forma persistente en la parte superior del plano (PC2 > 2.1) debido a su altísima tasa de multipropiedad, oscilando en el límite vertical ($PC1=0$) entre el Cuadrante II y el Cuadrante I. Termina en 2024 consolidada en el Cuadrante I ($x \\approx 0.0, y = 2.62$). Representa la financiarización globalizada sin retorno, combinando propiedad transnacional con control corporativo en red.
*   **Serie A (Ascenso dentro del Cuadrante IV)**: Se ubica firmemente de principio a fin en el Cuadrante IV (PC1 > 2.0, PC2 < 0), pero muestra una clara trayectoria ascendente (subiendo desde $y = -1.55$ en 2019 hasta $y = -0.36$ en 2024). Esto refleja cómo el capital nacional tradicional está siendo reemplazado progresivamente por fondos de inversión internacionales (que inyectan capital comercial, elevando el PC2 de la liga) y ascensos de clubes bajo modelos privados corporativos.
*   **Ligue 1 (Cruces Dinámicos entre los Cuadrantes I y IV)**: Es la liga con las oscilaciones más marcadas del estudio. Inicia profundamente en el Cuadrante IV en 2019 ($y \\approx -1.90$), asciende al Cuadrante I en 2022 ($y = +0.44$), desciende al Cuadrante IV en 2023, y en 2024 vuelve a cruzar levemente al Cuadrante I ($y = +0.03$). Refleja la inestabilidad de las finanzas francesas, con compras recurrentes de clubes y oscilaciones entre MCO transnacionales y privatizaciones de cartera individual.

---

### 6.4. Tratamiento de Datos Composicionales (CoDa)

Las proporciones de la matriz de Ownership Landscape son datos composicionales por definición (suman 1.0 y están acotados en el espacio simplex). En consecuencia, de acuerdo con la teoría metodológica contemporánea para el análisis de datos composicionales (Pawlowsky-Glahn et al., 2015), se aplican dos aproximaciones metodológicas para asegurar la robustez estadística:
* **Enfoque de Referencia (Conventional PCA)**: Se realiza el PCA convencional sobre las proporciones estandarizadas para mantener la legibilidad directa de las distancias euclidianas simples de las proporciones.
* **Enfoque de Sensibilidad (Compositional PCA)**: Se aplica una transformación **Centered Log-Ratio (CLR)** sobre las proporciones (añadiendo una constante residual de $1\\times 10^{-5}$ a las proporciones nulas para evitar indeterminaciones matemáticas de logaritmos) antes de realizar el PCA (Pawlowsky-Glahn et al., 2015). El CLR proyécta los datos fuera del simplex para evitar problemas de correlación espuria e inducir ortogonalidad real. Los resultados y la ordenación espacial de ambos análisis se contrastan y verifican en las pruebas de sensibilidad.

"""

# New English PCA Section
new_pca_en = """## 6. Principal Component Analysis (PCA)

PCA is used to reduce the dimensionality of the proportion matrix $\\mathbf{P}$ and represent the configurational differences of the 30 league-season observations in a two-dimensional plane.

### 6.1. Principal Component Loadings

To understand the geometric structure of the configurational space, the loadings of the variables on the first two principal components (PC1 and PC2) are calculated. Together, these components explain **$72.5\\%$** of the accumulated variance of the ownership structure:

| Ownership Model | PC1 Loading ($48.0\\%$) | PC2 Loading ($24.5\\%$) |
| :--- | :---: | :---: |
| **Member-owned** (`prop_member-owned`) | $-0.463$ | $-0.247$ |
| **Domestic private** (`prop_domestic private`) | $+0.448$ | $-0.270$ |
| **Foreign private** (`prop_foreign private`) | $+0.441$ | $+0.143$ |
| **Investment fund** (`prop_investment fund`) | $+0.484$ | $+0.086$ |
| **Hybrid** (`prop_hybrid`) | $-0.359$ | $+0.279$ |
| **Corporate-MCO** (`prop_corporate-MCO`) | $+0.040$ | $+0.630$ |
| **State-linked** (`prop_state-linked`) | $-0.134$ | $+0.445$ |
| **Unknown** (`prop_unknown`) | $-0.091$ | $-0.406$ |

#### Dimension Interpretations:
*   **Principal Component 1 (PC1 - Internationalization and Financialization Axis)**: This axis (explaining $48.0\\%$ of the variance) discriminates between models based on financial and international capital and those based on traditional and social control. **Positive** values on this axis are determined by advanced commercial logics: investment funds ($+0.484$), domestic private ownership ($+0.448$), and foreign private ownership ($+0.441$). Conversely, **negative** values represent the shielding of associative governance: member-owned clubs ($-0.463$) and mixed hybrid models ($-0.359$).
*   **Principal Component 2 (PC2 - Transnational and Geopolitical Axis)**: This axis (explaining $24.5\\%$ of the variance) separates leagues housing complex ownership structures integrated into supra-club networks from those composed of traditional independent clubs. **Positive** values correspond to corporate multi-club networks (`corporate-MCO`: $+0.630$) and vehicles with state or geopolitical links (`state-linked`: $+0.445$). **Negative** values signal the dominance of traditional, independent individual clubs (`unknown`: $-0.406$, `domestic private`: $-0.270$, and `member-owned`: $-0.247$).

---

### 6.2. Configurational Space: Quadrant Definitions

The intersection of the PC1 and PC2 axes defines **four configurational quadrants** that represent different competitive logics and business models:

*   **Quadrant I (Top Right: PC1 > 0, PC2 > 0) - Transnational Financial MCO**: Represents highly financialized ownership landscapes (investment funds, foreign owners) that are also heavily integrated into multi-club ownership (MCO) networks or under the direct influence of sovereign states. It is the quadrant of corporate globalization and global brands.
*   **Quadrant II (Top Left: PC1 < 0, PC2 > 0) - Hybrid / Collective with Networks**: Represents ownership landscapes that preserve a strong baseline of local social or democratic control (negative PC1 values) but incorporate higher corporate logics, hybrid participation, or moderate penetration of multi-club networks (positive PC2 values). Spanish LaLiga (due to its strong presence of hybrid and member-owned clubs, combined with controlled MCO acquisitions like Girona) and the Premier League in its years of less extreme financialization are positioned in this quadrant.
*   **Quadrant III (Bottom Left: PC1 < 0, PC2 < 0) - Democratic and Traditional Uniclub**: Represents the classical model of European football: clubs democratically governed by local members operating independently as individual entities, isolated from transnational multi-club networks or sovereign investments.
*   **Quadrant IV (Bottom Right: PC1 > 0, PC2 < 0) - Private Commercial Uniclub**: Leagues dominated by private owners (domestic or foreign) and institutional financial vehicles, but structured around clubs acting as independent commercial and portfolio entities, without aggregating into large transnational MCO networks.

---

### 6.3. Trajectory Analysis and Quadrant Shifts (2019-2024)

By projecting the coordinates (*scores*) of the 30 league-season observations in this plane, we visualize the longitudinal trajectories using directional vectors (arrows) from 2019 to 2024:

![Historical Configurational Trajectories of Ownership Landscapes (PCA 2019-2024)](../images/pca_trajectories.png)

The two-dimensional map reveals the existence of path-dependent evolutionary paths for each league:

*   **Bundesliga (Absolute Stability in Quadrant III)**: Stationary in the bottom-left corner of the plane (PC1 $\\approx -3.3$ and PC2 rising slightly from $-1.18$ to $-0.51$). This demonstrates the extraordinary institutional effectiveness of the 50+1 rule as an absolute shield against the entry of venture capital and transnational MCO networks, keeping its landscape under the traditional democratic and uniclub model.
*   **LaLiga (Oscillation between Quadrants II and III)**: Shifts exclusively in the left half of the plane (PC1 always negative), oscillating between Quadrant II and Quadrant III. It starts in 2019 in Quadrant II ($y = +0.21$), falls to Quadrant III in 2020-2021 (reaching its lowest point at $y = -0.50$ due to the promotion of traditional clubs), and returns to Quadrant II in 2024 ($y = +0.17$). Its member-owned clubs act as a structural anchor to the left, preserving its hybrid and socially rooted character.
*   **Premier League (Trajectory in Quadrants II and I)**: Remains persistently in the upper part of the plane (PC2 > 2.1) due to its very high rate of multi-club ownership, oscillating on the vertical border ($PC1=0$) between Quadrant II and Quadrant I. It ends in 2024 consolidated in Quadrant I ($x \\approx 0.0, y = 2.62$). It represents globalized financialization with no return, combining transnational ownership with group corporate control.
*   **Serie A (Rise within Quadrant IV)**: Positioned firmly from start to finish in Quadrant IV (PC1 > 2.0, PC2 < 0), but shows a clear upward trajectory (rising from $y = -1.55$ in 2019 to $y = -0.36$ in 2024). This reflects how traditional domestic capital is being progressively replaced by international investment funds (which inject commercial capital, raising the league's PC2) and promotions of clubs under private corporate models.
*   **Ligue 1 (Dynamic Shifts between Quadrants I and IV)**: This is the league with the most marked oscillations in the study. It starts deep in Quadrant IV in 2019 ($y \\approx -1.90$), rises to Quadrant I in 2022 ($y = +0.44$), falls back to Quadrant IV in 2023, and in 2024 crosses slightly into Quadrant I again ($y = +0.03$). It reflects the instability of French football finances, with recurring club buyouts and shifts between transnational MCOs and individual private ownership.

---

### 6.4. Treatment of Compositional Data (CoDa)

The proportions of the Ownership Landscape matrix are compositional data by definition (they sum to 1.0 and are bounded in the simplex space). Consequently, in accordance with contemporary methodological theory for compositional data analysis (Pawlowsky-Glahn et al., 2015), two methodological approaches are applied to ensure statistical robustness:
* **Reference Approach (Conventional PCA)**: Conventional PCA is performed on the standardized proportions to maintain the direct legibility of the simple Euclidean distances of the proportions.
* **Sensitivity Approach (Compositional PCA)**: A **Centered Log-Ratio (CLR)** transformation is applied to the proportions (adding a residual constant of $1\\times 10^{-5}$ to zero proportions to avoid mathematical indeterminacies of logarithms) before performing the PCA (Pawlowsky-Glahn et al., 2015). The CLR projects the data out of the simplex to avoid spurious correlation problems and induce true orthogonality. The results and spatial ordering of both analyses are contrasted and verified in the sensitivity tests.

"""

# Apply modifications in Spanish file
if os.path.exists(metodo_es):
    with open(metodo_es, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Locate the start of Section 6 and end before Section 7
    start_token = "## 6. Análisis de Componentes Principales (PCA)"
    end_token = "## 7. Sensibilidad, Robustez y Reproducibilidad"
    
    parts = text.split(start_token)
    if len(parts) == 2:
        subparts = parts[1].split(end_token)
        if len(subparts) == 2:
            new_text = parts[0] + new_pca_es + "\n" + end_token + subparts[1]
            with open(metodo_es, "w", encoding="utf-8") as f:
                f.write(new_text)
            print("Successfully restructured Spanish PCA section!")
        else:
            print("Failed to find end_token in Spanish file")
    else:
        print("Failed to find start_token in Spanish file")

# Apply modifications in English file
if os.path.exists(metodo_en):
    with open(metodo_en, "r", encoding="utf-8") as f:
        text = f.read()
        
    start_token_en = "## 6. Principal Component Analysis (PCA)"
    end_token_en = "## 7. Sensitivity, Robustness, and Reproducibility"
    
    parts = text.split(start_token_en)
    if len(parts) == 2:
        subparts = parts[1].split(end_token_en)
        if len(subparts) == 2:
            new_text_en = parts[0] + new_pca_en + "\n" + end_token_en + subparts[1]
            with open(metodo_en, "w", encoding="utf-8") as f:
                f.write(new_text_en)
            print("Successfully restructured English PCA section!")
        else:
            print("Failed to find end_token in English file")
    else:
        print("Failed to find start_token in English file")

# Render updated files to Word
print("Re-rendering Spanish Word Document...")
subprocess.run(["quarto", "render", metodo_es, "--to", "docx"], shell=True)
print("Re-rendering English Word Document...")
subprocess.run(["quarto", "render", metodo_en, "--to", "docx"], shell=True)
print("Finished rendering both files")
