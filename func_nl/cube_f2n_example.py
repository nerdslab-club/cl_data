import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_cube_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i+1))
        examples.append(
            {
                "inputStr": f"##cube({x})",
                "outputStr": __random_explanation_cube(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_cube(x: float, identifier: int | None) -> str:
    explanations = [
        f"The cube of the number {x}",
        f"The result of cubing {x}",
        f"The value obtained by raising {x} to the power of 3",
        f"The outcome of calculating the cube of {x}",
        f"The cubed value of {x}",
        f"The result of cubing the number {x}",
        f"The computed result of cubing {x}",
        f"The value of {x} cubed",
        f"The product of {x} raised to the power of 3",
        f"The cubed result of the number {x}",
        f"The outcome of finding the cube of {x}",
        f"The computed value of cube({x}) is",
        f"The value obtained by raising {x} to the power of 3 is",
        f"The result of evaluating the cube of {x} is",
        f"The computed result of {x} cubed is",
        f"The calculated value of raising {x} to the power of 3 is",
        f"The outcome of finding the cubed value of {x} is",
        f"The value obtained by raising {x} to the power of 3 is",
        f"The result of {x} raised to the power of 3 is",
        f"The outcome of evaluating cube({x}) is",
        f"The value of {x} cubed is",
        f"The computed outcome of cubing {x} is",
        f"The calculated result of {x} raised to the power of 3 is",
        f"The cubed value of {x} is",
        f"The result of cubing the number {x} is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_cube_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
