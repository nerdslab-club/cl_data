import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_multiplication_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.uniform(0.1, 1000.0)
        num2 = random.uniform(0.1, 1000.0)
        examples.append({
            "inputStr": f"##multiplication({num1},{num2})",
            "outputStr": __random_explanation(num1, num2)
        })
    return examples


def __random_explanation(x: float, y: float) -> str:
    explanations = [
        f"Multiplying {x} with {y}",
        f"{x} * {y}",
        f"The result of multiplying {x} and {y}",
        f"{x} times {y} equals?",
        f"Calculation: {x} * {y}",
        f"{x} multiplied by {y}",
        f"The product of {x} and {y}",
        f"{x} * {y} =",
        f"The total when {x} is multiplied by {y}",
        f"{x} and {y} multiplied together",
        f"{x} * {y} results in",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    Utility.create_sample_from_example(create_f2n_multiplication_example(2),TaskTypes.FUNC_TO_NL_TRANSLATION)
