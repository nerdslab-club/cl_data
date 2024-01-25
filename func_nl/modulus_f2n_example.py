import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_modulus_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        examples.append(
            {
                "inputStr": f"##modulus({num1},{num2})",
                "outputStr": __random_explanation_modulus(
                    num1,
                    num2, 
                    (None if identifier is None else identifier+i)
                ),
            }
        )
    return examples


def __random_explanation_modulus(x: int, y: int, identifier: int | None) -> str:
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
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_modulus_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
