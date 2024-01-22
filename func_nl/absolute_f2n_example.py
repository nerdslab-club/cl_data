import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_absolute_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-100.0, 100.0)
        examples.append(
            {
                "inputStr": f"##absolute({x})",
                "outputStr": __random_explanation_absolute(x),
            }
        )
    return examples


def __random_explanation_absolute(x: float) -> str:
    explanations = [
        f"The absolute value of the number {x}",
        f"absolute({x})",
        f"The result of taking the absolute value of {x}",
        f"Calculation: absolute({x})",
        f"The magnitude of the number {x}",
        f"The non-negative value of {x}",
        f"The outcome of calculating the absolute value of {x}",
        f"The absolute magnitude of {x}",
        f"The result of evaluating the absolute value of {x}",
        f"The value obtained by removing the sign of {x}",
        f"The absolute value of the quantity {x}",
        f"The absolute result of the number {x}",
        f"The outcome of finding the absolute value of {x}",
        f"The computed value of absolute({x}) is",
        f"The value obtained by discarding the sign of {x} is",
        f"The result of evaluating the magnitude of {x}",
        f"The absolute outcome of the number {x} is",
        f"The value of {x} without its sign is",
        f"The computed absolute value of {x} is",
        f"The non-negative result of evaluating the expression {x}",
        f"The absolute value of {x} is",
        f"The value of the number {x} without its sign is",
        f"The calculated absolute value of {x} is",
        f"The result of taking the absolute magnitude of {x} is",
        f"The outcome of finding the absolute magnitude of {x} is",
        f"The absolute result of evaluating {x} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_absolute_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
