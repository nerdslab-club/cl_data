import random
import math

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_is_perfect_square_example(count: int):
    examples = []
    for _ in range(count):
        x = random.randint(1, 100)
        is_perfect_square_result = math.isqrt(x) ** 2 == x
        examples.append(
            {
                "inputStr": f"##is_perfect_square({x})",
                "outputStr": __random_explanation_is_perfect_square(x, is_perfect_square_result),
            }
        )
    return examples


def __random_explanation_is_perfect_square(x: int, is_perfect_square_result: bool) -> str:
    square_str = "a perfect square" if is_perfect_square_result else "not a perfect square"
    explanations = [
        f"Whether {x} is {square_str}",
        f"is_perfect_square({x})",
        f"Checking if {x} is a perfect square",
        f"Calculation: is_perfect_square({x})",
        f"Whether the integer {x} is a perfect square",
        f"Determining if the value {x} is a perfect square",
        f"Verifying if {x} is {square_str}",
        f"Finding if {x} is a perfect square number",
        f"Checking if the number {x} is a perfect square",
        f"Whether {x} is a number that can be squared",
        f"Whether {x} is a perfect square or not",
        f"Checking if the value {x} can be squared",
        f"Checking if the integer {x} is {square_str}",
        f"Finding whether {x} is {square_str}",
        f"Verifying whether {x} is a perfect square or not",
        f"Determining if {x} is a number that can be squared",
        f"The outcome of evaluating is_perfect_square({x}) is",
        f"Checking if {x} is {square_str} is",
        f"The boolean result of checking if {x} is {square_str}",
        f"The result of checking if the integer {x} is {square_str} is",
        f"The boolean outcome of the is_perfect_square({x}) calculation is",
        f"Verifying if {x} is a number that can be squared is",
        f"The boolean value indicating if {x} is {square_str} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_is_perfect_square_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
