import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_n2f_square_root_example(count: int):
    examples = []
    for _ in range(count):
        num = round(random.uniform(1, 99999), 2)  # Using random float between 1 and 99999
        examples.append(
            {
                "inputStr": __random_explanation(num),
                "outputStr": f"##square_root({num})",
            }
        )
    return examples


def __random_explanation(f1: float) -> str:
    explanations = [
        f"Finding the square root of {f1}",
        f"The square root of {f1}",
        f"Square root of {f1}",
        f"Root of {f1}, what is it?",
        f"Calculate the square root of {f1}",
        f"The number whose square root is {f1}",
        f"Square root of {f1}, equals?",
        f"Taking the square root of {f1}",
        f"Square root of {f1}, the answer?",
        f"The square root of {f1}, find it",
        f"The root of {f1}, the value?",
        f"Square root of {f1}, what do you get?",
        f"Square root of {f1}, result is",
        f"The result of square root of {f1}",
        f"Let's find the square root of {f1}",
        f"Root calculation for {f1}",
        f"Square root: √{f1}",
        f"Find the square root of {f1}, result?",
        f"The value when square root is taken for {f1}",
        f"The square root of {f1}, the outcome?",
        f"The square root of {f1}, in decimal",
        f"The square root of {f1}, in numerical form",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_square_root_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
