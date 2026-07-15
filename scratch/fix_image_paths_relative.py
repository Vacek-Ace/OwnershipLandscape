import os

p = r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\metodologia_ownership_landscape.md"
if os.path.exists(p):
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    
    orig = text
    # Replace relative paths with '/C:\\Users\\vacek\\.gemini\\antigravity\\brain\\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\\filename.png'
    text = text.replace("(ownership_profiles_2024.png)", r"(/C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\ownership_profiles_2024.png)")
    text = text.replace("(temporal_indices.png)", r"(/C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\temporal_indices.png)")
    text = text.replace("(pca_trajectories.png)", r"(/C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\pca_trajectories.png)")
    
    if text != orig:
        with open(p, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully updated image paths in methodology to backslashes format")
    else:
        print("No changes made to methodology")
else:
    print("Methodology file not found")
