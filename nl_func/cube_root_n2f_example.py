import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_cube_root_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##cube_root({num})",
        })
    return examples


def __random_explanation(f1: float, identifier: int | None) -> str:
    explanations = [
        f"Calculate the cube root of the number {f1}",
        f"Find the cube root value for the number {f1}",
        f"The result of taking the cube root of {f1}",
        f"Performing the cube root operation on the number {f1}",
        f"The cube root of the number {f1}",
        f"Let's find the cube root value of {f1}",
        f"Cube root of {f1}, result is",
        f"Calculating the cube root for the number {f1}",
        f"The cube root result after taking the cube root of {f1}",
        f"Let's determine the cube root of the number {f1}",
        f"The cube root value of {f1}",
        f"Cube root {f1} and provide the result",
        f"The result after taking the cube root of {f1}",
        f"Calculate the cube root for the number {f1}, find the answer",
        f"Let's find the result after taking the cube root of {f1}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_cube_root_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
