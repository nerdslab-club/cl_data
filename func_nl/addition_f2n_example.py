import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_addition_example(count: int, identifier: int | None, seed: int):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_integer(seed=seed)
        num2 = RandomValueGenerator.generate_random_integer(seed=seed+1)
        examples.append(
            {
                "inputStr": f"##addition({num1},{num2})",
                "outputStr": __random_explanation(num1, num2, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation(x: int, y: int, identifier: int | None) -> str:
    explanations = [
        f"Adding {x} plus {y}",
        f"{x} + {y}",
        f"Summing {x} with {y}",
        f"{x} combined with {y}",

        f"The result of adding {x} and {y}",
        f"The sum of {x} and {y}",
        f"The total of {x} and {y}",
        f"Calculation: {x} + {y}",
        f"{x} plus {y} is",
        f"Summing up {x} and {y}",
        f"Sum: {x} + {y}",
        f"{x} and {y} added together",
        f"{x} + {y} results in",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_addition_example(2, None), TaskTypes.FUNC_TO_NL_TRANSLATION, 10, 15
        )
    )
