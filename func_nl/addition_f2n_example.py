import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_addition_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.randint(0, 1000)
        num2 = random.randint(0, 1000)
        examples.append({
            "inputStr": f"##addition({num1},{num2})",
            "outputStr": __random_explanation(num1, num2)
        })
    return examples


def __random_explanation(x: int, y: int) -> str:
    explanations = [
        f"Adding {x} plus {y}",
        f"{x} + {y}",
        f"Summing {x} with {y}...",
        f"The result of adding {x} and {y}",
        f"{x} plus {y} equals?",
        f"Calculation: {x} + {y}",
        f"{x} plus {y} is?",
        f"Summing up {x} and {y}",
        f"{x} combined with {y}",
        f"The sum of {x} and {y}",
        f"{x} + {y} =",
        f"The total of {x} and {y}",
        f"Sum: {x} + {y}",
        f"{x} and {y} added together",
        f"{x} + {y} results in",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    Utility.create_sample_from_example(create_f2n_addition_example(2),TaskTypes.FUNC_TO_NL_TRANSLATION)
