with open('scratch/build_separated_trajectories_notebook.py', 'r', encoding='utf-8') as f:
    code = f.read()

target = "| **LaLiga** | $(+0.740, +0.271)$ | $(+1.136, +0.368)$ | $(+0.409, -0.058)$ | $(+0.564, +0.047)$ | $(+0.762, +0.163)$ | **$(+0.487, +0.471)$** | **Cuadrante I $\\to$ Cuadrante I** |"
replacement = "| **LaLiga** | $(+0.740, +0.271)$ | $(+1.136, +0.368)$ | $(+0.409, -0.058)$ | $(+0.564, +0.047)$ | $(+0.762, +0.163)$ | **$(+0.487, +0.471)$** | **Cuadrante I (incursión en III en 2021) $\\to$ Cuadrante I** |"

if target in code:
    code = code.replace(target, replacement)
    with open('scratch/build_separated_trajectories_notebook.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Direct replacement successful in build_separated_trajectories_notebook.py!")
else:
    print("Target not found directly, searching flexible pattern...")
    code = code.replace("Cuadrante I $\\to$ Cuadrante I", "Cuadrante I (incursión en III en 2021) $\\to$ Cuadrante I")
    with open('scratch/build_separated_trajectories_notebook.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Flexible replacement done!")

import subprocess
subprocess.run(['python', 'scratch/build_separated_trajectories_notebook.py'], check=True)
subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', '--inplace', 'notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb'], check=True)
subprocess.run(['jupyter', 'nbconvert', '--to', 'html', 'notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb'], check=True)
print("Complete pipeline finished successfully!")
