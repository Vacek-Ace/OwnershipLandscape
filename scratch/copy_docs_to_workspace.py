import os
import shutil
import re

# Source paths
brain_dir = r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab"
report_src = os.path.join(brain_dir, "ownership_landscape_report.md")
metodo_src = os.path.join(brain_dir, "metodologia_ownership_landscape.md")

# Target paths
workspace_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape"
docs_dir = os.path.join(workspace_dir, "docs")
images_dir = os.path.join(docs_dir, "images")

# 1. Create directories
os.makedirs(docs_dir, exist_ok=True)
os.makedirs(images_dir, exist_ok=True)
print(f"Created directories: {docs_dir} and {images_dir}")

# 2. Copy all PNG files
copied_images = []
for f in os.listdir(brain_dir):
    if f.lower().endswith(".png"):
        src_file = os.path.join(brain_dir, f)
        dst_file = os.path.join(images_dir, f)
        shutil.copy2(src_file, dst_file)
        copied_images.append(f)
print(f"Copied {len(copied_images)} PNG images to {images_dir}")

# 3. Copy and update markdown files
for src_path, filename in [(report_src, "ownership_landscape_report.md"), (metodo_src, "metodologia_ownership_landscape.md")]:
    if os.path.exists(src_path):
        dst_path = os.path.join(docs_dir, filename)
        with open(src_path, "r", encoding="utf-8") as f:
            text = f.read()
        
        # Replace image links to point to images/filename.png
        # The pattern is ![caption](/filename.png) or ![caption](filename.png)
        # Regex to find ![caption](path/filename.png) or ![caption](/filename.png) or ![caption](filename.png)
        def replacer(match):
            caption = match.group(1)
            path = match.group(2)
            fname = os.path.basename(path)
            if fname.lower().endswith(".png"):
                return f"![{caption}](images/{fname})"
            return match.group(0)
            
        text = re.sub(r"!\[(.*?)\]\((.*?)\)", replacer, text)
        
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Copied and updated {filename} to {dst_path}")
    else:
        print(f"Source file not found: {src_path}")
