import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_square_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = random.uniform(-10.0, 10.0)
        examples.append(
            {
                "inputStr": f"##square({x})",
                "outputStr": __random_explanation_square(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_square(f: float, identifier: int | None) -> str:
    explanations = [
        f"The square of the number {f}",
        f"square({f})",
        f"The result of squaring {f}",
        f"Calculation: square({f})",
        f"The value obtained by multiplying {f} by itself",
        f"The outcome of calculating the square of {f}",
        f"The squared value of {f}",
        f"The result of squaring the number {f}",
        f"The computed result of squaring {f}",
        f"The value of {f} squared",
        f"The product of {f} and itself",
        f"The squared result of the number {f}",
        f"The outcome of evaluating square({f})",
        f"The computed value of {f} squared is",
        f"The value obtained by raising {f} to the power of 2",
        f"The outcome of finding the square of {f} is",
        f"The squared value obtained by squaring {f}",
        f"The result of raising {f} to the power of 2",
        f"The squared outcome of the number {f} is",
        f"The value of the number {f} squared is",
        f"The computed squared value of {f} is",
        f"The squared result of {f} is",
        f"The calculated outcome of squaring the number {f} is",
        f"The squared value of {f} is",
        f"The value calculated by squaring {f} is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_square_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
