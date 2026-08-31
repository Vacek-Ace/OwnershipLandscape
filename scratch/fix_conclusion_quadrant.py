import json
import os
import subprocess

gen_path = 'scratch/build_separated_trajectories_notebook.py'
with open(gen_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where Cuadrante II or Serie A is mentioned
lines = text.splitlines()
for i, l in enumerate(lines, 1):
    if 'Serie A' in l and 'Cuadrante II' in l:
        print(f"Line {i}: {l}")

old_conclusion_bullet = "*   **El Régimen en Transición Financiera (Italia y Francia, con España como puente híbrido)**: La Serie A y la Ligue 1 han experimentado una profunda transformación vertical en el PCA, transitando desde paisajes de mecenazgo familiar uniclub en el Cuadrante IV hacia ecosistemas colonizados por firmas de inversión y consorcios globales en el Cuadrante II."

new_conclusion_bullet = "*   **El Régimen en Transición Financiera (Italia y Francia, con España como puente híbrido)**: La Serie A y la Ligue 1 han experimentado una profunda transformación vertical en el PCA, ascendiendo desde la base del mecenazgo familiar uniclub en el Cuadrante IV hacia ecosistemas colonizados por firmas de inversión y consorcios globales (con la Ligue 1 cruzando plenamente al Cuadrante II y la Serie A situándose en el borde neutro superior del Cuadrante IV)."

if old_conclusion_bullet in text:
    text = text.replace(old_conclusion_bullet, new_conclusion_bullet)
    print("Replaced conclusion bullet successfully!")
else:
    print("Exact match not found, checking flexible replacement...")
    text = text.replace(
        "transitando desde paisajes de mecenazgo familiar uniclub en el Cuadrante IV hacia ecosistemas colonizados por firmas de inversión y consorcios globales en el Cuadrante II.",
        "ascendiendo desde la base del mecenazgo familiar uniclub en el Cuadrante IV hacia ecosistemas colonizados por firmas de inversión y consorcios globales (con la Ligue 1 cruzando plenamente al Cuadrante II y la Serie A situándose en el borde neutro superior del Cuadrante IV)."
    )

with open(gen_path, 'w', encoding='utf-8') as f:
    f.write(text)

subprocess.run(['python', gen_path], check=True)
subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', 'notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb'], check=True)
subprocess.run(['jupyter', 'nbconvert', '--to', 'html', 'notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb'], check=True)
print("Pipeline re-executed successfully!")
