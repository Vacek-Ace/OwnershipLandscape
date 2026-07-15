import os
import re

docs_dir = r"c:\Users\vacek\Proyectos\OwnershipLandscape\docs"
metodo_path = os.path.join(docs_dir, "metodologia_ownership_landscape.md")
notas_path = os.path.join(docs_dir, "notas_bibliograficas.md")

# 1. Update docs/metodologia_ownership_landscape.md
if os.path.exists(metodo_path):
    with open(metodo_path, "r", encoding="utf-8") as f:
        metodo_text = f.read()
    
    # In-text replacements:
    # configurations & RBV:
    metodo_text = metodo_text.replace(
        "en línea con las perspectivas clásicas sobre configuraciones organizacionales (Meyer et al., 1993) y la visión basada en recursos (Barney, 1991). Por lo tanto:",
        "en línea con la perspectiva de configuraciones organizacionales (Fiss, 2007). Por lo tanto:"
    )
    # HHI concentration:
    metodo_text = metodo_text.replace(
        " concentración de mercados (Herfindahl, 1950; Hirschman, 1964):",
        " concentración de mercados y evaluar el grado de competencia sectorial (U.S. Department of Justice & Federal Trade Commission [DOJ & FTC], 2023):"
    )
    # PCA:
    metodo_text = metodo_text.replace(
        "El Análisis de Componentes Principales convencional, desarrollado originalmente por Pearson (1901) y formalizado algebraicamente por Hotelling (1933), se aplica siguiendo la siguiente parametrización:",
        "El Análisis de Componentes Principales (PCA) convencional, parametrizado siguiendo las directrices contemporáneas de reducción dimensional (Jolliffe & Cadima, 2016), se aplica mediante el siguiente procedimiento:"
    )
    # CoDa:
    metodo_text = metodo_text.replace(
        "de acuerdo con la teoría matemática clásica para el análisis de composiciones (Aitchison, 1982, 1986), se aplican dos aproximaciones metodológicas para asegurar la robustez estadística:",
        "de acuerdo con la teoría metodológica moderna para el análisis de composiciones (Pawlowsky-Glahn et al., 2015), se aplican dos aproximaciones metodológicas para asegurar la robustez estadística:"
    )
    # Robustness / sensitivity check CLR-PCA:
    metodo_text = metodo_text.replace(
        "Spearman para el primer componente principal (PC1, el Eje de Internacionalización y Financiarización) superó el **$0.96$** en valor absoluto. Esto confirma de forma empírica que el eje principal de diferenciación e internacionalización de las ligas es sumamente estable y robusto, no viéndose afectado por la constricción de suma constante del simplex composicional.",
        "Spearman para el primer componente principal (PC1, el Eje de Internacionalización y Financiarización) superó el **$0.96$** en valor absoluto. Esto confirma de forma empírica que el eje principal de diferenciación e internacionalización de las ligas es sumamente estable y robusto, no viéndose afectado por la constricción de suma constante del simplex composicional (Pawlowsky-Glahn et al., 2015)."
    )

    # Bibliography section replacement:
    old_bib_block = """## 8. Referencias Bibliográficas

Aitchison, J. (1986). *The Statistical Analysis of Compositional Data*. Chapman & Hall.

Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management*, 17(1), 99–120. https://doi.org/10.1177/014920639101700108

Hirschman, A. O. (1964). The paternity of an index. *The American Economic Review*, 54(5), 761–762. https://www.jstor.org/stable/1818582

Jost, L. (2006). Entropy and diversity. *Oikos*, 113(2), 363–375. https://doi.org/10.1111/j.2006.0030-1299.14714.x

Meyer, A. D., Tsui, A. S., & Hinings, C. R. (1993). Configurational approaches to organizational analysis. *Academy of Management Journal*, 36(6), 1175–1195. https://doi.org/10.2307/256809

Nauright, J., & Ramfjord, J. (2010). Who owns England's game? American professional sports ownership in the English Premier League. *Soccer & Society*, 11(4), 428–441. https://doi.org/10.1080/14660971003780321

Pearson, K. (1901). LIII. On lines and planes of closest fit to systems of points in space. *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, 2(11), 559–572. https://doi.org/10.1080/14786440109462720

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

Storm, R. H., & Nielsen, K. (2012). Soft budget constraints in professional football. *European Sport Management Quarterly*, 12(2), 183–201. https://doi.org/10.1080/16184742.2012.670660

UEFA. (2024). *The European Club Finance and Investment Landscape Report*. UEFA."""

    new_bib_block = """## 8. Referencias Bibliográficas

Fiss, P. C. (2007). A set-theoretic approach to organizational configurations. *Academy of Management Review*, 32(4), 1180–1198. https://doi.org/10.5465/amr.2007.26586092

Jolliffe, I. T., & Cadima, J. (2016). Principal component analysis: a review and recent developments. *Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 374(2065), 20150202. https://doi.org/10.1098/rsta.2015.0202

Jost, L. (2006). Entropy and diversity. *Oikos*, 113(2), 363–375. https://doi.org/10.1111/j.2006.0030-1299.14714.x

Nauright, J., & Ramfjord, J. (2010). Who owns England's game? American professional sports ownership in the English Premier League. *Soccer & Society*, 11(4), 428–441. https://doi.org/10.1080/14660971003780321

Pawlowsky-Glahn, V., Egozcue, J. J., & Tolosana-Delgado, R. (2015). *Modeling and Analysis of Compositional Data*. John Wiley & Sons. https://doi.org/10.1002/9781119003144

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x

Storm, R. H., & Nielsen, K. (2012). Soft budget constraints in professional football. *European Sport Management Quarterly*, 12(2), 183–201. https://doi.org/10.1080/16184742.2012.670660

UEFA. (2024). *The European Club Finance and Investment Landscape Report*. UEFA.

U.S. Department of Justice & Federal Trade Commission. (2023). *Merger Guidelines*. U.S. DOJ & FTC. https://www.ftc.gov/reports/merger-guidelines-2023"""

    metodo_text = metodo_text.replace(old_bib_block, new_bib_block)
    
    with open(metodo_path, "w", encoding="utf-8") as f:
        f.write(metodo_text)
    print("Successfully updated methodology file in workspace")
