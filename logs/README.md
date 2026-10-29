# Ablation Study Evaluation Logs

This directory contains the raw epoch-by-epoch evaluation metrics for the ablation study detailed in the manuscript. To ensure statistical robustness and reproducibility, all experiments were executed across 10 distinct random seeds (e.g., 42, 123, 456, 789, 1024, 2024, 3141, 4242, 8080, 9999).

## Evaluated Methods
The 30 CSV files are divided equally among the three initialization strategies tested during the study:

1. **Baseline (Random Initialization)**
   * **Files:** `metrics_baseline_seed_*.csv`
   * **Description:** Standard random initialization of new vocabulary tokens. This serves as the control group, exhibiting the "cold-start" delay and spatial disorientation discussed in the methodology.

2. **Naive Mean Aggregation (Unsuccessful Method)**
   * **Files:** `metrics_mean_seed_*.csv`
   * **Description:** A direct mathematical average of shattered subword embeddings without magnitude calibration. These logs demonstrate the spatial collapse that pulls tokens out of the active embedding envelope, serving as the experimental baseline that necessitated the norm-scaled transformation.

3. **GATI (Norm-Scaled Geometric Aggregation)**
   * **Files:** `metrics_norm_mean_seed_*.csv`
   * **Description:** The proposed methodology. These logs validate the immediate semantic alignment and peak performance of the calibrated vectors, circumventing the cold-start delay entirely.

## File Structure
Each CSV file tracks the training progression up to 50 epochs. When loading these logs for independent analysis, the data is structured with the following key metric columns:

* `epoch`: The training epoch number (1.0 to 50.0).
* `step`: The corresponding training step count.
* `train_loss`: The model's cross-entropy loss on the training set.
* `eval_loss`: The validation loss on the evaluation set.
* `eval_bleu`: The BLEU score on the evaluation set.
* `eval_chrf`: The chrF score on the evaluation set.

## Key Results Verification
By isolating the `eval_bleu` metric at `epoch = 50.0` across the 10 seed files for a given method, reviewers can independently verify the peak performance claims highlighted in the manuscript:
* **GATI Average Peak BLEU:** 14.22
* **Baseline Average Peak BLEU:** 9.46
* **Mathematical Improvement:** 4.76 points
