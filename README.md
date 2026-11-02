GATI: Geometric Aggregation for Token Injection

This repository contains the code, dataset sample, and experimental logs for the framework presented in the manuscript: "Geometric Aggregation for Token Injection (GATI): A Norm-Scaled Framework for Vocabulary Adaptation in Pre-Trained Language Models."
GATI is a mathematical initialization protocol designed to prevent "spatial collapse" when expanding the vocabulary of Pre-Trained Language Models (PLMs). It was specifically evaluated on a zero-resource machine translation task for the indigenous Sikka language (Flores Island, Indonesia).

🗂 Repository Structure

/code: Python scripts and Jupyter notebooks demonstrating the Protocol Buffer (Protobuf) manipulation and Algorithm 1 (Norm-Scaled Geometric Aggregation) for injecting new tokens into a pre-trained tokenizer (e.g., SentencePiece).

/dataset: A curated sample of 821 Sikka-Indonesian parallel sentences used for model fine-tuning and evaluation.

/logs: The complete set of 30 ablation study CSV files. These contain the exact BLEU and chrF metric trajectories across 10 random seeds for the Baseline (Random), Naive Mean, and GATI (Norm-Scaled) initializations up to epoch 50.

🚀 Key Results

By bypassing the "cold-start" recovery phase typical of random token initialization, GATI provides immediate semantic alignment. Based on the evaluation logs provided in this repository, at epoch 50, GATI achieves an average peak BLEU score of 14.22, compared to the random baseline's 9.46—a 4.76-point performance improvement.

🤝 Acknowledgments

This research was financially supported by the Indonesia Endowment Fund for Education Agency (Lembaga Pengelola Dana Pendidikan / LPDP) under the Ministry of Finance, Republic of Indonesia. We extend our deepest gratitude to the native Sikka language speakers and local research partners in Kabupaten Sikka for their invaluable collaboration in the digital preservation of the Sikka language.

📜 Citation

If you use this code or dataset, please cite our paper:

not published, planned for MethodsX submission
