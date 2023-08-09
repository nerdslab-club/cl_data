import random

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_square_root_example(count: int):
    examples = []
    for _ in range(count):
        num = random.uniform(1, 99999)  # Using random float between 1 and 99999
        examples.append(
            {
                "inputStr": __random_explanation(num),
                "outputStr": f"##square_root({num})",
            }
        )
    return examples


def __random_explanation(number: float) -> str:
    explanations = [
        f"Finding the square root of {number}",
        f"The square root of {number}",
        f"Square root of {number}",
        f"Root of {number}, what is it?",
        f"Calculate the square root of {number}",
        f"The number whose square root is {number}",
        f"Square root of {number}, equals?",
        f"Taking the square root of {number}",
        f"Square root of {number}, the answer?",
        f"The square root of {number}, find it",
        f"The root of {number}, the value?",
        f"Square root of {number}, what do you get?",
        f"Square root of {number}, result is",
        f"The result of square root of {number}",
        f"Let's find the square root of {number}",
        f"Root calculation for {number}",
        f"Square root: √{number}",
        f"Find the square root of {number}, result?",
        f"The value when square root is taken for {number}",
        f"The square root of {number}, the outcome?",
        f"The square root of {number}, in decimal",
        f"The square root of {number}, in numerical form",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n1f_square_root_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
