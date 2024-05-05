import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_factorial_example(count: int, identifier: int | None, seed: int):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_integer(seed=seed)
        examples.append(
            {
                "inputStr": f"##factorial({x})",
                "outputStr": __random_explanation_factorial(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_factorial(x: int, identifier: int | None) -> str:
    explanations = [
        f"value of {x} factorial",
        f"product of all positive integers up to {x}",
        f"factorial value of {x}",
        f"calculated result of {x} factorial",

        f"The value obtained by multiplying all integers from 1 to {x}",
        f"The outcome of multiplying all numbers from 1 to {x}",
        f"The result of the product of numbers from 1 to {x}",
        f"The total of multiplying integers from 1 to {x}",
        f"The result of calculating the factorial of {x}",
        f"The value achieved by multiplying numbers from 1 to {x}",
        f"The product of all positive integers less than or equal to {x}",
        f"The outcome of multiplying all positive integers from 1 to {x}",
        f"The product of integers from 1 to {x} is",
        f"The total of multiplying all numbers from 1 to {x} is",
        f"The computed result of factorial({x}) is",
        f"The outcome of the product of all numbers from 1 to {x} is",
        f"The value of the factorial of {x} is",
        f"The product of all integers from 1 to {x} is",
        f"The value obtained by multiplying all positive integers from 1 to {x}",
        f"The outcome of calculating factorial({x}) is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_factorial_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
