import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_square_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-10.0, 10.0)
        examples.append(
            {
                "inputStr": f"##square({x})",
                "outputStr": __random_explanation_square(x),
            }
        )
    return examples


def __random_explanation_square(x: float) -> str:
    explanations = [
        f"The square of the number {x}",
        f"square({x})",
        f"The result of squaring {x}",
        f"Calculation: square({x})",
        f"The value obtained by multiplying {x} by itself",
        f"The outcome of calculating the square of {x}",
        f"The squared value of {x}",
        f"The result of squaring the number {x}",
        f"The computed result of squaring {x}",
        f"The value of {x} squared",
        f"The product of {x} and itself",
        f"The squared result of the number {x}",
        f"The outcome of evaluating square({x})",
        f"The computed value of {x} squared is",
        f"The value obtained by raising {x} to the power of 2",
        f"The outcome of finding the square of {x} is",
        f"The squared value obtained by squaring {x}",
        f"The result of raising {x} to the power of 2",
        f"The squared outcome of the number {x} is",
        f"The value of the number {x} squared is",
        f"The computed squared value of {x} is",
        f"The squared result of {x} is",
        f"The calculated outcome of squaring the number {x} is",
        f"The squared value of {x} is",
        f"The value calculated by squaring {x} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_square_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
