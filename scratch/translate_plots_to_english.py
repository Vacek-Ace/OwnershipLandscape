import os

path = r"C:\Users\vacek\.gemini\antigravity\brain\c7bab6f5-8c0e-48bf-8b50-88f1597357ab\scratch\generate_verbose_notebook.py"
if not os.path.exists(path):
    print("Error: File not found")
    exit()

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    # 1. Bar chart: ownership_profiles_2024.png
    'plt.title("Estructura Configuracional del Ownership Landscape por Liga (Temporada 2024)", fontsize=14)':
    'plt.title("Configurational Structure of the Ownership Landscape by League (2024 Season)", fontsize=14)',
    
    'plt.xlabel("Proporción de Clubes Activos en Primera División", fontsize=12)':
    'plt.xlabel("Proportion of Active Clubs in First Division", fontsize=12)',
    
    'plt.ylabel("Liga", fontsize=12)':
    'plt.ylabel("League", fontsize=12)',
    
    'plt.legend(bbox_to_anchor=(1.05, 1), loc=\'upper left\', title="Modelos de Propiedad", fontsize=11)':
    'plt.legend(bbox_to_anchor=(1.05, 1), loc=\'upper left\', title="Ownership Models", fontsize=11)',
    
    # 2. Line plot: temporal_indices.png
    'axes[0].set_title("Evolución de la Diversidad de Propiedad\\\\n(Entropía de Shannon)", fontsize=13, weight=\'bold\')':
    'axes[0].set_title("Evolution of Ownership Diversity\\\\n(Shannon Entropy)", fontsize=13, weight=\'bold\')',
    
    'axes[0].set_xlabel("Temporada", fontsize=11)':
    'axes[0].set_xlabel("Season", fontsize=11)',
    
    'axes[0].set_ylabel("Entropía de Shannon ($H$)", fontsize=11)':
    'axes[0].set_ylabel("Shannon Entropy ($H$)", fontsize=11)',
    
    'axes[1].set_title("Evolución de la Concentración de Propiedad\\\\n(Índice Herfindahl-Hirschman - HHI)", fontsize=13, weight=\'bold\')':
    'axes[1].set_title("Evolution of Ownership Concentration\\\\n(Herfindahl-Hirschman Index - HHI)", fontsize=13, weight=\'bold\')',
    
    'axes[1].set_xlabel("Temporada", fontsize=11)':
    'axes[1].set_xlabel("Season", fontsize=11)',
    
    'axes[1].set_ylabel("Índice HHI", fontsize=11)':
    'axes[1].set_ylabel("HHI Index", fontsize=11)',
    
    'axes[2].set_title("Evolución de la Penetración de\\\\nMultipropiedad (Tasa MCO de la Liga)", fontsize=13, weight=\'bold\')':
    'axes[2].set_title("Evolution of Multi-Club Ownership (MCO) Penetration\\\\n(League MCO Rate)", fontsize=13, weight=\'bold\')',
    
    'axes[2].set_xlabel("Temporada", fontsize=11)':
    'axes[2].set_xlabel("Season", fontsize=11)',
    
    'axes[2].set_ylabel("Proporción de Clubes en MCO", fontsize=11)':
    'axes[2].set_ylabel("Proportion of Clubs under MCO", fontsize=11)',
    
    'plt.legend(bbox_to_anchor=(1.05, 1), loc=\'upper left\', title="Ligas", fontsize=11)':
    'plt.legend(bbox_to_anchor=(1.05, 1), loc=\'upper left\', title="Leagues", fontsize=11)',
    
    # 3. PCA trajectories: pca_trajectories.png
    'plt.text(-3.2, 2.7, "CUADRANTE II\\\\nControl Social/Híbrido\\\\ny Redes Transnacionales\\\\n(PC1 < 0, PC2 > 0)"':
    'plt.text(-3.2, 2.7, "QUADRANT II\\\\nSocial/Hybrid Control\\\\n& Transnational Networks\\\\n(PC1 < 0, PC2 > 0)"',
    
    'plt.text(0.6, 2.7, "CUADRANTE I\\\\nFinanciarización Global y MCO\\\\n(PC1 > 0, PC2 > 0)"':
    'plt.text(0.6, 2.7, "QUADRANT I\\\\nGlobal Financialization & MCO\\\\n(PC1 > 0, PC2 > 0)"',
    
    'plt.text(-3.2, -1.8, "CUADRANTE III\\\\nDemocrático Tradicional e Indep.\\\\n(PC1 < 0, PC2 < 0)"':
    'plt.text(-3.2, -1.8, "QUADRANT III\\\\nTraditional Democratic & Indep.\\\\n(PC1 < 0, PC2 < 0)"',
    
    'plt.text(0.6, -1.8, "CUADRANTE IV\\\\nPrivatización Comercial Uniclub\\\\n(PC1 > 0, PC2 > 0)"':
    'plt.text(0.6, -1.8, "QUADRANT IV\\nCommercial Privatization Uniclub\\\\n(PC1 > 0, PC2 > 0)"',
    
    'plt.title("Trayectorias Históricas Configuracionales de los Ownership Landscapes (PCA 2019-2024)", fontsize=14)':
    'plt.title("Historical Configurational Trajectories of Ownership Landscapes (PCA 2019-2024)", fontsize=14)',
    
    'plt.xlabel(f"Componente Principal 1 ({pca.explained_variance_ratio_[0]*100:.1f}%) - Eje de Internacionalización y Multipropiedad (MCO)")':
    'plt.xlabel(f"Principal Component 1 ({pca.explained_variance_ratio_[0]*100:.1f}%) - Axis of Internationalization and Multi-Club Ownership (MCO)")',
    
    'plt.ylabel(f"Componente Principal 2 ({pca.explained_variance_ratio_[1]*100:.1f}%) - Eje de Propiedad Tradicional vs. Financiarizada")':
    'plt.ylabel(f"Principal Component 2 ({pca.explained_variance_ratio_[1]*100:.1f}%) - Axis of Traditional vs. Financialized Ownership")',
}

orig_text = text
for target, replacement in replacements.items():
    if target in text:
        text = text.replace(target, replacement)
    else:
        print(f"Warning: Target string not found: {repr(target)[:60]}")

if text != orig_text:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully updated generate_verbose_notebook.py with English plot titles and labels")
else:
    print("No changes made to generate_verbose_notebook.py")
