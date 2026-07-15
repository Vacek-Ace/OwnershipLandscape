import os
import re

workspace_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape"
docs_dir = os.path.join(workspace_dir, "docs")
metodo_file = os.path.join(docs_dir, "metodologia_ownership_landscape.md")
notas_file = os.path.join(docs_dir, "notas_bibliograficas.md")

# 1. Content for the new annotated bibliography file
notas_content = """# Notas Bibliográficas y Relevancia Metodológica

Este documento detalla las referencias científicas clave utilizadas para la conceptualización, diseño metodológico y técnicas de análisis del *Ownership Landscape*. Para cada obra, se presenta su referencia en formato APA 7ª edición, un resumen analítico de su contenido y su relevancia directa para nuestra investigación.

---

## 1. Diseño Teórico y Configuración Organizacional

### Referencia
Meyer, A. D., Tsui, A. S., & Hinings, C. R. (1993). Configurational approaches to organizational analysis. *Academy of Management Journal*, 36(6), 1175–1195. https://doi.org/10.2307/256809

* **¿De qué trata?**: Es el artículo seminal que establece los fundamentos del enfoque configuracional en la teoría de la organización. Propone que las organizaciones y sus entornos no deben estudiarse analizando variables aisladas, sino como configuraciones holísticas y multidimensionales de atributos (estructurales, políticos, culturales y ambientales) que se alinean y coexisten en perfiles definidos.
* **Relevancia para la investigación**: Justifica teóricamente la definición del *Ownership Landscape* como una propiedad emergente y colectiva de la liga. En lugar de estudiar variables de propiedad de forma aislada, este enfoque nos permite modelar la liga como una configuración conjunta de proporciones de control (el vector de 7 dimensiones) y analizar cómo estas configuraciones se desplazan colectivamente en el tiempo.

### Referencia
Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management*, 17(1), 99–120. https://doi.org/10.1177/014920639101700108

* **¿De qué trata?**: Introduce y desarrolla la Teoría de la Visión Basada en Recursos (RBV), argumentando que las empresas pueden lograr una ventaja competitiva sostenible si poseen recursos que sean valiosos, raros, difíciles de imitar y no sustituibles (VRIN).
* **Relevancia para la investigación**: Ayuda a conceptualizar las distintas tipologías de propiedad (ej. multipropiedad corporativa o fondos soberanos) como configuraciones de recursos estratégicos e inyecciones de capital que alteran la capacidad competitiva de los clubes en el mercado de fichajes.

---

## 2. Indicadores Estructurales de Diversidad y Concentración

### Referencia
Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

* **¿De qué trata?**: Es la obra fundacional de la Teoría de la Información. Introduce el concepto de entropía de la información para medir la incertidumbre, el desorden o la cantidad de información contenida en un mensaje o canal de comunicación.
* **Relevancia para la investigación**: Proporciona la formulación matemática de la Entropía de Shannon ($H$) que aplicamos para cuantificar la diversidad del landscape. Permite medir el grado de incertidumbre y equilibrio en la distribución de modelos de propiedad dentro de cada liga-temporada.

### Referencia
Jost, L. (2006). Entropy and diversity. *Oikos*, 113(2), 363–375. https://doi.org/10.1111/j.2006.0030-1299.14714.x

* **¿De qué trata?**: Resuelve la histórica confusión conceptual en ecología y ciencias sociales entre entropía y diversidad. Demuestra que las medidas tradicionales de entropía (como Shannon o Simpson) no son diversidad en sí mismas, sino medidas de incertidumbre, y propone un método matemático para convertirlas en "números equivalentes de especies" (diversidad verdadera).
* **Relevancia para la investigación**: Justifica metodológicamente la interpretación de la Entropía de Shannon como la medida de la coexistencia y balance de múltiples lógicas de propiedad (entornos multi-lógica) en las ligas de fútbol, proporcionando rigor interpretativo a nuestros índices longitudinales.

### Referencia
Hirschman, A. O. (1964). The paternity of an index. *The American Economic Review*, 54(5), 761–762. https://www.jstor.org/stable/1818582

* **¿De qué trata?**: Una breve e influyente nota histórica en la que Albert Hirschman reclama la paternidad del índice de concentración que él propuso originalmente en 1945 (*National Power and the Structure of Foreign Trade*) y que posteriormente Orris Herfindahl redesarrolló de manera independiente en su tesis de 1950.
* **Relevancia para la investigación**: Sirve como referencia bibliográfica y teórica para la aplicación del Índice Herfindahl-Hirschman (HHI). Lo utilizamos para medir de forma cuadrática la concentración y dominancia de modelos específicos (como el modelo de socios en Alemania o la multipropiedad en Inglaterra) sobre el landscape global.

---

## 3. Reducción de Dimensionalidad (Análisis Multivariante)

### Referencia
Pearson, K. (1901). LIII. On lines and planes of closest fit to systems of points in space. *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, 2(11), 559–572. https://doi.org/10.1080/14786440109462720

* **¿De qué trata?**: Es el artículo original donde Karl Pearson define y calcula por primera vez la recta y el plano de mejor ajuste para un sistema de puntos tridimensionales o multidimensionales, sentando las bases matemáticas de lo que hoy conocemos como Análisis de Componentes Principales (PCA).
* **Relevancia para la investigación**: Es la referencia metodológica para la reducción de dimensionalidad de la matriz $\mathbf{P}$ ($30 \times 8$). Justifica el uso de la proyección ortogonal sobre los ejes de máxima varianza (PC1 y PC2) para mapear las 30 observaciones liga-temporada en un espacio bidimensional interpretable.

---

## 4. Tratamiento de Datos Composicionales (CoDa)

### Referencia
Aitchison, J. (1986). *The Statistical Analysis of Compositional Data*. Chapman & Hall.

* **¿De qué trata?**: Es la "biblia" definitiva sobre el análisis estadístico de datos composicionales (datos que representan proporciones o partes de un todo y que están sujetos a una restricción de suma constante, como el simplex). Desarrolla de manera exhaustiva las transformaciones log-ratio (CLR, ALR e ILR) para liberar los datos del simplex y permitir la aplicación de estadísticas clásicas (PCA, correlaciones, regresión) de forma válida.
* **Relevancia para la investigación**: Justifica y rige nuestro enfoque de sensibilidad composicional. Explica por qué el PCA directo sobre proporciones puede sufrir de correlaciones espurias inducidas por la constricción del simplex (donde el aumento de una proporción obliga a la reducción de las demás) y valida nuestro test de robustez mediante la transformación Centered Log-Ratio (CLR).

---

## 5. Contexto Económico y Financiero del Fútbol

### Referencia
Storm, R. H., & Nielsen, K. (2012). Soft budget constraints in professional football. *European Sport Management Quarterly*, 12(2), 183–201. https://doi.org/10.1080/16184742.2012.670660

* **¿De qué trata?**: Aplica la teoría económica de Janos Kornai sobre las "restricciones presupuestarias blandas" (*soft budget constraints*) al fútbol europeo. Explica por qué los clubes de fútbol profesional muestran tasas de supervivencia extraordinariamente altas a pesar de incurrir en déficits crónicos y acumular deudas masivas, gracias al rescate constante por parte de mecenas, corporaciones, o subsidios indirectos.
* **Relevancia para la investigación**: Explica e interpreta la lógica detrás de los modelos de propiedad financiarizados (como los fondos de inversión o corporaciones MCO) y vinculados a estados. Justifica por qué el paisaje de propiedad influye en el comportamiento de gasto en transferencias de los clubes, quienes operan bajo restricciones presupuestarias blandas financiadas por sus UBOs.

### Referencia
Nauright, J., & Ramfjord, J. (2010). Who owns England's game? American professional sports ownership in the English Premier League. *Soccer & Society*, 11(4), 428–441. https://doi.org/10.1080/14660971003780321

* **¿De qué trata?**: Analiza el impacto, motivaciones y diferencias estratégicas de la entrada de capital de propiedad privada extranjera y norteamericana en la Premier League inglesa, detallando el proceso de mercantilización y transnacionalización de la gobernanza de los clubes.
* **Relevancia para la investigación**: Contextualiza la transición de los clubes ingleses desde modelos tradicionales de empresarios locales a corporaciones globales multipropiedad o fondos extranjeros, ayudando a interpretar los perfiles del landscape y la evolución temporal de la Premier League.

### Referencia
UEFA. (2024). *The European Club Finance and Investment Landscape Report*. UEFA.

* **¿De qué trata?**: Informe oficial anual de la UEFA que analiza las finanzas, ingresos, inversiones y estructuras de propiedad de los clubes de fútbol de las asociaciones miembro, prestando especial atención al crecimiento de la multipropiedad (MCO) y la inversión extranjera.
* **Relevancia para la investigación**: Proporciona el marco empírico e institucional más actualizado para contrastar nuestra taxonomía de 7 modelos de propiedad y validar los porcentajes de penetración de multipropiedad en las cinco grandes ligas.
"""

