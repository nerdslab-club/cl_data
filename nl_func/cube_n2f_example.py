import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_cube_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_float()
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##cube({num})",
        })
    return examples


def __random_explanation(f1: float, identifier: int | None) -> str:
    explanations = [
        f"Calculate the cube of the number {f1}",
        f"Find the cube value for the number {f1}",
        f"The result of cubing the number {f1}",
        f"Performing the cube operation on the number {f1}",
        f"The cube of the number {f1}",
        f"The result after cubing the number {f1}, what is it",
        f"The cube value of {f1}, what does it give",
        f"Let's find the cube value of {f1}",
        f"Cube the number {f1}, result is",
        f"Calculating the cube for the number {f1}",
        f"The cubed result after cubing the number {f1}",
        f"The cube of the number {f1}, what is its value",
        f"Let's determine the cube of the number {f1}",
        f"The cube value of {f1}",
        f"Cube {f1}, what is the result",
        f"The cube of the number {f1}, what does it give",
        f"Cube {f1} and provide the result",
        f"The cube value of {f1}, ignoring order",
        f"The result after cubing the number {f1}",
        f"The cube of the number {f1}, what is it",
        f"Calculate the cube for the number {f1}, find the answer",
        f"The cube value of {f1}, what does it give",
        f"Let's find the result after cubing the number {f1}",
        f"Cube {f1}, what is the output",
        f"The cubed result after cubing the number {f1}, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_cube_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
