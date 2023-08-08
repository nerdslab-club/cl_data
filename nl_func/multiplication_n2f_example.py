import random

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_multiplication_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.uniform(0, 1000)  # Using random float between 0 and 1000
        num2 = random.uniform(0, 1000)  # Using random float between 0 and 1000
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2),
                "outputStr": f"##multiplication({num1},{num2})",
            }
        )
    return examples


def __random_explanation(x: float, y: float) -> str:
    explanations = [
        f"Multiplying {x} by {y}",
        f"{x} times {y}",
        f"{x} multiplied by {y}",
        f"The result of {x} times {y}",
        f"{x} multiplied by {y}, what is it?",
        f"Calculation: {x} * {y}",
        f"{x} times {y}, equals?",
        f"Taking {x} and multiplying by {y}",
        f"{x} and {y} product",
        f"The multiplication of {x} and {y}",
        f"{x} times {y} is?",
        f"{x} times {y} is equal to?",
        f"The product of {x} and {y}",
        f"{x} and {y} multiplied, the result?",
        f"{x} multiplied by {y}, the answer?",
        f"{x} times {y}, find the result",
        f"Product: {x} * {y}",
        f"Let's multiply {x} and {y}",
        f"Find the product of {x} and {y}",
        f"{x} and {y}, their multiplication?",
        f"{x} multiplied by {y}, result is",
        f"{x} and {y}, what will be the product?",
        f"Multiplication: {x} * {y}",
        f"{x} times {y}, result?",
        f"{x} increased {y}-fold",
        f"{y} scaled by {x}",
        f"The total when {x} is multiplied by {y}",
        f"{x} times {y} equals?",
        f"{x} multiplied by {y}, in decimal",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    Utility.create_sample_from_example(
        create_n2f_multiplication_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
    )
