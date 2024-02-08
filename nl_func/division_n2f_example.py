import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_division_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        num2 = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i+1))
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2, (None if identifier is None else identifier+i)),
                "outputStr": f"##division({num1},{num2})",
            }
        )
    return examples


def __random_explanation(f1: float, f2: float, identifier: int | None) -> str:
    explanations = [
        f"Dividing {f1} by {f2}",
        f"{f1} divided by {f2}",
        f"{f1} over {f2}",
        f"The result of {f1} divided by {f2}",
        f"Calculation: {f1} / {f2}",
        f"Taking {f1} and dividing by {f2}",
        f"{f1} divided by {f2}, the answer",
        f"{f1} and {f2} division",
        f"The division of {f1} and {f2}",
        f"{f1} divided by {f2} is",
        f"{f1} and {f2} divided, the result",
        f"{f1} divided by {f2}, find the result",
        f"Quotient: {f1} / {f2}",
        f"Let's divide {f1} by {f2}",
        f"Find the result of {f1} divided by {f2}",
        f"{f1} and {f2}, their division",
        f"{f1} divided by {f2}, result is",
        f"{f1} and {f2}, what will be the quotient",
        f"Division: {f1} / {f2}",
        f"{f1} divided by {f2}, result",
        f"{f1} separated into {f2} parts",
        f"{f1} distributed over {f2}",
        f"{f1} split into {f2} groups",
        f"The result when {f1} is divided by {f2}",
        f"{f1} divided by {f2}, in decimal",
        f"The quotient when {f1} is divided by {f2}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_division_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
