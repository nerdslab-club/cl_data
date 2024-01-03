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


def __random_explanation_sqrt(f: float) -> str:
    explanations = [
        f"The square root of {f}",
        f"√ {f}",
        f"The result of taking the square root of {f}",
        f"Calculation: √ {f}",
        f"The square root of {f} is",
        f"The positive square root of {f}",
        f"The value of √ {f}",
        f"The non-negative square root of {f}",
        f"The square root of {f} equals?",
        f"The radical of {f}",
        f"The square root of {f} is approximately",
        f"The principal square root of {f}",
        f"The square root of {f} gives",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_square_root_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
