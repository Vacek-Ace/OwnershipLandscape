import os
import subprocess

docs_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape\docs"
metodo_es = os.path.join(docs_dir, "metodologia_ownership_landscape.md")
metodo_en = os.path.join(docs_dir, "methodology_ownership_landscape.md")

# 1. Update Spanish Methodology
if os.path.exists(metodo_es):
    with open(metodo_es, "r", encoding="utf-8") as f:
        text_es = f.read()
    
    # Insert interpretation 1 after figure 1:
    fig1_target = "![Configurational Structure of the Ownership Landscape by League (2024 Season)](../images/ownership_profiles_2024.png)"
    fig1_repl = fig1_target + "\n\n### Análisis Configuracional de los Perfiles (Snapshot 2024)\nLa composición detallada de la propiedad al cierre de la temporada 2024-2025 devela tres configuraciones estructurales diferenciadas en el fútbol europeo:\n1. **El Modelo Tradicional-Asociativo (Alemania)**: La Bundesliga exhibe una homogeneidad estructural excepcional dominada por el modelo democrático de socios (`member-owned`, $66.7\%$), blindado por la regla regulatoria del \"50+1\". Es el único entorno donde la multipropiedad transnacional y los fondos de inversión carecen de penetración significativa.\n2. **El Ecosistema Global y Financiarizado (Inglaterra)**: La Premier League representa el extremo opuesto, con una penetración masiva de multipropiedad corporativa (`corporate-MCO`, $30\%$) y capital privado extranjero (`foreign private`, $25\%$). La tasa de MCO alcanza un récord del $65.0\%$ (13 de 20 clubes), evidenciando la colonización de la liga por redes transnacionales y vehículos de capital de riesgo.\n3. **Los Paisajes Híbridos y de Transición (España, Italia y Francia)**: LaLiga española muestra una convivencia equilibrada de lógicas donde coexisten clubes democráticos ($20\%$), propiedad privada nacional ($25\%$), capital extranjero ($15\%$) e híbrido ($15\%$). Por su parte, la Serie A italiana y la Ligue 1 francesa muestran una fragmentación extrema marcada por la progresiva retirada de las familias locales tradicionales ante la entrada de fondos de inversión (`investment fund`, como en AC Milan o Inter) y redes de MCO."
    
    if fig1_target in text_es and "### Análisis Configuracional de los Perfiles" not in text_es:
        text_es = text_es.replace(fig1_target, fig1_repl)

    # Insert interpretation 2 after figure 2:
    fig2_target = "![Evolution of Ownership Diversity, Concentration, and Multi-Club Ownership (2019-2024)](../images/temporal_indices.png)"
    fig2_repl = fig2_target + "\n\n### Trayectorias de Diversidad y Concentración (2019-2024)\nLa evolución longitudinal de las métricas de diversidad ($H$) y concentración ($HHI$) durante las últimas seis temporadas ratifica tres dinámicas de cambio:\n* **La Simetría de los Indicadores (El Espejo Matemático)**: Los paneles longitudinales muestran curvas perfectamente invertidas entre la Entropía y el HHI. La Bundesliga se mantiene inmóvil en el extremo inferior de diversidad (Entropía $\approx 1.05$) y superior de concentración (HHI $\approx 0.48$), mientras que LaLiga y la Premier League lideran de forma constante el índice de diversidad (Entropía $> 1.70$, HHI $< 0.19$).\n* **La Volatilidad de la Serie A y Ligue 1**: Ambos entornos exhiben las mayores oscilaciones anuales. En la Serie A, la abrupta caída de la entropía hasta un mínimo de $1.290$ en 2023 refleja el proceso de colonización financiera del fútbol italiano, donde los fondos de inversión extranjeros y consorcios internacionales absorbieron y concentraron el control de los clubes históricos.\n* **La Expansión de la Multipropiedad (MCO)**: La tasa de MCO (panel derecho) es un fenómeno global al alza. Crece del $60\%$ al $65\%$ en la Premier League, alcanza el $30\%$ en la Serie A y el $27.8\%$ en la Ligue 1. La Bundesliga permanece inalterada en su nivel mínimo ($5.6\%$), actuando como una anomalía regulatoria en el continente."
    
    if fig2_target in text_es and "### Trayectorias de Diversidad y Concentración" not in text_es:
        text_es = text_es.replace(fig2_target, fig2_repl)

    # Insert interpretation 3 after figure 3:
    fig3_target = "![Historical Configurational Trajectories of Ownership Landscapes (PCA 2019-2024)](../images/pca_trajectories.png)"
    fig3_repl = fig3_target + "\n\n### Interpretación de los Cuadrantes y Trayectorias del PCA\nLa proyección bidimensional de las 30 observaciones liga-temporada devela la existencia de senderos evolutivos dependientes de la trayectoria (*path dependency*) y tipifica los entornos competitivos:\n* **Cuadrante III (Democrático y Tradicional Uniclub - Abajo a la Izquierda)**: La Bundesliga permanece inmóvil en este espacio (PC1 $\approx -3.3$). La regla 50+1 opera como un estabilizador institucional absoluto que impide que la liga se desplace hacia la financiarización o la multipropiedad transnacional.\n* **Cuadrante IV (Privatización Comercial Uniclub - Abajo a la Derecha)**: La Serie A italiana y la Ligue 1 francesa inician profundamente en este cuadrante, caracterizado por propietarios privados que actúan como entidades comerciales individuales. Sin embargo, la Serie A exhibe una clara trayectoria ascendente ($y = -1.55$ en 2019 a $y = -0.36$ en 2024), aproximándose al Cuadrante I a medida que los fondos y consorcios institucionales desplazan a los propietarios familiares locales.\n* **Cuadrante I (Financiarización Transnacional MCO - Arriba a la Derecha)**: Representa el ecosistema más financiarizado e integrado en redes globales. La Premier League y la Ligue 1 oscilan dinámicamente cruzando las fronteras de este cuadrante. La Premier League termina en 2024 en el límite superior ($y = 2.62$) por su altísima tasa de multipropiedad, consolidando una trayectoria de financiarización globalizada sin retorno al modelo tradicional."
    
    if fig3_target in text_es and "### Interpretación de los Cuadrantes y Trayectorias del PCA" not in text_es:
        text_es = text_es.replace(fig3_target, fig3_repl)

    with open(metodo_es, "w", encoding="utf-8") as f:
        f.write(text_es)
    print("Updated Spanish methodology markdown")

