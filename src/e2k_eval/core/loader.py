from pathlib import Path
import random

from e2k_eval.schemas import WordPair

def load_evaluation_data() -> list[WordPair]:
    file_path = Path(__file__).parent.parent.parent.parent / "local/bep-eng.dic"
    num = 100
    seed = 42
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        lines = [line for line in lines if not line.startswith("#")]
        random.seed(seed)
        lines = random.sample(lines, min(num, len(lines)))
        dictlist = []
        for line in lines:
            english, kana = line.split()
            dictlist.append(WordPair(english=english, kana=kana))

        return dictlist


if __name__ == "__main__":
    # Example usage
    word_pairs = load_evaluation_data()
    print(len(word_pairs))
    for pair in word_pairs[:10]:
        print(f"English: {pair.english}, Kana: {pair.kana}")
