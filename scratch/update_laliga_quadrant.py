import json
import os
import subprocess

gen_path = 'scratch/build_separated_trajectories_notebook.py'
with open(gen_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace LaLiga quadrant progression in table and text
old_table_str = "**Cuadrante I $\\to$ Cuadrante I**"
new_table_str = "**Cuadrante I (incursión en III en 2021) $\\to$ Cuadrante I**"

text = text.replace(old_table_str, new_table_str)

with open(gen_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated build_separated_trajectories_notebook.py!")

# Execute generator
subprocess.run(['python', gen_path], check=True)
print("Regenerated notebook JSON!")

# Execute notebook inplace
subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', 'notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb'], check=True)
print("Executed notebook successfully!")

# Export to HTML
subprocess.run(['jupyter', 'nbconvert', '--to', 'html', 'notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb'], check=True)
print("Exported to HTML successfully!")
