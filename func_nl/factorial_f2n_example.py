import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_factorial_example(count: int):
    examples = []
    for _ in range(count):
        x = random.randint(0, 10)  # Generate integers from 0 to 10
        examples.append(
            {
                "inputStr": f"##factorial({x})",
                "outputStr": __random_explanation_factorial(x),
            }
        )
    return examples


def __random_explanation_factorial(x: int) -> str:
    explanations = [
        f"The factorial of {x}",
        f"factorial({x})",
        f"The product of all positive integers up to {x}",
        f"Calculation: factorial({x})",
        f"The value obtained by multiplying all integers from 1 to {x}",
        f"The outcome of multiplying all numbers from 1 to {x}",
        f"The result of the product of numbers from 1 to {x}",
        f"The factorial value of {x}",
        f"The total of multiplying integers from 1 to {x}",
        f"The value of {x} factorial",
        f"The computed result of {x}!",
        f"The result of calculating the factorial of {x}",
        f"The value achieved by multiplying numbers from 1 to {x}",
        f"The product of all positive integers less than or equal to {x}",
        f"The outcome of multiplying all positive integers from 1 to {x}",
        f"The product of integers from 1 to {x} is",
        f"The total of multiplying all numbers from 1 to {x} is",
        f"The computed result of factorial({x}) is",
        f"The outcome of the product of all numbers from 1 to {x} is",
        f"The factorial of the integer {x} is",
        f"The value of the factorial of {x} is",
        f"The product of all integers from 1 to {x} is",
        f"The value obtained by multiplying all positive integers from 1 to {x}",
        f"The calculated result of {x} factorial is",
        f"The outcome of calculating factorial({x}) is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_factorial_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
