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


def __random_explanation_is_even(n: int) -> str:
    explanations = [
        f"Whether the number {n} is even",
        f"is_even({n})",
        f"Whether {n} is divisible by 2 without remainder",
        f"Calculation: is_even({n})",
        f"Whether the remainder of {n} divided by 2 is 0",
        f"Whether {n} is an even number",
        f"Whether {n} is evenly divisible by 2",
        f"Whether {n} is a multiple of 2",
        f"Whether {n} is a whole number divisible by 2",
        f"Whether the integer {n} is an even number",
        f"Whether {n} can be divided by 2 without leaving a remainder",
        f"Whether {n} can be evenly divided by 2",
        f"Whether {n} is an integer that is divisible by 2",
        f"Whether the result of evaluating is_even({n}) is true",
        f"Whether {n} is a number that is divisible by 2",
        f"Whether {n} is evenly divisible by 2 or not",
        f"Whether {n} can be divided by 2 without having a remainder",
        f"Whether {n} is an integer that can be divided by 2",
        f"Whether {n} is a whole number that is divisible by 2",
        f"Whether the value of is_even({n}) is true or not",
        f"Whether {n} is evenly divisible by 2 or not",
        f"Whether {n} is a number that can be divided by 2",
        f"Whether the result of evaluating {n} % 2 == 0 is true",
        f"Whether {n} is a multiple of 2 or not",
        f"Whether the integer {n} is divisible by 2 or not",
        f"Whether {n} is a whole number that can be divided by 2",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2b_is_even_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
