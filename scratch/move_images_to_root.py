import os
import shutil
import re

workspace_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape"
brain_dir = r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab"

# New target paths
docs_dir = os.path.join(workspace_dir, "docs")
root_images_dir = os.path.join(workspace_dir, "images")
old_images_dir = os.path.join(docs_dir, "images")

# 1. Create root images folder
os.makedirs(root_images_dir, exist_ok=True)
print(f"Created root images directory: {root_images_dir}")

# 2. Copy PNGs from brain directory to root images folder
copied_count = 0
for f in os.listdir(brain_dir):
    if f.lower().endswith(".png"):
        src = os.path.join(brain_dir, f)
        dst = os.path.join(root_images_dir, f)
        shutil.copy2(src, dst)
        copied_count += 1
print(f"Copied {copied_count} PNGs to {root_images_dir}")

# 3. Delete old docs/images directory if it exists
if os.path.exists(old_images_dir):
    shutil.rmtree(old_images_dir)
    print(f"Deleted old images directory: {old_images_dir}")

# 4. Update image links in docs/*.md to use '../images/filename.png'
for filename in ["ownership_landscape_report.md", "metodologia_ownership_landscape.md"]:
    filepath = os.path.join(docs_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Replace image links to point to ../images/filename.png
        # The previous link format was images/filename.png
        def replacer(match):
            caption = match.group(1)
            path = match.group(2)
            fname = os.path.basename(path)
            if fname.lower().endswith(".png"):
                return f"![{caption}](../images/{fname})"
            return match.group(0)
            
        text = re.sub(r"!\[(.*?)\]\((.*?)\)", replacer, text)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Updated image links to '../images/' in {filepath}")
    else:
        print(f"File not found: {filepath}")
