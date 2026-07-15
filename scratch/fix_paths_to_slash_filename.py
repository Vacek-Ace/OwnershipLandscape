import os
import re

paths = [
    r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\ownership_landscape_report.md",
    r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\metodologia_ownership_landscape.md"
]

for p in paths:
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            text = f.read()
        
        orig = text
        # Regex to match ![caption](path/filename.png) or ![caption](/C:\path\filename.png)
        # and replace the path with /filename.png
        def replacer(match):
            caption = match.group(1)
            path = match.group(2)
            filename = os.path.basename(path)
            # Ensure it starts with /
            return f"![{caption}](/{filename})"
            
        text = re.sub(r"!\[(.*?)\]\((.*?)\)", replacer, text)
        
        if text != orig:
            with open(p, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Successfully updated image paths in {os.path.basename(p)}")
        else:
            print(f"No changes made to {os.path.basename(p)}")
    else:
        print(f"File not found: {p}")
