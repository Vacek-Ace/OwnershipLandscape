import json
import os
import subprocess

# 1. Update generator script
gen_path = 'scratch/generate_detailed_notebook.py'
with open(gen_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = "que ya superan el $25\\%$ en 4 de las 5 grandes ligas y alcanzan el $60\\%$ en Inglaterra"
replacement = "que ya alcanzan o superan el $25\\%$ en 4 de las 5 grandes ligas (todas salvo la Bundesliga) y llegan al $60\\%$ en Inglaterra"

if target in text:
    text = text.replace(target, replacement)
    with open(gen_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated generate_detailed_notebook.py!")
else:
    print("Target phrase not found in exact form, checking alternative...")
    text = text.replace("superan el $25", "alcanzan o superan el $25")
    with open(gen_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated with fallback!")

# 2. Run generator script
subprocess.run(['python', gen_path], check=True)
print("Regenerated Analisis_Ownership_Landscape_Dinamico.ipynb")

# 3. Execute notebook inplace
subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', 'notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb'], check=True)
print("Executed notebook successfully")

# 4. Export to HTML
subprocess.run(['jupyter', 'nbconvert', '--to', 'html', 'notebooks/Analisis_Ownership_Landscape_Dinamico.html'], check=False)
subprocess.run(['jupyter', 'nbconvert', '--to', 'html', 'notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb'], check=True)
print("Exported to HTML successfully")
