import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_invert_number_example(count: int):
    examples = []
    for _ in range(count):
        number = random.uniform(0.1, 10.0)
        examples.append(
            {
                "inputStr": f"##invert_number({number})",
                "outputStr": __random_explanation_invert_number(number),
            }
        )
    return examples


def __random_explanation_invert_number(number: float) -> str:
    explanations = [
        f"The multiplicative inverse of the number {number}",
        f"invert_number({number})",
        f"The result of calculating the reciprocal of the number {number}",
        f"Calculation: invert_number({number})",
        f"The reciprocal value of the number {number}",
        f"The outcome of finding the multiplicative inverse of the number {number}",
        f"The number that, when multiplied by {number}, results in 1",
        f"The result of determining the inverse of the number {number}",
        f"The computed result of calculating the multiplicative inverse of the number {number}",
        f"The value that, when multiplied by {number}, equals 1",
        f"The outcome of evaluating invert_number({number})",
        f"The value obtained by finding the reciprocal of the number {number}",
        f"The result of evaluating invert_number({number})",
        f"The value that, when multiplied by {number}, gives the result 1",
        f"The computed reciprocal value of the number {number}",
        f"The value that, when multiplied by {number}, gives the outcome 1",
        f"The calculated result of determining the multiplicative inverse of the number {number}",
        f"The reciprocal number for the given number {number}",
        f"The result obtained from calculating the reciprocal of the number {number}",
        f"The computed value of the multiplicative inverse of the number {number}",
        f"The reciprocal of the number {number} is",
        f"The result derived from calculating the reciprocal of the number {number}",
        f"The computed inverse value of the number {number}",
        f"The calculated outcome of evaluating invert_number({number})",
        f"The reciprocal fraction for the number {number}",
        f"The calculated inverse value of the number {number}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_invert_number_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
