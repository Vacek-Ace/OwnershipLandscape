import os
import subprocess

docs_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape\docs"
eng_md_path = os.path.join(docs_dir, "methodology_ownership_landscape.md")

eng_content = """# Methodological Design: Measurement and Analysis of the Ownership Landscape (2019–2024)

This document details the quantitative methodology employed for the operationalization, measurement, and comparative analysis of the **Ownership Landscape** (OL) construct in elite European football. The focus is placed exclusively on the macro-configurational characterization of leagues through diversity and concentration indicators, as well as the dimensional reduction of the ownership space using Principal Component Analysis (PCA).

---

## 1. Research Design and Unit of Analysis

The study adopts a **quantitative, longitudinal, comparative, and exploratory design** with the purpose of offering a first empirical and reproducible approximation of the *Ownership Landscape* concept.

### Theoretical Distinction and Level of Aggregation
La premisa fundamental de este diseño es que el *Ownership Landscape* no es una propiedad individual de los clubes, sino una **propiedad emergente y colectiva del entorno competitivo** (la liga), en línea con la perspectiva de configuraciones organizacionales (Fiss, 2007). Por lo tanto:
* **Data collection unit**: The primary level of observation is the **club-season** (the ownership and financial characteristics of a specific club in a given year).
* **Unit of analysis**: The main level of aggregation is the **league-season** (the joint configuration resulting from the distribution of ownership models within a league in a given year).

### Analytical Tools and Their Collective Role
To capture the different dimensions of this collective structure, three complementary mathematical tools are employed:
1. **Shannon Entropy ($H$)**: Measures the degree of **diversity and evenness** of the landscape. It indicates whether multiple ownership logics coexist or if the system is dominated by a few.
2. **Herfindahl-Hirschman Index (HHI)**: Measures the degree of **concentration**. It evaluates the dominance of specific models and the level of homogeneity of the environment.
3. **Principal Component Analysis (PCA)**: Projects the **joint configuration** (the simultaneous proportions of all ownership models) into a low-dimensional space (2D) to classify leagues, track historical trajectories, and visualize the configurational distance between them.

This design has a strictly **methodological and descriptive** purpose. It does not seek to establish definitive causal relationships or conclusively validate complex predictive hypotheses, but rather to propose a standardized and reproducible framework to measure, compare, and historicize the ownership structures of contemporary football.

---

## 2. Empirical Context and Sample Construction

### League Selection Criteria
The empirical sample comprises the first divisions of the five major European football leagues (the "Big Five"): **Bundesliga** (Germany), **LaLiga** (Spain), **Ligue 1** (France), **Premier League** (England), and **Serie A** (Italy). The selection of these settings is justified under two criteria:
1. **Economic and institutional relevance**: They represent the financial and sporting core of global football.
2. **Configurational variation**: Disparate regulatory and traditional frameworks coexist, from the protectionism of the "50+1" rule in Germany to the extreme deregulation and financialization of the Premier League.

### Temporal Window (2019-2024)
The study analyzes a period of **6 complete seasons** spanning from the **2019-2020** to the **2024-2025** seasons (identified in the study by their start years as 2019 and 2024, respectively). This temporal window is ideal because it captures:
* The stability and resilience of traditional models against external shocks (COVID-19).
* The acceleration of institutional transformation processes, such as the penetration of international private investment funds and the consolidation of multi-club ownership (MCO) networks.

### Dynamic Panel Construction
To accurately reflect the real market structure of each season, the panel is constructed **dynamically** rather than statically. The clubs that actually participated in the first division of each league in each specific season are identified. This implies:
1. **Inclusion of promotions and exclusion of relegations**: Each year, the club sample varies for each league, reflecting the impact of sporting rotation on the macro landscape.
2. **Record harmonization**: An algorithmic and manual matching of club names from official league match databases with their respective financial identifiers and corporate registries is performed.
3. **Integration**: Each club-season observation is associated with its corresponding ownership classification for that year.

The resulting final sample of the panel comprises:
* **176 unique clubs**.
* **584 club-season observations** (used to characterize micro behavior and baseline distributions).
* **30 league-season observations** (the 30 macro configurations analyzed: 5 leagues $\times$ 6 transition years/seasons between 2019 and 2024).

*Note on temporal reference*: The reference point to determine the ownership structure of a club in a given season is the **closing of the summer transfer market** (August/September) of the corresponding season, as this milestone sets the planning and capital available for the annual competitive cycle.

---

## 3. Data Sources and Ownership Classification

### Corporate Information Sources
To identify the Ultimate Beneficial Owner (UBO) or the legal entity exercising effective voting control (greater than 50% or agreed management control) in each club-season observation, data was collected and triangulated from the following sources:
* Official corporate documents and national business registries (e.g., *Companies House* in the UK, *Infogreffe* in France).
* Club annual financial reports and national association governance reports (e.g., reports from the DNCG in France, resolutions of the Consejo Superior de Deportes in Spain).
* Official club websites and corporate press releases from investment groups.
* Specialized football finance databases (e.g., *UEFA Club Licensing reports*) and reputable journalistic outlets (e.g., *The Athletic*, *Off The Pitch*, *Bloomberg*).

### Taxonomy of Ownership Models
To classify and analyze ownership models in contemporary football, a taxonomy adapted from UEFA (2024) financial reports and sports economics and governance literature (e.g., Nauright & Ramfjord, 2010; Storm & Nielsen, 2012) is adopted. A classification of **7 substantive categories** based on majority or decisive control is employed:

1. **Member-owned (Democratic/Socios)**: Clubs democratically controlled by their members under the "one member, one vote" principle (e.g., Real Madrid, FC Bayern München).
2. **Domestic private (Private Local)**: Controlled by a natural person, family, or company of local/national origin (e.g., the traditional local businessman model).
3. **Foreign private (Private Foreign)**: Controlled by a foreign entrepreneur or family consortium not classified as a financial fund (e.g., the Glazer family at Manchester United pre-2024).
4. **Investment fund (Institutional/Financial)**: Controlled by venture capital firms, hedge funds, pension funds, or institutional financial investment vehicles whose primary goal is financial return or asset appreciation (e.g., RedBird Capital at AC Milan, Oaktree at Inter).
5. **Hybrid (Mixed)**: Structures with public listing or statutory division where democratic member control and the investment of influential but minority commercial partners formally coexist (e.g., Borussia Dortmund, where the members' club and sponsors like Evonik or Puma coexist).
6. **Corporate-MCO (Multi-Club Networks)**: Clubs formally integrated within trans-national corporate networks specializing in sports multi-club ownership, where the club operates under group synergies (e.g., Manchester City under City Football Group, RB Leipzig under Red Bull).
7. **State-linked (Sovereign/Geopolitical)**: Clubs under the effective control of state corporations, sovereign wealth funds, or investment vehicles directly linked to national governments (e.g., Paris Saint-Germain under Qatar Sports Investments, Newcastle United under the Saudi PIF).

### Treatment of Special Cases and Codebook
To ensure consistency, classification is governed by a **methodological codebook** that defines clear rules for ambiguities:
* **Consortia and multiple investors**: Classified according to the majority controlling partner or leading management vehicle.
* **Dispersed ownership / Listed companies**: Classified as *domestic/foreign private* or *investment fund* based on the nature of the controlling block that dominates the board of directors.
* **Static nature of the model by club**: In the analyzed panel, the ownership classification of each club is kept constant across the seasons of the study (representing their consolidated control model). Therefore, the interannual variation of the macro Ownership Landscape is driven exclusively by sporting rotation (promotions and relegations of teams between the first and second division), and not by transactional changes of owner within a club during the analyzed period.

### Treatment of the "Unknown" Category
The **Unknown** category represents unresolved cases of information (e.g., opaque trust structures, undeclared shell companies, or missing data). Methodologically:
* **It is not treated as a substantive ownership model**, but as information noise.
* For the landscape analysis, its proportion is transparently recorded at the descriptive level.
* In the configurational (PCA) and diversity (Shannon and HHI) analyses, the sensitivity of the model is evaluated through two pathways: exclusion and re-normalization versus direct inclusion. In our sample, its prevalence is marginal (averaging $1.74\%$ of the sample, with a maximum of $10\%$ in isolated observations), so its inclusion does not distort the substantive components.

---

## 4. Construction of the Ownership Landscape (OL)

The step from individual club classification to the aggregate scale of the league is performed by calculating **compositional proportions**.

For each ownership model $i$ ($i \in \{1, 2, ..., K\}$), league $l$, and season $t$, its representation proportion $p_{i,l,t}$ is calculated:

$$p_{i,l,t} = \frac{n_{i,l,t}}{N_{l,t}}$$

Where:
* $n_{i,l,t}$ is the number of clubs in the first division of league $l$ during season $t$ classified under ownership model $i$.
* $N_{l,t}$ is the total number of active clubs analyzed in that league-season.

The resulting matrix $\mathbf{P}$ of dimensions $30 \times 8$ (or $30 \times 7$ if *unknown* is excluded) completely and continuously describes the composition of each Ownership Landscape. The rows correspond to league-season observations and the columns to the proportions of the ownership models, satisfying the unit-sum constraint:

$$\sum_{i=1}^{K} p_{i,l,t} = 1.0$$

### Methodological Distinction of the Indicators
It is essential to highlight the difference in the treatment of the information in matrix $\mathbf{P}$:
* **Shannon and HHI** are one-dimensional summary measures. They collapse the distribution of proportions into a single scalar indicator, losing information about *which* specific models generate that diversity or concentration.
* **PCA** preserves the configurational and multidimensional nature of the data. It does not reduce the landscape to a single balance figure, but rather projects the similarities and differences between specific combinations of ownership models, allowing the identification of clusters and specific evolutionary trajectories.

### Ownership Profile Structure (Composition Example)
As a graphical representation of the composition of matrix $\mathbf{P}$, the following figure shows the structural composition of the Ownership Landscape of the five analyzed leagues at the close of the 2024 reference season:

![Configurational Structure of the Ownership Landscape by League (2024 Season)](../images/ownership_profiles_2024.png)

---

## 5. Shannon Entropy and Herfindahl-Hirschman Index (HHI)

We present diversity and concentration as **complementary but analytically distinct** dimensions.

### Shannon Entropy
To measure the variety of ownership models and the degree of balance in their distribution within the league-season, the Shannon Entropy ($H_{l,t}$) is calculated, based on mathematical information theory (Shannon, 1948) and its subsequent conceptual adaptation to characterize diversity in ecological and social systems (Jost, 2006):

$$H_{l,t} = -\sum_{i=1}^{K} p_{i,l,t} \ln(p_{i,l,t})$$

*Where by definition $0 \ln(0) = 0$.*
The Shannon Entropy ($H_{l,t}$) takes values in the interval $[0, \ln(K)]$, where $K$ is the maximum number of possible ownership categories ($K=7$ substantive models in our analysis). A value of $0$ represents absolute homogeneity (the entire league under a single ownership model) and the maximum value of $\ln(K)$ represents perfect balance (an identical distribution of clubs among all ownership categories). Since the catalog of categories is constant for all observations in the panel, the indicator is directly comparable across leagues.

### Herfindahl-Hirschman Index (HHI)
To measure the dominance of one or a few categories over the total of the league-season, the Herfindahl-Hirschman Index ($HHI_{l,t}$) is calculated, which constitutes the classical standard for evaluating market concentration and assessing the degree of competition sector (U.S. DOJ & FTC, 2023):

$$HHI_{l,t} = \sum_{i=1}^{K} p_{i,l,t}^{2}$$

The HHI ranges in the interval $[1/K, 1.0]$. A high HHI value denotes high concentration (one model clearly dominates), while low values indicate a fragmented landscape.

### Non-Equivalent Relationship
Although entropy and HHI strongly correlate in general terms, **they are not interchangeable**:
* **Shannon Entropy** is more sensitive to the presence of minority categories and the overall evenness of the distribution (uniform distribution).
* **HHI** penalizes deviations from balance quadratically, giving much more weight and importance to the dominant categories of the landscape.
Therefore, the evolution of both indicators is not symmetrical in the face of changes in minority models, providing complementary information for structural analysis.

### Historical Trends in Diversity and Concentration Indices
The evolution of these two one-dimensional indicators ($H_{l,t}$ and $HHI_{l,t}$), along with the multi-club ownership (MCO) rate, is visualized in the three panels below for the 2019-2024 temporal window:

![Evolution of Ownership Diversity, Concentration, and Multi-Club Ownership (2019-2024)](../images/temporal_indices.png)

---

## 6. Principal Component Analysis (PCA)

PCA is used to reduce the dimensionality of the proportion matrix $\mathbf{P}$ and represent the configurational differences of the 30 league-season observations in a two-dimensional plane.

### Parameters of the Conventional PCA
The conventional Principal Component Analysis (PCA), parameterized following contemporary dimensional reduction guidelines (Jolliffe & Cadima, 2016), is applied through the following procedure:
1. **Variables Included**: The proportions of the 8 ownership models (`prop_member-owned`, `prop_domestic private`, `prop_foreign private`, `prop_investment fund`, `prop_hybrid`, `prop_corporate-MCO`, `prop_state-linked`, and `prop_unknown`).
2. **Standardization**: Since proportions have similar scales but highly different variances (e.g., `member-owned` has high values in Germany and zero in England), the variables are centered and standardized to have mean 0 and standard deviation 1. This prevents high-proportion models from spuriously dominating over low-proportion but configurationally highly relevant models (e.g., `state-linked`).
3. **Component Selection Criterion**: The first two principal components (PC1 and PC2) are selected following Kaiser's criterion (eigenvalues greater than 1) and the scree plot analysis, explaining a combined **$72.5\%$** of the accumulated variance of the ownership structure.
4. **Interpretation of Loadings**: The components are not labeled *a priori*, but rather based on the observed correlation of the original variables:
   * **PC1 ($48.0\%$ of variance)**: Acts as the **Internationalization and Financialization Axis**. It has high positive loadings on `investment fund`, `foreign private`, and `corporate-MCO`, and high negative loadings on `member-owned` and `hybrid`.
   * **PC2 ($24.5\%$ of variance)**: Acts as the **Traditional Concentration vs. Financial Capital Axis**. It separates landscapes dominated by corporate investment and funds from landscapes of private domestic or traditional uniclub privatization.
5. **Trajectory Visualization**: The coordinates (*scores*) of the 30 league-season observations are projected in the PC1-PC2 space. To capture the dynamic of historical change, the years of each league (from 2019 to 2024) are sequentially connected through directional vectors (arrows), visualizing whether the leagues converge or diverge over time.

The projection of the longitudinal trajectories of each league landscape in the two-dimensional PC1-PC2 space is presented below, divided by the described analytical quadrants:

![Historical Configurational Trajectories of Ownership Landscapes (PCA 2019-2024)](../images/pca_trajectories.png)

### Treatment of Compositional Data (CoDa)
The proportions of the Ownership Landscape matrix are compositional data by definition (they sum to 1.0 and are bounded in the simplex space). Consequently, in accordance with contemporary methodological theory for compositional data analysis (Pawlowsky-Glahn et al., 2015), two methodological approaches are applied to ensure statistical robustness:
* **Reference Approach (Conventional PCA)**: Conventional PCA is performed on the standardized proportions to maintain the direct legibility of the simple Euclidean distances of the proportions.
* **Sensitivity Approach (Compositional PCA)**: A **Centered Log-Ratio (CLR)** transformation is applied to the proportions (adding a residual constant of $1\times 10^{-5}$ to zero proportions to avoid mathematical indeterminacies of logarithms) before performing the PCA (Pawlowsky-Glahn et al., 2015). The CLR projects the data out of the simplex to avoid spurious correlation problems and induce true orthogonality. The results and spatial ordering of both analyses are contrasted and verified in the sensitivity tests.

---

## 7. Sensitivity, Robustness, and Reproducibility

To validate the methodological soundness of the descriptive and configurational results obtained, the following robustness tests were implemented:

* **Conventional vs. Compositional PCA (CLR)**: The scores of the 30 league-season observations obtained under both approaches were correlated. The Spearman rank correlation for the first principal component (PC1, the Internationalization and Financialization Axis) exceeded **$0.96$** in absolute value. This empirically confirms that the main axis of league differentiation and internationalization is highly stable and robust, and is not affected by the constant-sum constraint of the compositional simplex (Pawlowsky-Glahn et al., 2015).
* **Stability Without the "Unknown" Category**: The PCA was repeated after excluding the `unknown` proportion and re-normalizing the remaining 7 substantive categories to $1.0$ using the formula $p'_{i} = p_{i} / (1 - p_{unknown})$. The geometric comparison of the relative position of the 30 league-season observations in the two-dimensional plane yielded a Procrustes correlation of **$0.985$**, rigorously validating that the presence of unresolved data does not introduce bias or affect the configurational validity of the study.

### Reproducibility and Software Infrastructure
The analysis was executed using **Python 3.13** in a reproducible development environment with the following scientific support libraries:
* Data processing and matrix manipulation: `pandas (v2.2)` and `numpy (v1.26)`.
* Statistical modeling and dimensional analysis: `scikit-learn (v1.4)`.
* High-quality graphical visualization: `matplotlib (v3.8)` and `seaborn (v0.13)`.

---

## 8. References

Fiss, P. C. (2007). A set-theoretic approach to organizational configurations. *Academy of Management Review*, 32(4), 1180–1198. https://doi.org/10.5465/amr.2007.26586092

Jolliffe, I. T., & Cadima, J. (2016). Principal component analysis: a review and recent developments. *Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 374(2065), 20150202. https://doi.org/10.1098/rsta.2015.0202

Jost, L. (2006). Entropy and diversity. *Oikos*, 113(2), 363–375. https://doi.org/10.1111/j.2006.0030-1299.14714.x

Nauright, J., & Ramfjord, J. (2010). Who owns England's game? American professional sports ownership in the English Premier League. *Soccer & Society*, 11(4), 428–441. https://doi.org/10.1080/14660971003780321

Pawlowsky-Glahn, V., Egozcue, J. J., & Tolosana-Delgado, R. (2015). *Modeling and Analysis of Compositional Data*. John Wiley & Sons. https://doi.org/10.1002/9781119003144

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

Storm, R. H., & Nielsen, K. (2012). Soft budget constraints in professional football. *European Sport Management Quarterly*, 12(2), 183–201. https://doi.org/10.1080/16184742.2012.670660

UEFA. (2024). *The European Club Finance and Investment Landscape Report*. UEFA. https://ecfil.uefa.com/2024

U.S. Department of Justice & Federal Trade Commission. (2023). *Merger Guidelines*. U.S. DOJ & FTC. https://www.ftc.gov/reports/merger-guidelines-2023
"""

