import json
import os
import subprocess

gen_path = 'scratch/build_separated_trajectories_notebook.py'
with open(gen_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    "| **LaLiga** | $(+0.740, +0.271)$ | $(+1.136, +0.368)$ | $(+0.409, -0.058)$ | $(+0.564, +0.047)$ | $(+0.762, +0.163)$ | **$(+0.487, +0.471)$** | **Cuadrante I \\to Cuadrante I** |",
    "| **LaLiga** | $(+0.740, +0.271)$ | $(+1.136, +0.368)$ | $(+0.409, -0.058)$ | $(+0.564, +0.047)$ | $(+0.762, +0.163)$ | **$(+0.487, +0.471)$** | **Cuadrante I (incursión en III en 2021) \\to Cuadrante I** |"
)

with open(gen_path, 'w', encoding='utf-8') as f:
    f.write(text)

subprocess.run(['python', gen_path], check=True)
subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', 'notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb'], check=True)
subprocess.run(['jupyter', 'nbconvert', '--to', 'html', 'notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb'], check=True)
print("Updated and verified!")
