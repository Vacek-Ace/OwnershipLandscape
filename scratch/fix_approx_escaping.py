import os

# 1. Fix generate_verbose_notebook.py
notebook_gen_path = r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\scratch\generate_verbose_notebook.py"
if os.path.exists(notebook_gen_path):
    with open(notebook_gen_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # We want to replace any single backslash \approx with double backslash \\approx in the python string literals
    # Let's inspect where it occurs and replace it
    # We replace "$\approx" with "$\\approx", "$x \approx" with "$x \\approx", "$y \approx" with "$y \\approx"
    orig_text = text
    text = text.replace(r"$\approx", r"$\\approx")
    text = text.replace(r"$x \approx", r"$x \\approx")
    text = text.replace(r"$y \approx", r"$y \\approx")
    
    if text != orig_text:
        with open(notebook_gen_path, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully fixed generate_verbose_notebook.py")
    else:
        print("No changes needed in generate_verbose_notebook.py")
else:
    print("generate_verbose_notebook.py not found")

# 2. Fix ownership_landscape_report.md
report_path = r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\ownership_landscape_report.md"
if os.path.exists(report_path):
    with open(report_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Replace corrupted $ pprox or similar with $\approx$
    # Let's see: the search showed "Entropía $ pprox 1.05$" or similar. Let's do a case-insensitive replacement of "pprox" or " pprox" or "\x07pprox"
    orig_text = text
    # Let's clean up any "\x07pprox", "pprox", or " pprox" following a "$" sign
    text = text.replace("$ pprox", r"$\approx$")
    text = text.replace("$\x07pprox", r"$\approx$")
    text = text.replace("$pprox", r"$\approx$")
    
    if text != orig_text:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully fixed ownership_landscape_report.md")
    else:
        print("No changes made in ownership_landscape_report.md")
else:
    print("ownership_landscape_report.md not found")
