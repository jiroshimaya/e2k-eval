from english2kana import english2kana
from e2k_eval.core.loader import load_evaluation_data
from e2k_eval.core.loader import load_evaluation_data
from e2k_eval.core.utils import calculate_relative_editdistance, calculate_relative_kana_distance

import time
# Initialize the translator
e2k = english2kana()
# Load the pretrained model
e2k.load_model()

def convert(english: str) -> str:
    return e2k.translate(english)

def evaluate() -> None:
    evaluation_data = load_evaluation_data()
  
    start = time.perf_counter()
    results = [convert(item.english) for item in evaluation_data]
    elapsed = time.perf_counter() - start
    accuracy = sum(1 for item, result in zip(evaluation_data, results) if item.kana == result) / len(evaluation_data)
    avg_ed = sum(calculate_relative_editdistance(item.kana, result) for item, result in zip(evaluation_data, results)) / len(evaluation_data)
    avg_kana_distance = sum(calculate_relative_kana_distance(item.kana, result) for item, result in zip(evaluation_data, results)) / len(evaluation_data)
    wrong_items = [(item.english, item.kana, result) for item, result in zip(evaluation_data, results) if item.kana != result]
    for wrong_item in wrong_items:
        print(wrong_item)
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Average Edit Distance: {avg_ed:.3f}")
    print(f"Average Kana Distance: {avg_kana_distance:.3f}")
    print(f"Time: {elapsed/len(evaluation_data):.3f} seconds / per item")

if __name__ == "__main__":
    evaluate()
