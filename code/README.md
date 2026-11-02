# Geometric Aggregation for Token Injection (GATI)

This directory contains the core implementation and experimental pipelines for the GATI framework. GATI is a vocabulary initialization protocol designed for zero-resource languages, utilizing norm-scaled subword aggregation to mitigate the spatial collapse inherent in naive mean initialization (such as Fast Vocabulary Transfer).

## Directory Structure

*   **/GATI_function** - Contains the Jupyter Notebook demonstrating the PyTorch implementation of the GATI protocol.
*   **/ablation_study** - Contains the experimental notebooks used to generate the 10-seed comparative evaluation logs.

---

### 1. GATI Function (`/GATI_function`)
This folder contains the step-by-step implementation of the GATI algorithm within a Jupyter environment. It demonstrates how to integrate the protocol into standard Hugging Face `transformers` pipelines. 

The core notebook extracts shattered subword embeddings from a parent language model, calculates the geometric arithmetic mean, applies L2 norm-scaling to match the model's native embedding space, and injects the calibrated vector into the newly resized tokenizer.

### 2. Ablation Study (`/ablation_study`)
This folder contains the fully reproducible experimental setup used to validate GATI against existing baselines across 10 random computational seeds (as presented in the *MethodsX* manuscript).

**Key File:**
*   `NLLB GATI Ablatation Study.ipynb`

The notebook evaluates three distinct initialization protocols on a zero-resource neural machine translation task (Sikka-Indonesian):
1.  **Baseline (Random):** Standard Gaussian noise initialization.
2.  **FVT (Naive Mean):** Raw arithmetic mean of shattered subwords without spatial scaling.
3.  **GATI (Norm-Scaled):** The proposed geometric aggregation method.
