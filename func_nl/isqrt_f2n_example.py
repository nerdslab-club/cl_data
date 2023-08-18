import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_isqrt_example(count: int):
    examples = []
    for _ in range(count):
        x = random.randint(0, 1000)
        examples.append(
            {
                "inputStr": f"##isqrt({x})",
                "outputStr": __random_explanation_isqrt(x),
            }
        )
    return examples


def __random_explanation_isqrt(x: int) -> str:
    explanations = [
        f"The integer square root of {x}",
        f"isqrt({x})",
        f"The largest integer that, when squared, is less than or equal to {x}",
        f"Calculation: isqrt({x})",
        f"The floor value of the square root of {x}",
        f"The greatest integer whose square is less than or equal to {x}",
        f"The square root of {x} rounded down to the nearest integer",
        f"The value of the square root of {x} rounded down",
        f"The integer value of the square root of {x}",
        f"The result of finding the integer square root of {x}",
        f"The whole number part of the square root of {x}",
        f"The largest integer whose square is less than or equal to {x} is",
        f"The floor value of the square root of {x} is",
        f"The greatest integer whose square is less than or equal to {x} is",
        f"The square root of {x} rounded down to the nearest integer is",
        f"The value of the square root of {x} rounded down is",
        f"The integer value of the square root of {x} is",
        f"The result of calculating the integer square root of {x} is",
        f"The whole number part of the square root of {x} is",
        f"The largest integer that, when squared, is less than or equal to {x} is",
        f"The value of isqrt({x}) is",
        f"The isqrt value of {x} is",
        f"The floor square root of {x} is",
        f"The integer square root of {x} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_isqrt_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
