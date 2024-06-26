import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_round_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-100.0, 100.0)
        examples.append(
            {
                "inputStr": f"##round({x})",
                "outputStr": __random_explanation_round(x),
            }
        )
    return examples


def __random_explanation_round(f: float) -> str:
    explanations = [
        f"The integer closest to {f} after rounding",
        f"round({f})",
        f"The nearest whole number to {f}",
        f"Calculation: round({f})",
        f"The integer that is closest to {f} and has the same magnitude",
        f"The number rounded to the nearest integer value",
        f"The integer that is nearest to {f} after rounding",
        f"The value of {f} rounded to the nearest whole number",
        f"The integer value that is nearest to {f}",
        f"The result of rounding {f} to the nearest integer",
        f"The closest whole number to the decimal {f}",
        f"The closest integer to {f} after rounding",
        f"The integer that is closest to {f} is",
        f"The nearest whole number value for the decimal {f}",
        f"The integer value closest to {f}",
        f"The value of {f} rounded to the closest integer",
        f"The result of rounding the decimal {f} to the nearest whole number",
        f"The whole number that is nearest to {f} after rounding",
        f"The integer that is nearest to the number {f}",
        f"The value of {f} rounded to the nearest integer is",
        f"The result of rounding {f} is",
        f"The integer that is closest to the input value {f}",
        f"The nearest integer to the number {f} is",
        f"The integer that is nearest to {f} is",
        f"The value of rounding {f} to the nearest integer",
        f"The integer value nearest to {f}",
        f"The round value of {f} is",
        f"The result of calculating round({f}) is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_round_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
