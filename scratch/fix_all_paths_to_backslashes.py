import os
import re

paths = [
    r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\ownership_landscape_report.md",
    r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\metodologia_ownership_landscape.md"
]

artifact_dir = r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab"

for p in paths:
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            text = f.read()
        
        orig = text
        # Replace any image pattern ![caption](filename.png) or ![caption](/filename.png) or similar
        # with ![caption](/C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\filename.png)
        # Note: the regex matches !\[(.*?)\]\((.*?)\)
        def replacer(match):
            caption = match.group(1)
            path = match.group(2)
            # Get the basename
            filename = os.path.basename(path)
            # Ensure it is a png file
            if filename.lower().endswith(".png"):
                new_path = "/" + os.path.join(artifact_dir, filename)
                return f"![{caption}]({new_path})"
            return match.group(0)
            
        text = re.sub(r"!\[(.*?)\]\((.*?)\)", replacer, text)
        
        if text != orig:
            with open(p, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Successfully fixed image paths in {os.path.basename(p)}")
        else:
            print(f"No changes made to {os.path.basename(p)}")
    else:
        print(f"File not found: {p}")