else:
    print("Methodology file not found")

# 2. Re-create docs/notas_bibliograficas.md with the modern references (no Barney, Aitchison 1986, Hirschman, Meyer, or Pearson)
notas_content = """# Notas Bibliográficas y Relevancia Metodológica (Versión Moderna y Depurada)

Este documento detalla las referencias científicas clave utilizadas para la conceptualización, diseño metodológico y técnicas de análisis del *Ownership Landscape*. Para cada obra, se presenta su referencia en formato APA 7ª edición, un resumen analítico de su contenido y su relevancia directa para nuestra investigación.

---

## 1. Diseño Teórico y Configuración Organizacional

### Referencia
Fiss, P. C. (2007). A set-theoretic approach to organizational configurations. *Academy of Management Review*, 32(4), 1180–1198. https://doi.org/10.5465/amr.2007.26586092

* **¿De qué trata?**: Es el artículo seminal contemporáneo que redefine el enfoque configuracional en los estudios organizacionales. Fiss argumenta que las organizaciones y sus entornos son configuraciones de características mutuamente interdependientes, y propone métodos que permiten modelar empíricamente conceptos como la equifinalidad (distintos caminos para un mismo fin) y la diversidad limitada.
* **Relevancia para la investigación**: Sirve de justificación teórica y empírica para la conceptualización de las ligas como "Ownership Landscapes" (paisajes de propiedad). Nos permite tratar las ligas no mediante la suma lineal de variables de propiedad aisladas, sino como perfiles configuracionales sistémicos y holísticos de lógicas institucionales que cambian colectivamente.

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
U.S. Department of Justice & Federal Trade Commission. (2023). *Merger Guidelines*. U.S. DOJ & FTC. https://www.ftc.gov/reports/merger-guidelines-2023

* **¿De qué trata?**: Directrices oficiales y actualizadas de las autoridades de competencia estadounidenses (DOJ y FTC) para evaluar la concentración y los efectos anticompetitivos en fusiones de mercados. Define formalmente los umbrales de concentración industrial mediante el uso del Índice Herfindahl-Hirschman (HHI).
* **Relevancia para la investigación**: Sustenta la validez y los umbrales de interpretación del Índice HHI que calculamos para las ligas. Nos permite clasificar empíricamente los paisajes de propiedad de las ligas como concentrados, moderadamente concentrados o desconcentrados bajo un marco normativo oficial y actual de economía industrial.

---

## 3. Reducción de Dimensionalidad (Análisis Multivariante)

### Referencia
Jolliffe, I. T., & Cadima, J. (2016). Principal component analysis: a review and recent developments. *Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 374(2065), 20150202. https://doi.org/10.1098/rsta.2015.0202

* **¿De qué trata?**: Es la revisión metodológica de referencia sobre el Análisis de Componentes Principales (PCA) elaborada por Ian Jolliffe, el mayor especialista mundial en la técnica. Revisa los fundamentos del PCA y discute sus desarrollos recientes, su aplicación y las directrices de interpretación de cargas y scores.
* **Relevancia para la investigación**: Sustenta nuestra metodología de reducción de dimensionalidad en el PCA macro (reduciendo la matriz de proporciones de 8 variables a los componentes PC1 y PC2 que explican el $72.5\%$ de la varianza acumulada), dotando al diseño de una base de estadística multivariante contemporánea y rigurosa.

---

## 4. Tratamiento de Datos Composicionales (CoDa)

### Referencia
Pawlowsky-Glahn, V., Egozcue, J. J., & Tolosana-Delgado, R. (2015). *Modeling and Analysis of Compositional Data*. John Wiley & Sons. https://doi.org/10.1002/9781119003144

* **¿De qué trata?**: El libro de texto moderno y de referencia definitiva para el análisis de datos composicionales (datos acotados a un simplex de suma constante, como las proporciones). Presenta las bases matemáticas para analizar composiciones en coordenadas reales mediante transformaciones log-ratio (CLR, ALR, ILR) y detalla el PCA composicional.
* **Relevancia para la investigación**: Es la justificación estadística de nuestra prueba de sensibilidad composicional. Explica por qué realizar PCA convencional sobre proporciones brutas puede distorsionar las correlaciones y la posición geométrica debido al simplex de suma 1.0, y valida la aplicación de la transformación Centered Log-Ratio (CLR) como test de robustez geométrica (Spearman PC1 > 0.96).

---

## 5. Contexto Económico y Financiero del Fútbol

### Referencia
Storm, R. H., & Nielsen, K. (2012). Soft budget constraints in professional football. *European Sport Management Quarterly*, 12(2), 183–201. https://doi.org/10.1080/16184742.2012.670660

* **¿De qué trata?**: Aplica la teoría económica de Janos Kornai sobre las "restricciones presupuestarias blandas" (*soft budget constraints*) al fútbol europeo. Explica por qué los clubes de fútbol profesional muestran tasas de supervivencia extraordinariamente altas a pesar de incurrir en déficits crónicos y acumular deudas masivas, gracias al rescate constante por parte de mecenas, corporaciones, o subsidios indirectos.
* **Relevancia para la investigación**: Explica e interpreta la lógica detrás de los modelos de propiedad financiarizados (como los fondos de inversión o corporaciones MCO) y vinculados a estados. Justifica por qué el paisaje de propiedad influye en el comportamiento de gasto en transferencias de los clubes, quienes operan bajo restricciones presupuestarias blandas financiadas por sus UBOs.

### Referencia
Nauright, J., & Ramfjord, J. (2010). Who owns England's game? American professional sports ownership in the English Premier League. *Soccer & Society*, 11(4), 428–441. https://doi.org/10.1080/14660971003780321

* **¿De qué trata?**: Analiza el impacto, motivaciones y diferencias estratégicas de la entrada de capital de propiedad privada extranjera y norteamericana en la Premier League inglesa, detailing el proceso de mercantilización y transnacionalización de la gobernanza de los clubes.
* **Relevancia para la investigación**: Contextualiza la transición de los clubes ingleses desde modelos tradicionales de empresarios locales a corporaciones globales multipropiedad o fondos extranjeros, ayudando a interpretar los perfiles del landscape y la evolución temporal de la Premier League.

### Referencia
UEFA. (2024). *The European Club Finance and Investment Landscape Report*. UEFA.

* **¿De qué trata?**: Informe oficial anual de la UEFA que analiza las finanzas, ingresos, inversiones y estructuras de propiedad de los clubes de fútbol de las asociaciones miembro, prestando especial atención al crecimiento de la multipropiedad (MCO) y la inversión extranjera.
* **Relevancia para la investigación**: Proporciona el marco empírico e institucional más actualizado para contrastar nuestra taxonomía de 7 modelos de propiedad y validar los porcentajes de penetración de multipropiedad en las cinco grandes ligas.
"""

with open(notas_path, "w", encoding="utf-8") as f:
    f.write(notas_content.strip())
print("Successfully re-created annotated bibliography with modern references")
