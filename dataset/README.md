# Sikka-Indonesian Parallel Corpus (Dataset Sample)
This branch contains a curated sample of 821 parallel sentence pairs in Sikka and Indonesian. This dataset serves as the foundational evaluation corpus for testing dynamic vocabulary adaptation and subword tokenization strategies in zero-resource machine translation.

## The Sikka Language (Sara Sikka)
Sikka is an under-documented, indigenous language spoken primarily in Kabupaten Sikka, East Nusa Tenggara, Indonesia. From a computational linguistics perspective, Sikka presents unique morphological and orthographic challenges:
* **Glottal Orthography:** The language relies heavily on glottal stops, represented by apostrophes (e.g., *wi'in*). These glottal stops are not merely phonetic accents; they are critical semantic boundaries used across verbs, pronouns, and nouns. 
* **Pronoun-Linked Morphology:** Base verbs undergo complex morphological variations that act as synonyms directly linked to personal pronouns. 
* **Zero-Resource Status:** Sikka lacks representation in large-scale multilingual pre-training corpora, meaning standard tokenizers often shatter its unique morphological structures into nonsensical subword fragments, leading to spatial collapse during fine-tuning.

## Dataset Curation
This 821-sentence sample was digitized and extracted from a physical Sikka-Indonesia dictionary via optical character recognition (OCR) and meticulously cleaned. The entries were subsequently verified in collaboration with native Sikka language speakers and local research partners to ensure dialectal accuracy (specifically capturing Sikka Krowe nuances) and correct glottal tokenization.

## Data Structure
The dataset is formatted as a semicolon-separated values (CSV) file. When loading this data using libraries like `pandas`, ensure the delimiter is explicitly set to `;`.

| Column Header | Description |
| :--- | :--- |
| `no` | The sequential index number of the dataset entry. |
| `jenis_data` | The data type or categorization tag for the entry. |
| `bahasa_sikka` | The source text in the Sikka language, preserving native glottal orthography. |
| `bahasa_indonesia` | The parallel target text translated into Indonesian. |

### Usage Example (Python/Pandas)
```python
import pandas as pd

# Load the dataset using the semicolon delimiter
df = pd.read_csv('sikka_indonesian_sample.csv', sep=';')
print(df.head())
