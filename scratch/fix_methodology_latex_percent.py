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
    text = text.replace(
        "Crece del $60\\%$ al $65\\%$ en la Premier League",
        "oscila en niveles muy altos (entre el $60\\%$ y el $70\\%$) en la Premier League, cerrando en el $65\\%$ en 2024"
    )
    if text != orig:
        with open(metodo_es, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully corrected Spanish methodology markdown text!")
    else:
        print("Failed to replace Spanish methodology markdown text!")

# 2. Update English Methodology
if os.path.exists(metodo_en):
    with open(metodo_en, "r", encoding="utf-8") as f:
        text = f.read()
    orig = text
    text = text.replace(
        "It grows from $60\\%$ to $65\\%$ in the Premier League",
        "fluctuates at high levels (between $60\\%$ and $70\\%$) in the Premier League, ending at $65\\%$ in 2024"
    )
    if text != orig:
        with open(metodo_en, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully corrected English methodology markdown text!")
    else:
        print("Failed to replace English methodology markdown text!")

# 3. Render methodology files to Word
print("Re-rendering Spanish Word Document...")
subprocess.run(["quarto", "render", metodo_es, "--to", "docx"], shell=True)
print("Re-rendering English Word Document...")
subprocess.run(["quarto", "render", metodo_en, "--to", "docx"], shell=True)
print("Finished rendering both files")
