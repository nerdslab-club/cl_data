import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_square_root_example(count: int):
    examples = []
    for _ in range(count):
        number = random.uniform(0.1, 10000.0)
        examples.append(
            {
                "inputStr": f"##square_root({number})",
                "outputStr": __random_explanation_sqrt(
                    number,
                ),
            }
        )
    return examples


def __random_explanation_sqrt(number: float) -> str:
    explanations = [
        f"The square root of {number}",
        f"√ {number}",
        f"The result of taking the square root of {number}",
        f"Calculation: √ {number}",
        f"The square root of {number} is",
        f"The positive square root of {number}",
        f"The value of √ {number}",
        f"The non-negative square root of {number}",
        f"The square root of {number} equals?",
        f"The radical of {number}",
        f"The square root of {number} is approximately",
        f"The principal square root of {number}",
        f"The square root of {number} gives",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_square_root_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
