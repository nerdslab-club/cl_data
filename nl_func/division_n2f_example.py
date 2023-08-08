import random

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_division_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.uniform(
            1, 1000
        )  # Using random float between 1 and 1000 (avoid division by zero)
        num2 = random.uniform(
            1, 1000
        )  # Using random float between 1 and 1000 (avoid division by zero)
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2),
                "outputStr": f"##division({num1},{num2})",
            }
        )
    return examples


def __random_explanation(x: float, y: float) -> str:
    explanations = [
        f"Dividing {x} by {y}",
        f"{x} divided by {y}",
        f"{x} over {y}",
        f"The result of {x} divided by {y}",
        f"{x} divided by {y}, what is it?",
        f"Calculation: {x} / {y}",
        f"{x} divided by {y}, equals?",
        f"Taking {x} and dividing by {y}",
        f"{x} divided by {y}, the answer?",
        f"{x} and {y} division",
        f"The division of {x} and {y}",
        f"{x} divided by {y} is?",
        f"{x} divided by {y} is equal to?",
        f"{x} and {y} divided, the result?",
        f"{x} divided by {y}, find the result",
        f"Quotient: {x} / {y}",
        f"Let's divide {x} by {y}",
        f"Find the result of {x} divided by {y}",
        f"{x} and {y}, their division?",
        f"{x} divided by {y}, result is",
        f"{x} and {y}, what will be the quotient?",
        f"Division: {x} / {y}",
        f"{x} divided by {y}, result?",
        f"{x} separated into {y} parts",
        f"{x} distributed over {y}",
        f"{x} split into {y} groups",
        f"The result when {x} is divided by {y}",
        f"{x} divided by {y}, in decimal",
        f"The quotient when {x} is divided by {y}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    Utility.create_sample_from_example(
        create_n2f_division_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
    )
