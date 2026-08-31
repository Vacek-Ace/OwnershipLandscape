import json

nb_path = 'notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        outputs = cell.get('outputs', [])
        img_count = sum(1 for out in outputs if 'image/png' in out.get('data', {}))
        print(f"Cell {i} outputs count: {len(outputs)}, PNG images: {img_count}")
