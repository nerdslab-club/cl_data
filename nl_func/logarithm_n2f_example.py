import random
import math

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_logarithm_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        base = RandomValueGenerator.generate_random_float(2, 10, round_to=1, seed=(None if identifier is None else identifier+i+1))
        examples.append(
            {
                "inputStr": __random_explanation(num, base, (None if identifier is None else identifier+i)),
                "outputStr": f"##logarithm({num},{base})",
            }
        )
    return examples


def __random_explanation(f1: float, base: float, identifier: int | None) -> str:
    explanations = [
        f"Finding the logarithm of {f1} to the base {base}",
        f"The logarithm of {f1} with base {base}",
        f"Logarithm of {f1} to the base {base}",
        f"Calculate the logarithm of {f1} with base {base}",
        f"The result of logarithm of {f1} to the base {base}",
        f"The value of log base {base} for {f1}",
        f"The logarithm of {f1} with base {base}, equals",
        f"Taking the logarithm of {f1} with base {base}",
        f"Logarithm of {f1} with base {base}, the answer",
        f"Let's find the logarithm of {f1} to the base {base}",
        f"{f1} and {base}, their logarithm",
        f"The outcome when taking the logarithm of {f1} with base {base}",
        f"The logarithm of {f1} in base {base}, in decimal",
        f"The logarithm of {f1} in base {base}, the outcome",
        f"The logarithm of {f1} with base {base}, what will you get",
        f"Logarithm calculation: log({f1}, {base}), what is it",
        f"The value of log base {base} for {f1}, result",
        f"The logarithm of {f1} to the base {base}, the value",
        f"The logarithm of {f1} with base {base}, the value left",
        f"Calculating the value of log({f1}, {base})",
        f"Finding the result of log({f1}, {base})",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_logarithm_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
