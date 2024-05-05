import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_division_example(count: int, identifier: int | None, seed: int):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_float(seed=seed)
        num2 = RandomValueGenerator.generate_random_float(0.1, num1, seed=seed+1)  # To ensure no division by zero
        examples.append(
            {
                "inputStr": f"##division({num1},{num2})",
                "outputStr": __random_explanation(
                    num1,
                    num2, 
                    (None if identifier is None else identifier+i)
                ),
            }
        )
    return examples


def __random_explanation(x: float, y: float, identifier: int | None) -> str:
    explanations = [
        f"dividing {x} by {y}",
        f"{x} / {y}",
        f"{x} over {y}",
        f"The result of dividing {x} by {y}",

        f"{x} divided by {y} equals",
        f"The quotient of {x} and {y}",
        f"{x} divided by {y} results in",
        f"Calculation: {x} / {y}",
        f"{x} divided by {y}",
        f"{x} divided by {y} gives",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_division_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
