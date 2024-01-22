import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


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


def __random_explanation(f2: float, f3: float) -> str:
    explanations = [
        f"Multiplying {f2} by {f3}",
        f"{f2} times {f3}",
        f"{f2} multiplied by {f3}",
        f"The result of {f2} times {f3}",
        f"{f2} multiplied by {f3}, what is it?",
        f"Calculation: {f2} * {f3}",
        f"{f2} times {f3}, equals?",
        f"Taking {f2} and multiplying by {f3}",
        f"{f2} and {f3} product",
        f"The multiplication of {f2} and {f3}",
        f"{f2} times {f3} is?",
        f"{f2} times {f3} is equal to?",
        f"The product of {f2} and {f3}",
        f"{f2} and {f3} multiplied, the result?",
        f"{f2} multiplied by {f3}, the answer?",
        f"{f2} times {f3}, find the result",
        f"Product: {f2} * {f3}",
        f"Let's multiply {f2} and {f3}",
        f"Find the product of {f2} and {f3}",
        f"{f2} and {f3}, their multiplication?",
        f"{f2} multiplied by {f3}, result is",
        f"{f2} and {f3}, what will be the product?",
        f"Multiplication: {f2} * {f3}",
        f"{f2} times {f3}, result?",
        f"{f2} increased {f3}-fold",
        f"{f3} scaled by {f2}",
        f"The total when {f2} is multiplied by {f3}",
        f"{f2} times {f3} equals?",
        f"{f2} multiplied by {f3}, in decimal",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    Utility.create_sample_from_example(
        create_n2f_multiplication_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
    )
