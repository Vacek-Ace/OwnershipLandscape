import os
import subprocess

docs_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape\docs"
metodo_es = os.path.join(docs_dir, "metodologia_ownership_landscape.md")
metodo_en = os.path.join(docs_dir, "methodology_ownership_landscape.md")

paths = [metodo_es, metodo_en]

for p in paths:
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            text = f.read()
        
        orig = text
        # Replace the incorrectly escaped bell character + 'pprox' with '\approx'
        # \x07 is the ASCII bell character from '\approx' escaping
        text = text.replace("\x07pprox", r"\approx")
        
        if text != orig:
            with open(p, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Fixed LaTeX math escaping in {os.path.basename(p)}")
        else:
            print(f"No escaping issues found in {os.path.basename(p)}")

# Re-render files
print("Re-rendering Spanish Word Document...")
subprocess.run(["quarto", "render", metodo_es, "--to", "docx"], shell=True)
print("Re-rendering English Word Document...")
subprocess.run(["quarto", "render", metodo_en, "--to", "docx"], shell=True)
print("Finished re-rendering both files")
