import os

paths = [
    r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\ownership_landscape_report.md",
    r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\metodologia_ownership_landscape.md"
]

target_prefix = "/C:/Users/vacek/.gemini/antigravity/brain/c7bab6f5-8c0e-48bf-8b50-88f1597357ab/"

for p in paths:
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            text = f.read()
        
        orig = text
        # Let's replace any variants of the absolute path in ![caption](path)
        # 1. file:///C:/Users/vacek/.gemini/antigravity/brain/c7bab6f5-8c0e-48bf-8b50-88f1597357ab/
        text = text.replace("file:///C:/Users/vacek/.gemini/antigravity/brain/c7bab6f5-8c0e-48bf-8b50-88f1597357ab/", target_prefix)
        # 2. C:/Users/vacek/.gemini/antigravity/brain/c7bab6f5-8c0e-48bf-8b50-88f1597357ab/ (but avoid double slashes if it already started with a slash)
        # We can look for occurrences of (C:/Users/vacek/...) and replace with (/C:/Users/vacek/...)
        text = text.replace("(C:/Users/vacek/.gemini/antigravity/brain/c7bab6f5-8c0e-48bf-8b50-88f1597357ab/", "(/" + "C:/Users/vacek/.gemini/antigravity/brain/c7bab6f5-8c0e-48bf-8b50-88f1597357ab/")
        # Remove any double slashes that might have been created, like (//C:/...)
        text = text.replace("(//C:/Users/vacek/", "(/C:/Users/vacek/")
        
        if text != orig:
            with open(p, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Successfully updated image paths in {os.path.basename(p)}")
        else:
            print(f"No path updates needed in {os.path.basename(p)}")
    else:
        print(f"File not found: {p}")
