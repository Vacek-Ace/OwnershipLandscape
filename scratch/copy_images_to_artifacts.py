import shutil
import os

artifact_dir = r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab"
images_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape\images"

for img_name in ['ownership_profiles_2024.png', 'temporal_indices.png', 'pca_trajectories.png']:
    src = os.path.join(images_dir, img_name)
    dst = os.path.join(artifact_dir, img_name)
    shutil.copy2(src, dst)
    print(f"Copied {src} -> {dst}")
