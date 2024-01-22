import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_square_int_example(count: int):
    examples = []
    for _ in range(count):
        x = random.randint(-10, 10)
        examples.append(
            {
                "inputStr": f"##square_int({x})",
                "outputStr": __random_explanation_square_int(x),
            }
        )
    return examples


def __random_explanation_square_int(a: int) -> str:
    explanations = [
        f"The square of the integer {a}",
        f"square_int({a})",
        f"The result of squaring {a}",
        f"Calculation: square_int({a})",
        f"The value obtained by multiplying {a} by itself",
        f"The outcome of calculating the square of {a}",
        f"The squared value of {a}",
        f"The result of squaring the integer {a}",
        f"The computed result of squaring {a}",
        f"The value of {a} squared",
        f"The product of {a} and itself",
        f"The squared result of the number {a}",
        f"The outcome of evaluating square_int({a})",
        f"The computed value of {a} squared is",
        f"The value obtained by raising {a} to the power of 2",
        f"The outcome of finding the square of {a} is",
        f"The squared value obtained by squaring {a}",
        f"The result of raising {a} to the power of 2",
        f"The squared outcome of the number {a} is",
        f"The value of the integer {a} squared is",
        f"The computed squared value of {a} is",
        f"The squared result of {a} is",
        f"The calculated outcome of squaring the number {a} is",
        f"The squared value of {a} is",
        f"The value calculated by squaring {a} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_square_int_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
