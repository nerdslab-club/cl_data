import random

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_modulus_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.randint(1, 99999)  # Using random integer between 1 and 99999
        num2 = random.randint(
            1, 99999
        )  # Using random integer between 1 and 99999 (avoid division by zero)
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2),
                "outputStr": f"##modulus({num1},{num2})",
            }
        )
    return examples


def __random_explanation(x: int, y: int) -> str:
    explanations = [
        f"The remainder when {x} is divided by {y}",
        f"Finding the modulus of {x} divided by {y}",
        f"The modulus of {x} when divided by {y}",
        f"{x} modulo {y}, what is it?",
        f"Calculate the remainder when {x} is divided by {y}",
        f"The number {x} mod {y}",
        f"The result of {x} modulo {y}",
        f"The remainder when {x} is divided by {y}, what is it?",
        f"Calculation: {x} % {y}",
        f"The remainder of {x} divided by {y}, equals?",
        f"The remaining value when {x} is divided by {y}",
        f"The remainder when {x} is divided by {y}, find it",
        f"The result when {x} modulo {y}",
        f"Let's find the remainder when {x} is divided by {y}",
        f"Find the modulus of {x} divided by {y}",
        f"{x} divided by {y}, what is the leftover?",
        f"The value of {x} modulo {y}",
        f"{x} modulo {y}, result is",
        f"The outcome when {x} is divided by {y}, the remainder?",
        f"The remainder when {x} is divided by {y}, in numbers",
        f"The modulus of {x} divided by {y}, the outcome?",
        f"{x} divided by {y}, what's left?",
        f"The result when {x} is divided by {y}, the remainder?",
        f"{x} divided by {y}, the remainder?",
        f"{x} divided into {y} parts, what remains?",
        f"The value left after {x} is divided by {y}",
        f"The value remaining when {x} is divided by {y}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_modulus_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
