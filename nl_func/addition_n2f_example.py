import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_addition_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_integer()
        num2 = RandomValueGenerator.generate_random_integer()
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2, (None if identifier is None else identifier+i)),
                "outputStr": f"##addition({num1},{num2})",
            }
        )
    return examples


def __random_explanation(a: int, b: int, identifier: int | None) -> str:
    explanations = [
        f"Adding {a} to {b}",
        f"{a} plus {b}",
        f"Summing {a} and {b}",
        f"The result of {a} plus {b}",
        f"{a} plus {b}, what is it",
        f"Calculation: {a} + {b}",
        f"{a} plus {b}, equals",
        f"Summing up {a} with {b}",
        f"{a} combined with {b}",
        f"The sum of {a} and {b}",
        f"{a} plus {b} is",
        f"{a} plus {b} is equal to",
        f"{a} added to {b}",
        f"{a} plus {b}, what does it give",
        f"{a} and {b} added together",
        f"{a} + {b}, the result",
        f"{a} summed with {b}",
        f"Calculate the sum of {a} and {b}",
        f"The total when you add {a} to {b}",
        f"{a} plus {b}, find the answer",
        f"Sum: {a} + {b}",
        f"Let's add {a} and {b}",
        f"Find the sum of {a} and {b}",
        f"{a} and {b}, their sum",
        f"{a} plus {b}, result is",
        f"{a} and {b}, what will be the sum",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_addition_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
