import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


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


def __random_explanation(a: int, b: int) -> str:
    explanations = [
        f"The remainder when {a} is divided by {b}",
        f"Finding the modulus of {a} divided by {b}",
        f"The modulus of {a} when divided by {b}",
        f"{a} modulo {b}, what is it?",
        f"Calculate the remainder when {a} is divided by {b}",
        f"The number {a} mod {b}",
        f"The result of {a} modulo {b}",
        f"The remainder when {a} is divided by {b}, what is it?",
        f"Calculation: {a} % {b}",
        f"The remainder of {a} divided by {b}, equals?",
        f"The remaining value when {a} is divided by {b}",
        f"The remainder when {a} is divided by {b}, find it",
        f"The result when {a} modulo {b}",
        f"Let's find the remainder when {a} is divided by {b}",
        f"Find the modulus of {a} divided by {b}",
        f"{a} divided by {b}, what is the leftover?",
        f"The value of {a} modulo {b}",
        f"{a} modulo {b}, result is",
        f"The outcome when {a} is divided by {b}, the remainder?",
        f"The remainder when {a} is divided by {b}, in numbers",
        f"The modulus of {a} divided by {b}, the outcome?",
        f"{a} divided by {b}, what's left?",
        f"The result when {a} is divided by {b}, the remainder?",
        f"{a} divided by {b}, the remainder?",
        f"{a} divided into {b} parts, what remains?",
        f"The value left after {a} is divided by {b}",
        f"The value remaining when {a} is divided by {b}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_modulus_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
