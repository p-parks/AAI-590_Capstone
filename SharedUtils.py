import evaluate
import json
import os

def trim_to_last_punctuation(text):
    # attempt to trim any of the cut off sentences
    # reverse find the last punctuation
    last_punctuation = -1
    for p in ['.', '!', '?']:
        last_punctuation = text.rfind(p)
        if last_punctuation != -1:
            break
    if last_punctuation != -1:
        text = text[:last_punctuation + 1]
    return text


max__text_length = 1024

def trim_to_max_length(text):
    # trim the text to max length
    if len(text) > max__text_length:
        text = text[:max__text_length]
    
    return trim_to_last_punctuation(text)

results_dir = 'results'

def evaluate_and_save_metrics(dir_name, run_name, model_name, reference_summaries, generated_summaries, elapsed_time):
    os.makedirs(f"./results/{dir_name}/{run_name}", exist_ok=True)

    rouge = evaluate.load('rouge')
    rouge_results = rouge.compute(predictions=generated_summaries, references=reference_summaries)
    bleu = evaluate.load('bleu')
    results_bleu = bleu.compute(predictions=generated_summaries, references=reference_summaries)
    
    with open(f"./results/{dir_name}/{run_name}/{model_name}_rouge_results.json", "w") as f:
        json.dump(rouge_results, f)
    with open(f"./results/{dir_name}/{run_name}/{model_name}_bleu_results.json", "w") as f:
        json.dump(results_bleu, f)
    with open(f"./results/{dir_name}/{run_name}/{model_name}_time.txt", "w") as f:
        f.write(f"{elapsed_time}\n")

    return rouge_results, results_bleu 