import editdistance as ed
from kanasim import create_kana_distance_calculator

kana_distance_calculator = create_kana_distance_calculator()


def calculate_relative_editdistance(reference: str, hypothesis: str) -> float:
    return ed.eval(reference, hypothesis) / len(reference)


def calculate_relative_kana_distance(reference: str, hypothesis: str) -> float:
    return kana_distance_calculator.calculate(reference, hypothesis) / len(reference)