with open(notas_file, "w", encoding="utf-8") as f:
    f.write(notas_content.strip())
print(f"Created annotated bibliography: {notas_file}")

# 2. Modify methodology_ownership_landscape.md to remove redundant references
if os.path.exists(metodo_file):
    with open(metodo_file, "r", encoding="utf-8") as f:
        text = f.read()
    
    orig = text
    
    # Replace in-text citations:
    # 1. (Herfindahl, 1950; Hirschman, 1964) -> (Hirschman, 1964)
    text = text.replace("(Herfindahl, 1950; Hirschman, 1964)", "(Hirschman, 1964)")
    # 2. (Pearson, 1901; Hotelling, 1933) -> (Pearson, 1901)
    text = text.replace("(Pearson, 1901; Hotelling, 1933)", "(Pearson, 1901)")
    # 3. (Aitchison, 1982, 1986) -> (Aitchison, 1986)
    text = text.replace("(Aitchison, 1982, 1986)", "(Aitchison, 1986)")
    
    # Replace references section block:
    old_bib_block = """Aitchison, J. (1982). The statistical analysis of compositional data. *Journal of the Royal Statistical Society: Series B (Methodological)*, 44(2), 139–160. https://doi.org/10.1111/j.2517-6161.1982.tb01195.x

Aitchison, J. (1986). *The Statistical Analysis of Compositional Data*. Chapman & Hall.

Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management*, 17(1), 99–120. https://doi.org/10.1177/014920639101700108

Herfindahl, O. C. (1950). *Concentration in the steel industry* (Doctoral dissertation, Columbia University).

Hirschman, A. O. (1964). The paternity of an index. *The American Economic Review*, 54(5), 761–762. https://www.jstor.org/stable/1818582

Hotelling, H. (1933). Analysis of a complex of statistical variables into principal components. *Journal of Educational Psychology*, 24(6), 417–441. https://doi.org/10.1037/h0071325

Jost, L. (2006). Entropy and diversity. *Oikos*, 113(2), 363–375. https://doi.org/10.1111/j.2006.0030-1299.14714.x

Meyer, A. D., Tsui, A. S., & Hinings, C. R. (1993). Configurational approaches to organizational analysis. *Academy of Management Journal*, 36(6), 1175–1195. https://doi.org/10.2307/256809

Nauright, J., & Ramfjord, J. (2010). Who owns England's game? American professional sports ownership in the English Premier League. *Soccer & Society*, 11(4), 428–441. https://doi.org/10.1080/14660971003780321

Pearson, K. (1901). LIII. On lines and planes of closest fit to systems of points in space. *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, 2(11), 559–572. https://doi.org/10.1080/14786440109462720

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

Storm, R. H., & Nielsen, K. (2012). Soft budget constraints in professional football. *European Sport Management Quarterly*, 12(2), 183–201. https://doi.org/10.1080/16184742.2012.670660

UEFA. (2024). *The European Club Finance and Investment Landscape Report*. UEFA."""

    new_bib_block = """Aitchison, J. (1986). *The Statistical Analysis of Compositional Data*. Chapman & Hall.

Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management*, 17(1), 99–120. https://doi.org/10.1177/014920639101700108

Hirschman, A. O. (1964). The paternity of an index. *The American Economic Review*, 54(5), 761–762. https://www.jstor.org/stable/1818582

Jost, L. (2006). Entropy and diversity. *Oikos*, 113(2), 363–375. https://doi.org/10.1111/j.2006.0030-1299.14714.x

Meyer, A. D., Tsui, A. S., & Hinings, C. R. (1993). Configurational approaches to organizational analysis. *Academy of Management Journal*, 36(6), 1175–1195. https://doi.org/10.2307/256809

Nauright, J., & Ramfjord, J. (2010). Who owns England's game? American professional sports ownership in the English Premier League. *Soccer & Society*, 11(4), 428–441. https://doi.org/10.1080/14660971003780321

Pearson, K. (1901). LIII. On lines and planes of closest fit to systems of points in space. *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, 2(11), 559–572. https://doi.org/10.1080/14786440109462720

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

Storm, R. H., & Nielsen, K. (2012). Soft budget constraints in professional football. *European Sport Management Quarterly*, 12(2), 183–201. https://doi.org/10.1080/16184742.2012.670660

UEFA. (2024). *The European Club Finance and Investment Landscape Report*. UEFA."""

    text = text.replace(old_bib_block, new_bib_block)
    
    if text != orig:
        with open(metodo_file, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Successfully cleaned up methodology file: {metodo_file}")
    else:
        print("No changes made to methodology file")
else:
    print(f"Methodology file not found: {metodo_file}")
