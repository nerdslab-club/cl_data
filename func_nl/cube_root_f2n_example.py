import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_cube_root_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_float()
        examples.append(
            {
                "inputStr": f"##cube_root({x})",
                "outputStr": __random_explanation_cube_root(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_cube_root(x: float, identifier: int | None) -> str:
    explanations = [
        f"The cube root of the number {x}",
        f"The result of finding the cube root of {x}",
        f"Calculation: cube_root({x})",
        f"The value obtained by taking the cube root of {x}",
        f"The outcome of calculating the cube root of {x}",
        f"The cube root value of {x}",
        f"The result of finding the cube root of the number {x}",
        f"The computed result of finding the cube root of {x}",
        f"The value of {x} under the cube root",
        f"The cube root of the quantity {x}",
        f"The cube root result of the number {x}",
        f"The outcome of evaluating cube_root({x})",
        f"The value calculated by taking the cube root of {x} is",
        f"The result of evaluating the cube root of {x} is",
        f"The value of the number {x} under the cube root is",
        f"The computed cube root of {x} is",
        f"The calculated value of the cube root of {x} is",
        f"The outcome of finding the cube root value of {x} is",
        f"The value obtained by finding the cube root of {x} is",
        f"The result of taking the cube root of {x} is",
        f"The computed outcome of evaluating cube_root({x}) is",
        f"The value of {x} under the cube root is",
        f"The computed value of cube_root({x}) is",
        f"The calculated result of finding the cube root of {x} is",
        f"The cube root value of {x} is",
        f"The result of finding the cube root of the number {x} is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_cube_root_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
