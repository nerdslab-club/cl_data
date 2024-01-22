import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_cube_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-10.0, 10.0)
        examples.append(
            {
                "inputStr": f"##cube({x})",
                "outputStr": __random_explanation_cube(x),
            }
        )
    return examples


def __random_explanation_cube(x: float) -> str:
    explanations = [
        f"The cube of the number {x}",
        f"cube({x})",
        f"The result of cubing {x}",
        f"Calculation: cube({x})",
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
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_cube_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
