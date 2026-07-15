import os
import subprocess

docs_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape\docs"
metodo_es = os.path.join(docs_dir, "metodologia_ownership_landscape.md")
metodo_en = os.path.join(docs_dir, "methodology_ownership_landscape.md")

# 1. Update Spanish Methodology
if os.path.exists(metodo_es):
    with open(metodo_es, "r", encoding="utf-8") as f:
        text = f.read()
    orig = text
    
    q1_target = "* **Cuadrante I (Financiarización Transnacional MCO - Arriba a la Derecha)**: Representa el ecosistema más financiarizado e integrado en redes globales. La Premier League y la Ligue 1 oscilan dinámicamente cruzando las fronteras de este cuadrante. La Premier League termina en 2024 en el límite superior ($y = 2.62$) por su altísima tasa de multipropiedad, consolidando una trayectoria de financiarización globalizada sin retorno al modelo tradicional."
    
    q2_text = "\n* **Cuadrante II (Híbrido / Colectivo con Redes - Arriba a la Izquierda)**: Representa paisajes de propiedad que conservan una fuerte base de control social o democrático local (valores negativos de PC1) pero que incorporan lógicas corporativas superiores, participación híbrida o una penetración moderada de redes de multipropiedad (valores positivos de PC2). LaLiga española (debido a su fuerte presencia de clubes híbridos y de socios, combinada con compras controladas de MCO como el Girona) y la Premier League en sus años de menor financiarización extrema se ubican en este cuadrante."
    
    if q1_target in text and "Cuadrante II" not in text:
        text = text.replace(q1_target, q1_target + q2_text)
        with open(metodo_es, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully added Cuadrante II to Spanish methodology!")

# 2. Update English Methodology
if os.path.exists(metodo_en):
    with open(metodo_en, "r", encoding="utf-8") as f:
        text = f.read()
    orig = text
    
    q1_target_en = "* **Quadrant I (Transnational Financial MCO - Top Right)**: Represents the most financialized and globally integrated ecosystem. The Premier League and Ligue 1 oscillate dynamically across the borders of this quadrant. The Premier League ends in 2024 at the upper limit ($y = 2.62$) due to its very high rate of multi-club ownership, consolidating a trajectory of globalized financialization with no return to the traditional model."
    
    q2_text_en = "\n* **Quadrant II (Hybrid / Collective with Networks - Top Left)**: Represents ownership landscapes that preserve a strong baseline of local social or democratic control (negative PC1 values) but incorporate higher corporate logics, hybrid participation, or moderate penetration of multi-club networks (positive PC2 values). Spanish LaLiga (due to its strong presence of hybrid and member-owned clubs, combined with controlled MCO acquisitions like Girona) and the Premier League in its years of less extreme financialization are positioned in this quadrant."
    
    if q1_target_en in text and "Quadrant II" not in text:
        text = text.replace(q1_target_en, q1_target_en + q2_text_en)
        with open(metodo_en, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully added Quadrant II to English methodology!")

# 3. Render both updated files
print("Re-rendering Spanish Word Document...")
subprocess.run(["quarto", "render", metodo_es, "--to", "docx"], shell=True)
print("Re-rendering English Word Document...")
subprocess.run(["quarto", "render", metodo_en, "--to", "docx"], shell=True)
print("Finished rendering both files")