# Wait, let's fix the spanish paragraph in line 12:
# In my translation above:
# "La premisa fundamental de este diseño es que el *Ownership Landscape* no es una propiedad individual de los clubes, sino una **propiedad emergente y colectiva del entorno competitivo** (la liga), en línea con la perspectiva de configuraciones organizacionales (Fiss, 2007). Por lo tanto:"
# Let's write it in English in the script:
# "The fundamental premise of this design is that the *Ownership Landscape* is not an individual property of clubs, but rather an **emergent and collective property of the competitive environment** (the league), in line with the organizational configurations perspective (Fiss, 2007). Therefore:"
eng_content = eng_content.replace(
    "La premisa fundamental de este diseño es que el *Ownership Landscape* no es una propiedad individual de los clubes, sino una **propiedad emergente y colectiva del entorno competitivo** (la liga), en línea con la perspectiva de configuraciones organizacionales (Fiss, 2007). Por lo tanto:",
    "The fundamental premise of this design is that the *Ownership Landscape* is not an individual property of clubs, but rather an **emergent and collective property of the competitive environment** (the league), in line with the organizational configurations perspective (Fiss, 2007). Therefore:"
)

with open(eng_md_path, "w", encoding="utf-8") as f:
    f.write(eng_content.strip())
print("Successfully created methodology_ownership_landscape.md in English")
