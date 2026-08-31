import json

nb = json.load(open('notebooks/Analisis_Ownership_Landscape_Dinamico.ipynb', encoding='utf-8'))

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        content = "".join(cell['source'])
        if 'Trayectorias' in content or 'Cuadrante' in content or 'Conclusiones' in content:
            print(f"\n=================== CELL {i} ===================")
            print(content)
