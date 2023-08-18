import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2b_is_odd_example(count: int):
    examples = []
    for _ in range(count):
        x = random.randint(-100, 100)
        examples.append(
            {
                "inputStr": f"##is_odd({x})",
                "outputStr": __random_explanation_is_odd(x),
            }
        )
    return examples


def __random_explanation_is_odd(x: int) -> str:
    explanations = [
        f"Whether the number {x} is odd",
        f"is_odd({x})",
        f"Whether {x} is not divisible by 2 without remainder",
        f"Calculation: is_odd({x})",
        f"Whether the remainder of {x} divided by 2 is not 0",
        f"Whether {x} is not an even number",
        f"Whether {x} is not evenly divisible by 2",
        f"Whether {x} is not a multiple of 2",
        f"Whether {x} is not a whole number divisible by 2",
        f"Whether the integer {x} is not an even number",
        f"Whether {x} cannot be divided by 2 without leaving a remainder",
        f"Whether {x} cannot be evenly divided by 2",
        f"Whether {x} is not an integer that is divisible by 2",
        f"Whether the result of evaluating is_odd({x}) is true",
        f"Whether {x} is not a number that is divisible by 2",
        f"Whether {x} is not evenly divisible by 2 or not",
        f"Whether {x} cannot be divided by 2 without having a remainder",
        f"Whether {x} is not an integer that can be divided by 2",
        f"Whether {x} is not a whole number that is divisible by 2",
        f"Whether the value of is_odd({x}) is true or not",
        f"Whether {x} is not evenly divisible by 2 or not",
        f"Whether {x} is not a number that can be divided by 2",
        f"Whether the result of evaluating {x} % 2 != 0 is true",
        f"Whether {x} is not a multiple of 2 or not",
        f"Whether the integer {x} is not divisible by 2 or not",
        f"Whether {x} is not a whole number that can be divided by 2",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2b_is_odd_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
