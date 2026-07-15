import os
import subprocess

docs_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape\docs"
metodo_es = os.path.join(docs_dir, "metodologia_ownership_landscape.md")
metodo_en = os.path.join(docs_dir, "methodology_ownership_landscape.md")
notas_path = os.path.join(docs_dir, "notas_bibliograficas.md")

# 1. Update Spanish Methodology
if os.path.exists(metodo_es):
    with open(metodo_es, "r", encoding="utf-8") as f:
        text = f.read()
    orig = text
    text = text.replace(
        "La correlación de rango de Spearman para el primer componente principal (PC1, el Eje de Internacionalización y Financiarización) superó el **$0.96$** en valor absoluto.",
        "La correlación de Pearson para el primer componente principal (PC1, el Eje de Internacionalización y Financiarización) entre ambos enfoques superó el **$0.96$** en valor absoluto (con una correlación de rango de Spearman de **$0.88$**)."
    )
    if text != orig:
        with open(metodo_es, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully corrected correlation terms in Spanish methodology!")

# 2. Update English Methodology
if os.path.exists(metodo_en):
    with open(metodo_en, "r", encoding="utf-8") as f:
        text = f.read()
    orig = text
    text = text.replace(
        "The Spearman rank correlation for the first principal component (PC1, the Internationalization and Financialization Axis) exceeded **$0.96$** in absolute value.",
        "The Pearson correlation for the first principal component (PC1, the Internationalization and Financialization Axis) between both approaches exceeded **$0.96$** in absolute value (with a Spearman rank correlation of **$0.88$**)."
    )
    if text != orig:
        with open(metodo_en, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully corrected correlation terms in English methodology!")

# 3. Update Notas Bibliográficas
if os.path.exists(notas_path):
    with open(notas_path, "r", encoding="utf-8") as f:
        text = f.read()
    orig = text
    text = text.replace(
        "Spearman PC1 > 0.96",
        "Pearson PC1 > 0.96, Spearman > 0.88"
    )
    if text != orig:
        with open(notas_path, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully corrected correlation terms in notas_bibliograficas.md!")

# 4. Render methodology files to Word
print("Re-rendering Spanish Word Document...")
subprocess.run(["quarto", "render", metodo_es, "--to", "docx"], shell=True)
print("Re-rendering English Word Document...")
subprocess.run(["quarto", "render", metodo_en, "--to", "docx"], shell=True)
print("Finished rendering both files")
