import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_multiplication_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        num2 = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i+1))
        examples.append(
            {
                "inputStr": f"##multiplication({num1},{num2})",
                "outputStr": __random_explanation(num1, num2, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation(m: float, n: float, identifier: int | None) -> str:
    explanations = [
        f"Multiplying {m} with {n}",
        f"{m} * {n}",
        f"The result of multiplying {m} and {n}",
        f"{m} times {n} equals",
        f"{m} multiplied by {n}",
        f"The product of {m} and {n}",
        f"Calculation: {m} * {n}",
        f"The total when {m} is multiplied by {n}",
        f"{m} and {n} multiplied together",
        f"{m} * {n} results in",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    Utility.create_sample_from_example(
        create_f2n_multiplication_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
    )
