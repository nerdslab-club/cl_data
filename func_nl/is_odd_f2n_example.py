import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_is_odd_example(count: int):
    examples = []
    for _ in range(count):
        x = random.randint(-100, 100)
        examples.append(
            {##is_odd({n})
                "inputStr": f"##is_odd({x})",
                "outputStr": __random_explanation_is_odd(x),
            }
        )
    return examples


def __random_explanation_is_odd(n: int) -> str:
    explanations = [
        f"Whether the number {n} is odd",
        f"is_odd({n})",
        f"Whether {n} is not divisible by 2 without remainder",
        f"Calculation: is_odd({n})",
        f"Whether the remainder of {n} divided by 2 is not 0",
        f"Whether {n} is not an even number",
        f"Whether {n} is not evenly divisible by 2",
        f"Whether {n} is not a multiple of 2",
        f"Whether {n} is not a whole number divisible by 2",
        f"Whether the integer {n} is not an even number",
        f"Whether {n} cannot be divided by 2 without leaving a remainder",
        f"Whether {n} cannot be evenly divided by 2",
        f"Whether {n} is not an integer that is divisible by 2",
        f"Whether the result of evaluating is_odd({n}) is true",
        f"Whether {n} is not a number that is divisible by 2",
        f"Whether {n} is not evenly divisible by 2 or not",
        f"Whether {n} cannot be divided by 2 without having a remainder",
        f"Whether {n} is not an integer that can be divided by 2",
        f"Whether {n} is not a whole number that is divisible by 2",
        f"Whether the value of is_odd({n}) is true or not",
        f"Whether {n} is not evenly divisible by 2 or not",
        f"Whether {n} is not a number that can be divided by 2",
        f"Whether the result of evaluating {n} % 2 != 0 is true",
        f"Whether {n} is not a multiple of 2 or not",
        f"Whether the integer {n} is not divisible by 2 or not",
        f"Whether {n} is not a whole number that can be divided by 2",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_is_odd_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
