# AAI-590_Capstone

This project builds and fine-tunes machine learning models to generate abstractive summaries of podcast transcripts using Knowledge Distillation from OpenAI GPT-4o. Three models were developed and evaluated:

1. **LSTM with Attention**: A custom-built long short-term memory network with an attention mechanism.
2. **Fine-Tuned Seq2Seq T5 Model**: A pretrained T5 model fine-tuned for summarization tasks.
3. **Fine-Tuned GPT Model**: A GPT-Neo 125M model fine-tuned to produce high-quality summaries.

Target summaries were generated using OpenAI GPT-4o. This project aims to create a model that can produce summaries as good as an LLM but able to be ran on smaller hardware. 

## Project Structure

- **`datasets/`**: Training and testing datasets
- **`results/`**: Output summaries, evaluation metrics, and logs.
- **`Archive/`**: Test notebooks used throughout the capstone project

All notebooks are numbered in the order they should be ran. ie `1_X_.ipynb`

## Key Features

- **Custom LSTM with Attention Layer**: Sequence-to-sequence learning with attention mechanisms.
- **Pretrained Model Fine-Tuning**: Utilizes T5 and GPT-Neo architectures for summarization.
- **Evaluation Metrics**: ROUGE and BLEU scores for assessing model performance. Inference time is also recorded in seconds. 