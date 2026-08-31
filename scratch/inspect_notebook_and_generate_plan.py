import json

nb_path = 'notebooks/Analisis_Ownership_Landscape.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

lines = []
lines.append(f"Total cells in notebook: {len(nb['cells'])}")
lines.append("\n=== OUTLINE OF NOTEBOOK CELLS ===")
for i, cell in enumerate(nb['cells']):
    ctype = cell['cell_type']
    src = "".join(cell['source'])
    first_line = src.split('\n')[0] if src else ""
    if ctype == 'markdown':
        if '#' in first_line:
            lines.append(f"Cell {i} [MD]: {first_line}")
    elif ctype == 'code':
        if any(kw in src.lower() for kw in ['pca', 'entropy', 'hhi', 'read_csv', 'to_csv', 'plot', 'figure', 'model', 'shap', 'rf', 'ols']):
            lines.append(f"Cell {i} [CODE]: {first_line[:80]}...")

with open('scratch/nb_outline.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Notebook outline written to scratch/nb_outline.txt")
