import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_modulus_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i))
        num2 = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i+1))
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2, (None if identifier is None else identifier+i)),
                "outputStr": f"##modulus({num1},{num2})",
            }
        )
    return examples


def __random_explanation(a: int, b: int, identifier: int | None) -> str:
    explanations = [
        f"The remainder when {a} is divided by {b}",
        f"Finding the modulus of {a} divided by {b}",
        f"The modulus of {a} when divided by {b}",
        f"Calculate the remainder when {a} is divided by {b}",
        f"The number {a} mod {b}",
        f"The result of {a} modulo {b}",
        f"Calculation: {a} % {b}",
        f"The remaining value when {a} is divided by {b}",
        f"The result when {a} modulo {b}",
        f"Let's find the remainder when {a} is divided by {b}",
        f"Find the modulus of {a} divided by {b}",
        f"{a} divided by {b}, what is the leftover",
        f"The value of {a} modulo {b}",
        f"{a} modulo {b}, result is",
        f"The outcome when {a} is divided by {b}, the remainder",
        f"The remainder when {a} is divided by {b}, in numbers",
        f"The modulus of {a} divided by {b}, the outcome",
        f"{a} divided by {b}, what's left",
        f"The result when {a} is divided by {b}, the remainder",
        f"{a} divided by {b}, the remainder",
        f"{a} divided into {b} parts, what remains",
        f"The value left after {a} is divided by {b}",
        f"The value remaining when {a} is divided by {b}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_modulus_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
