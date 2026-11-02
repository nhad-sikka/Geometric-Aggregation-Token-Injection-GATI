# Geometric Aggregation for Token Injection (GATI)

This directory contains the core implementation and experimental pipelines for the GATI framework. GATI is a vocabulary initialization protocol designed for zero-resource languages, utilizing norm-scaled subword aggregation to mitigate the spatial collapse inherent in naive mean initialization (such as Fast Vocabulary Transfer).

## Directory Structure

*   **/GATI_function** - Contains the standalone PyTorch implementation of the GATI protocol.
*   **/ablation_study** - Contains the scripts and training configurations used to generate the 10-seed comparative evaluation logs.

---

### 1. GATI Function (`/GATI_function`)
This folder contains the modular implementation of the GATI algorithm. It is designed to be easily integrated into standard Hugging Face `transformers` pipelines. 

The core function extracts shattered subword embeddings from a parent language model, calculates the geometric arithmetic mean, applies L2 norm-scaling to match the model's native embedding space, and injects the calibrated vector into the newly resized tokenizer.

**Key File:**
*   `gati_initializer.py`: The primary script containing the `apply_gati_initialization()` function.

### 2. Ablation Study (`/ablation_study`)
This folder contains the fully reproducible experimental setup used to validate GATI against existing baselines across 10 random computational seeds (as presented in the *MethodsX* manuscript).

The scripts here evaluate three distinct initialization protocols on a zero-resource neural machine translation task (Sikka-Indonesian):
1.  **Baseline (Random):** Standard Gaussian noise initialization.
2.  **FVT (Naive Mean):** Raw arithmetic mean of shattered subwords without spatial scaling.
3.  **GATI (Norm-Scaled):** The proposed geometric aggregation method.

**Execution:**
To reproduce the training runs and extract the exact BLEU and chrF convergence metrics, run the evaluation script:
```bash
# Example execution command (update with your actual script name)
python run_10_seed_ablation.py --config config.json
