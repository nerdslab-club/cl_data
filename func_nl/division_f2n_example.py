import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_division_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.uniform(0.1, 1000.0)
        num2 = random.uniform(0.1, num1)  # To ensure no division by zero
        examples.append(
            {##division({x},{y})
                "inputStr": f"##division({num1},{num2})",
                "outputStr": __random_explanation(
                    num1,
                    num2,
                ),
            }
        )
    return examples


def __random_explanation(x: float, y: float) -> str:
    explanations = [
        f"Dividing {x} by {y}",
        f"{x} / {y}",
        f"The result of dividing {x} by {y}",
        f"{x} divided by {y} equals?",
        f"Calculation: {x} / {y}",
        f"{x} divided by {y}",
        f"{x} over {y}",
        f"The quotient of {x} and {y}",
        f"{x} / {y} =",
        f"{x} divided by {y} gives",
        f"{x} over {y} is",
        f"{x} divided by {y} results in",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_division_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
