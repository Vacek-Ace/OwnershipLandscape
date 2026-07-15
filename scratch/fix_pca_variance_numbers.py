import os

report_path = r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\ownership_landscape_report.md"
metodologia_path = r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\metodologia_ownership_landscape.md"

# 1. Update report
if os.path.exists(report_path):
    with open(report_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    orig = text
    text = text.replace(
        "que explican conjuntamente el **67.7%** de la varianza total de los datos de la liga (PC1 explica el 42.6% y PC2 el 25.1%):",
        "que explican conjuntamente el **72.5%** de la varianza total de los datos de la liga (PC1 explica el 48.0% y PC2 el 24.5%):"
    )
    if text != orig:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully updated ownership_landscape_report.md with actual PCA percentages")
    else:
        print("No changes made to ownership_landscape_report.md")

# 2. Update methodology
if os.path.exists(metodologia_path):
    with open(metodologia_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    orig = text
    text = text.replace(
        "explicar conjuntamente el **$67.7\\%$** de la varianza acumulada de la estructura de propiedad.",
        "explicar conjuntamente el **$72.5\\%$** de la varianza acumulada de la estructura de propiedad."
    )
    text = text.replace(
        "* **PC1 ($42.6\\%$ de varianza)**:",
        "* **PC1 ($48.0\\%$ de varianza)**:"
    )
    text = text.replace(
        "* **PC2 ($25.1\\%$ de varianza)**:",
        "* **PC2 ($24.5\\%$ de varianza)**:"
    )
    if text != orig:
        with open(metodologia_path, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully updated metodologia_ownership_landscape.md with actual PCA percentages")
    else:
        print("No changes made to metodologia_ownership_landscape.md")
