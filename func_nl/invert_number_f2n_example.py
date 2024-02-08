import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_invert_number_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        number = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        examples.append(
            {
                "inputStr": f"##invert_number({number})",
                "outputStr": __random_explanation_invert_number(number, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_invert_number(x: float, identifier: int | None) -> str:
    explanations = [
        f"The multiplicative inverse of the number {x}",
        f"The result of calculating the reciprocal of the number {x}",
        f"The reciprocal value of the number {x}",
        f"The outcome of finding the multiplicative inverse of the number {x}",
        f"The number that, when multiplied by {x}, results in 1",
        f"The result of determining the inverse of the number {x}",
        f"The value that, when multiplied by {x}, equals 1",
        f"The value obtained by finding the reciprocal of the number {x}",
        f"The value that, when multiplied by {x}, gives the result 1",
        f"The computed reciprocal value of the number {x}",
        f"The value that, when multiplied by {x}, gives the outcome 1",
        f"The calculated result of determining the multiplicative inverse of the number {x}",
        f"The reciprocal number for the given number {x}",
        f"The result obtained from calculating the reciprocal of the number {x}",
        f"The computed value of the multiplicative inverse of the number {x}",
        f"The reciprocal of the number {x} is",
        f"The result derived from calculating the reciprocal of the number {x}",
        f"The computed inverse value of the number {x}",
        f"The calculated outcome of evaluating invert_number({x})",
        f"The reciprocal fraction for the number {x}",
        f"The calculated inverse value of the number {x}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_invert_number_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