# 2. Update English Methodology
if os.path.exists(metodo_en):
    with open(metodo_en, "r", encoding="utf-8") as f:
        text_en = f.read()
    
    # Insert interpretation 1 after figure 1:
    fig1_target = "![Configurational Structure of the Ownership Landscape by League (2024 Season)](../images/ownership_profiles_2024.png)"
    fig1_repl = fig1_target + "\n\n### Configurational Analysis of the Profiles (2024 Snapshot)\nThe detailed composition of ownership at the close of the 2024-2025 season reveals three distinct structural configurations in European football:\n1. **The Traditional-Associative Model (Germany)**: The Bundesliga exhibits exceptional structural homogeneity dominated by the democratic member-owned model (`member-owned`, $66.7\%$), shielded by the \"50+1\" regulatory rule. It is the only setting where trans-national multi-club ownership and investment funds lack significant penetration.\n2. **The Global and Financialized Ecosystem (England)**: The Premier League represents the opposite extreme, with a massive penetration of corporate multi-club ownership (`corporate-MCO`, $30\%$) and foreign private capital (`foreign private`, $25\%$). The MCO rate reaches a record $65.0\%$ (13 out of 20 clubs), showcasing the colonization of the league by trans-national networks and venture capital vehicles.\n3. **Hybrid and Transition Landscapes (Spain, Italy, and France)**: Spanish LaLiga shows a balanced coexistence of logics where democratic clubs ($20\%$), domestic private ownership ($25\%$), foreign capital ($15\%$), and hybrid models ($15\%$) coexist. Meanwhile, Italian Serie A and French Ligue 1 show extreme fragmentation marked by the progressive retreat of traditional local families in the face of the entry of investment funds (`investment fund`, such as at AC Milan or Inter) and MCO networks."
    
    if fig1_target in text_en and "### Configurational Analysis of the Profiles" not in text_en:
        text_en = text_en.replace(fig1_target, fig1_repl)

    # Insert interpretation 2 after figure 2:
    fig2_target = "![Evolution of Ownership Diversity, Concentration, and Multi-Club Ownership (2019-2024)](../images/temporal_indices.png)"
    fig2_repl = fig2_target + "\n\n### Trajectories of Diversity and Concentration (2019-2024)\nThe longitudinal evolution of diversity ($H$) and concentration ($HHI$) metrics over the last six seasons confirms three dynamics of change:\n* **Indicator Symmetry (The Mathematical Mirror)**: The longitudinal panels show perfectly inverted curves between Entropy and HHI. The Bundesliga remains motionless at the lower extreme of diversity (Entropy $\approx 1.05$) and upper extreme of concentration (HHI $\approx 0.48$), while LaLiga and the Premier League constantly lead the diversity index (Entropy $> 1.70$, HHI $< 0.19$).\n* **Volatility in Serie A and Ligue 1**: Both environments exhibit the largest annual oscillations. In Serie A, the sharp drop in entropy to a minimum of $1.290$ in 2023 reflects the process of financial colonization of Italian football, where foreign investment funds and international consortia absorbed and concentrated control of historic clubs.\n* **The Expansion of Multi-Club Ownership (MCO)**: The MCO rate (right panel) is a global rising phenomenon. It grows from $60\%$ to $65\%$ in the Premier League, reaches $30\%$ in Serie A, and $27.8\%$ in Ligue 1. The Bundesliga remains unchanged at its minimum level ($5.6\%$), acting as a regulatory anomaly on the continent."
    
    if fig2_target in text_en and "### Trajectories of Diversity and Concentration" not in text_en:
        text_en = text_en.replace(fig2_target, fig2_repl)

    # Insert interpretation 3 after figure 3:
    fig3_target = "![Historical Configurational Trajectories of Ownership Landscapes (PCA 2019-2024)](../images/pca_trajectories.png)"
    fig3_repl = fig3_target + "\n\n### Interpretation of PCA Quadrants and Trajectories\nThe two-dimensional projection of the 30 league-season observations reveals the existence of path-dependent evolutionary paths and typifies the competitive environments:\n* **Quadrant III (Democratic and Traditional Uniclub - Bottom Left)**: The Bundesliga remains stationary in this space (PC1 $\approx -3.3$). The 50+1 rule operates as an absolute institutional stabilizer that prevents the league from moving toward financialization or trans-national multi-club ownership.\n* **Quadrant IV (Private Commercial Uniclub - Bottom Right)**: Italian Serie A and French Ligue 1 start deep in this quadrant, characterized by private owners acting as individual commercial entities. However, Serie A exhibits a clear upward trajectory ($y = -1.55$ in 2019 to $y = -0.36$ in 2024), approaching Quadrant I as foreign institutional funds and consortia displace local family owners.\n* **Quadrant I (Transnational Financial MCO - Top Right)**: Represents the most financialized and globally integrated ecosystem. The Premier League and Ligue 1 oscillate dynamically across the borders of this quadrant. The Premier League ends in 2024 at the upper limit ($y = 2.62$) due to its very high rate of multi-club ownership, consolidating a trajectory of globalized financialization with no return to the traditional model."
    
    if fig3_target in text_en and "### Interpretation of PCA Quadrants and Trajectories" not in text_en:
        text_en = text_en.replace(fig3_target, fig3_repl)

    with open(metodo_en, "w", encoding="utf-8") as f:
        f.write(text_en)
    print("Updated English methodology markdown")

# 3. Render both updated markdown files to docx using Quarto
print("Rendering Spanish Word Document...")
subprocess.run(["quarto", "render", metodo_es, "--to", "docx"], shell=True)
print("Rendering English Word Document...")
subprocess.run(["quarto", "render", metodo_en, "--to", "docx"], shell=True)
print("Finished rendering both files")
