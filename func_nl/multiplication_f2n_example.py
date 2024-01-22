import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_multiplication_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.uniform(0.1, 1000.0)
        num2 = random.uniform(0.1, 1000.0)
        examples.append(
            {
                "inputStr": f"##multiplication({num1},{num2})",
                "outputStr": __random_explanation(num1, num2),
            }
        )
    return examples


def __random_explanation(m: float, n: float) -> str:
    explanations = [
        f"Multiplying {m} with {n}",
        f"{m} * {n}",
        f"The result of multiplying {m} and {n}",
        f"{m} times {n} equals?",
        f"Calculation: {m} * {n}",
        f"{m} multiplied by {n}",
        f"The product of {m} and {n}",
        f"{m} * {n} =",
        f"The total when {m} is multiplied by {n}",
        f"{m} and {n} multiplied together",
        f"{m} * {n} results in",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    Utility.create_sample_from_example(
        create_f2n_multiplication_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
    )
