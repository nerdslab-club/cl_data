import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_is_perfect_cube_example(count: int):
    examples = []
    for _ in range(count):
        x = random.randint(1, 100)
        is_perfect_cube_result = round(x ** (1 / 3)) ** 3 == x
        examples.append(
            {
                "inputStr": f"##is_perfect_cube({x})",
                "outputStr": __random_explanation_is_perfect_cube(
                    x, is_perfect_cube_result
                ),
            }
        )
    return examples


def __random_explanation_is_perfect_cube(x: int, is_perfect_cube_result: bool) -> str:
    cube_str = "a perfect cube" if is_perfect_cube_result else "not a perfect cube"
    explanations = [
        f"Whether {x} is {cube_str}",
        f"is_perfect_cube({x})",
        f"Checking if {x} is a perfect cube",
        f"Calculation: is_perfect_cube({x})",
        f"Whether the integer {x} is a perfect cube",
        f"Determining if the value {x} is a perfect cube",
        f"Verifying if {x} is {cube_str}",
        f"Finding if {x} is a perfect cube number",
        f"Checking if the number {x} is a perfect cube",
        f"Whether {x} is a number that can be cubed",
        f"Whether {x} is a perfect cube or not",
        f"Checking if the value {x} can be cubed",
        f"Checking if the integer {x} is {cube_str}",
        f"Finding whether {x} is {cube_str}",
        f"Verifying whether {x} is a perfect cube or not",
        f"Determining if {x} is a number that can be cubed",
        f"The outcome of evaluating is_perfect_cube({x}) is",
        f"Checking if {x} is {cube_str} is",
        f"The boolean result of checking if {x} is {cube_str}",
        f"The result of checking if the integer {x} is {cube_str} is",
        f"The boolean outcome of the is_perfect_cube({x}) calculation is",
        f"Verifying if {x} is a number that can be cubed is",
        f"The boolean value indicating if {x} is {cube_str} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_is_perfect_cube_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
