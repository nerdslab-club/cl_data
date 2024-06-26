import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_modulus_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        examples.append(
            {
                "inputStr": f"##modulus({num1},{num2})",
                "outputStr": __random_explanation_modulus(
                    num1,
                    num2,
                ),
            }
        )
    return examples


def __random_explanation_modulus(x: int, y: int) -> str:
    explanations = [
        f"The modulus of {x} by {y}",
        f"{x} % {y}",
        f"The remainder when {x} is divided by {y}",
        f"The result of the modulus operation on {x} and {y}",
        f"Calculation: {x} % {y}",
        f"The remainder after dividing {x} by {y}",
        f"{x} modulus {y}",
        f"{x} % {y} equals?",
        f"The modulo result of {x} divided by {y}",
        f"The remainder of {x} divided by {y}",
        f"The value of {x} % {y}",
        f"The modulus of {x} and {y} is",
        f"The remainder of dividing {x} by {y}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_modulus_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
