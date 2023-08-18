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


def __random_explanation_round(x: float) -> str:
    explanations = [
        f"The integer closest to {x} after rounding",
        f"round({x})",
        f"The nearest whole number to {x}",
        f"Calculation: round({x})",
        f"The integer that is closest to {x} and has the same magnitude",
        f"The number rounded to the nearest integer value",
        f"The integer that is nearest to {x} after rounding",
        f"The value of {x} rounded to the nearest whole number",
        f"The integer value that is nearest to {x}",
        f"The result of rounding {x} to the nearest integer",
        f"The closest whole number to the decimal {x}",
        f"The closest integer to {x} after rounding",
        f"The integer that is closest to {x} is",
        f"The nearest whole number value for the decimal {x}",
        f"The integer value closest to {x}",
        f"The value of {x} rounded to the closest integer",
        f"The result of rounding the decimal {x} to the nearest whole number",
        f"The whole number that is nearest to {x} after rounding",
        f"The integer that is nearest to the number {x}",
        f"The value of {x} rounded to the nearest integer is",
        f"The result of rounding {x} is",
        f"The integer that is closest to the input value {x}",
        f"The nearest integer to the number {x} is",
        f"The integer that is nearest to {x} is",
        f"The value of rounding {x} to the nearest integer",
        f"The integer value nearest to {x}",
        f"The round value of {x} is",
        f"The result of calculating round({x}) is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_round_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
