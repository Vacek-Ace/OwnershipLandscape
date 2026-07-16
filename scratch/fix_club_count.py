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
    text = text.replace("* **176 clubes únicos**.", "* **137 clubes únicos**.")
    if text != orig:
        with open(metodo_es, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully corrected unique club count in Spanish methodology!")

# 2. Update English Methodology
if os.path.exists(metodo_en):
    with open(metodo_en, "r", encoding="utf-8") as f:
        text = f.read()
    orig = text
    text = text.replace("* **176 unique clubs**.", "* **137 unique clubs**.")
    if text != orig:
        with open(metodo_en, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully corrected unique club count in English methodology!")

# 3. Render methodology files to Word
print("Re-rendering Spanish Word Document...")
subprocess.run(["quarto", "render", metodo_es, "--to", "docx"], shell=True)
print("Re-rendering English Word Document...")
subprocess.run(["quarto", "render", metodo_en, "--to", "docx"], shell=True)
print("Finished rendering both files")
