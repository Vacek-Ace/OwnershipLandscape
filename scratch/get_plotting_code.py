import os

out_path = r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\scratch\search_seasons_output.txt"
paths = [
    r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\ownership_landscape_report.md",
    r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\metodologia_ownership_landscape.md"
]

output = []
for p in paths:
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            text = f.read()
        lines = text.splitlines()
        for i, l in enumerate(lines, 1):
            if "temporada" in l.lower() or "2019" in l or "2024" in l:
                output.append(f"{os.path.basename(p)}:L{i}: {l}")
    else:
        output.append(f"File not found: {p}")

with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(output))
print("Successfully searched files and saved results")
