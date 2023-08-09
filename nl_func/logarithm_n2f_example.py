import random
import math

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_logarithm_example(count: int):
    examples = []
    for _ in range(count):
        num = random.uniform(1, 1000)  # Using random float between 1 and 1000
        base = random.uniform(2, 10)  # Using random float between 2 and 10 for base
        examples.append(
            {
                "inputStr": __random_explanation(num, base),
                "outputStr": f"##logarithm({num},{base})",
            }
        )
    return examples


def __random_explanation(x: float, base: float) -> str:
    explanations = [
        f"Finding the logarithm of {x} to the base {base}",
        f"The logarithm of {x} with base {base}",
        f"Logarithm of {x} to the base {base}",
        f"Logarithm of {x} in base {base}, what is it?",
        f"Calculate the logarithm of {x} with base {base}",
        f"The result of logarithm of {x} to the base {base}",
        f"The value of log({x}, {base})",
        f"The value of log base {base} for {x}",
        f"The logarithm of {x} with base {base}, equals?",
        f"Taking the logarithm of {x} with base {base}",
        f"Logarithm of {x} with base {base}, the answer?",
        f"The logarithm of {x} in base {base}, find it",
        f"The result of log({x}, {base})",
        f"Let's find the logarithm of {x} to the base {base}",
        f"Logarithm calculation: log({x}, {base})",
        f"Find the value of log({x}, {base})",
        f"{x} and {base}, their logarithm?",
        f"The value of log({x}, {base}), result is",
        f"The outcome when taking the logarithm of {x} with base {base}",
        f"The logarithm of {x} in base {base}, in decimal",
        f"The logarithm of {x} in base {base}, the outcome?",
        f"The logarithm of {x} with base {base}, what will you get?",
        f"Logarithm calculation: log({x}, {base}), what is it?",
        f"The value of log base {base} for {x}, result?",
        f"The logarithm of {x} to the base {base}, the value?",
        f"The logarithm of {x} with base {base}, the value left?",
        f"Calculating the value of log({x}, {base})",
        f"Finding the result of log({x}, {base})",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_logarithm_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
