import os

docs_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape\docs"
metodo_path = os.path.join(docs_dir, "metodologia_ownership_landscape.md")
notas_path = os.path.join(docs_dir, "notas_bibliograficas.md")

paths = [metodo_path, notas_path]

for p in paths:
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            text = f.read()
        
        orig = text
        # Replace the UEFA citation line
        text = text.replace(
            "UEFA. (2024). *The European Club Finance and Investment Landscape Report*. UEFA.",
            "UEFA. (2024). *The European Club Finance and Investment Landscape Report*. UEFA. https://ecfil.uefa.com/2024"
        )
        # Also handle potential trailing space differences
        text = text.replace(
            "UEFA. (2024). *The European Club Finance and Investment Landscape Report*. UEFA. ",
            "UEFA. (2024). *The European Club Finance and Investment Landscape Report*. UEFA. https://ecfil.uefa.com/2024"
        )
        
        if text != orig:
            with open(p, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Successfully added UEFA URL to {os.path.basename(p)}")
        else:
            print(f"No changes made to {os.path.basename(p)}")
    else:
        print(f"File not found: {p}")
