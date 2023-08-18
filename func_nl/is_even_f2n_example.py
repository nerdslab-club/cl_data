import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2b_is_even_example(count: int):
    examples = []
    for _ in range(count):
        x = random.randint(-100, 100)
        examples.append(
            {
                "inputStr": f"##is_even({x})",
                "outputStr": __random_explanation_is_even(x),
            }
        )
    return examples


def __random_explanation_is_even(x: int) -> str:
    explanations = [
        f"Whether the number {x} is even",
        f"is_even({x})",
        f"Whether {x} is divisible by 2 without remainder",
        f"Calculation: is_even({x})",
        f"Whether the remainder of {x} divided by 2 is 0",
        f"Whether {x} is an even number",
        f"Whether {x} is evenly divisible by 2",
        f"Whether {x} is a multiple of 2",
        f"Whether {x} is a whole number divisible by 2",
        f"Whether the integer {x} is an even number",
        f"Whether {x} can be divided by 2 without leaving a remainder",
        f"Whether {x} can be evenly divided by 2",
        f"Whether {x} is an integer that is divisible by 2",
        f"Whether the result of evaluating is_even({x}) is true",
        f"Whether {x} is a number that is divisible by 2",
        f"Whether {x} is evenly divisible by 2 or not",
        f"Whether {x} can be divided by 2 without having a remainder",
        f"Whether {x} is an integer that can be divided by 2",
        f"Whether {x} is a whole number that is divisible by 2",
        f"Whether the value of is_even({x}) is true or not",
        f"Whether {x} is evenly divisible by 2 or not",
        f"Whether {x} is a number that can be divided by 2",
        f"Whether the result of evaluating {x} % 2 == 0 is true",
        f"Whether {x} is a multiple of 2 or not",
        f"Whether the integer {x} is divisible by 2 or not",
        f"Whether {x} is a whole number that can be divided by 2",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2b_is_even_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
