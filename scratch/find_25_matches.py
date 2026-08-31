import os

matches = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith(('.md', '.py', '.ipynb', '.html', '.docx')):
            path = os.path.join(root, f)
            try:
                content = open(path, encoding='utf-8', errors='ignore').read()
                if '25%' in content:
                    for i, l in enumerate(content.splitlines(), 1):
                        if '25%' in l and ('superan' in l or 'redes' in l or 'mco' in l.lower() or 'conclusiones' in l.lower()):
                            matches.append(f"{path} : {i} : {l}")
            except Exception as e:
                pass

with open('scratch/search_25_matches.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(matches))

print(f"Found {len(matches)} matches, written to scratch/search_25_matches.txt")
