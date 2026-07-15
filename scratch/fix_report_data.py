import os
import subprocess

docs_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape\docs"
report_path = os.path.join(docs_dir, "ownership_landscape_report.md")
metodo_es = os.path.join(docs_dir, "metodologia_ownership_landscape.md")
metodo_en = os.path.join(docs_dir, "methodology_ownership_landscape.md")

# 1. Update ownership_landscape_report.md
if os.path.exists(report_path):
    with open(report_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    orig = text
    
    # Correct table lines
    old_laliga_2019 = "| **LaLiga** | 2019 | 20 | 1.735 | 0.185 | 25.0% | 5.0% | domestic private (30.0%) |"
    new_laliga_2019 = "| **LaLiga** | 2019 | 20 | 1.735 | 0.185 | 25.0% | 0.0% | `hybrid` (25.0%) |"
    
    old_laliga_2024 = "| | 2024 | 20 | **1.848** | **0.170** | 25.0% | 5.0% | domestic private (25.0%) |"
    new_laliga_2024 = "| | 2024 | 20 | **1.848** | **0.170** | 25.0% | 5.0% | `domestic private` (25.0%) |"
    
    old_ligue_2019 = "| **Ligue 1** | 2019 | 20 | 1.539 | 0.250 | 25.0% | 5.0% | domestic private (40.0%) |"
    new_ligue_2019 = "| **Ligue 1** | 2019 | 20 | 1.539 | **0.270** | 25.0% | 5.0% | `domestic private` (45.0%) |"
    
    old_ligue_2024 = "| | 2024 | 18 | **1.426** | **0.272** | 27.8% | 5.6% | domestic private (38.9%) |"
    new_ligue_2024 = "| | 2024 | 18 | **1.426** | **0.272** | 27.8% | 5.6% | `domestic private` (38.9%) |"
    
    old_premier_2019 = "| **Premier League** | 2019 | 20 | 1.713 | 0.190 | 60.0% | 10.0% | corporate-MCO / foreign private (25.0%) |"
    new_premier_2019 = "| **Premier League** | 2019 | 20 | 1.713 | **0.195** | **70.0%** | 10.0% | `corporate-MCO` (30.0%) |"
    
    old_premier_2024 = "| | 2024 | 20 | **1.730** | **0.190** | **65.0%** | **10.0%** | corporate-MCO (30.0%) |"
    new_premier_2024 = "| | 2024 | 20 | **1.730** | **0.190** | **65.0%** | **10.0%** | `corporate-MCO` (30.0%) |"
    
    old_seriea_2019 = "| **Serie A** | 2019 | 20 | 1.484 | 0.270 | 25.0% | 0.0% | domestic private (45.0%) |"
    new_seriea_2019 = "| **Serie A** | 2019 | 20 | 1.484 | 0.270 | 25.0% | 0.0% | `domestic private` (40.0%) |"
    
    old_seriea_2024 = "| | 2024 | 20 | **1.431** | **0.265** | 30.0% | 0.0% | domestic private (35.0%) |"
    new_seriea_2024 = "| | 2024 | 20 | **1.431** | **0.265** | 30.0% | 0.0% | `domestic private` (35.0%) |"
    
    old_bundes_2019 = "| **Bundesliga** | 2019 | 18 | 1.242 | 0.414 | 5.6% | 5.6% | member-owned (61.1%) |"
    new_bundes_2019 = "| **Bundesliga** | 2019 | 18 | 1.242 | 0.414 | 5.6% | 5.6% | `member-owned` (61.1%) |"
    
    old_bundes_2024 = "| | 2024 | 18 | **1.051** | **0.481** | 5.6% | 5.6% | member-owned (66.7%) |"
    new_bundes_2024 = "| | 2024 | 18 | **1.051** | **0.481** | 5.6% | 5.6% | `member-owned` (66.7%) |"
    
    replacements = {
        old_laliga_2019: new_laliga_2019,
        old_laliga_2024: new_laliga_2024,
        old_ligue_2019: new_ligue_2019,
        old_ligue_2024: new_ligue_2024,
        old_premier_2019: new_premier_2019,
        old_premier_2024: new_premier_2024,
        old_seriea_2019: new_seriea_2019,
        old_seriea_2024: new_seriea_2024,
        old_bundes_2019: new_bundes_2019,
        old_bundes_2024: new_bundes_2024,
        "liderado por la Premier League (que crece del 60% al 65%)": "liderado por la Premier League (que oscila entre el 60% y el 70%, cerrando en el 65% en 2024)",
        "el modelo domestic private cayó del 45% al 35%": "el modelo domestic private cayó del 40% al 35%"
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
        
    if text != orig:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully corrected data and table in ownership_landscape_report.md")
    else:
        print("No changes made to ownership_landscape_report.md")

# 2. Update methodology files
if os.path.exists(metodo_es):
    with open(metodo_es, "r", encoding="utf-8") as f:
        text = f.read()
    orig = text
    text = text.replace(
        "Crece del 60% al 65% en la Premier League",
        "se mantiene en un nivel muy elevado (entre el 60% y el 70%) en la Premier League, cerrando en el 65% en 2024"
    )
    if text != orig:
        with open(metodo_es, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully corrected narrative in metodologia_ownership_landscape.md")

if os.path.exists(metodo_en):
    with open(metodo_en, "r", encoding="utf-8") as f:
        text = f.read()
    orig = text
    text = text.replace(
        "It grows from 60% to 65% in the Premier League",
        "remains at a very high level (between 60% and 70%) in the Premier League, ending at 65% in 2024"
    )
    if text != orig:
        with open(metodo_en, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully corrected narrative in methodology_ownership_landscape.md")

# 3. Render methodology files to Word
print("Re-rendering Spanish Word Document...")
subprocess.run(["quarto", "render", metodo_es, "--to", "docx"], shell=True)
print("Re-rendering English Word Document...")
subprocess.run(["quarto", "render", metodo_en, "--to", "docx"], shell=True)
print("Finished rendering both files")
