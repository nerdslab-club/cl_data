import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_round_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        examples.append(
            {
                "inputStr": f"##round({x})",
                "outputStr": __random_explanation_round(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_round(f: float, identifier: int | None) -> str:
    explanations = [
        f"The integer closest to {f} after rounding",
        f"The nearest whole number to {f}",
        f"The integer that is closest to {f} and has the same magnitude",
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
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_round_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
