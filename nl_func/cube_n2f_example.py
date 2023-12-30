import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_cube_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_float(1.0, 10.0)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##cube({num})",
        })
    return examples


def __random_explanation(x: float) -> str:
    explanations = [
        f"Calculate the cube of the number {x}",
        f"CUBE({x})",
        f"Find the cube value for the number {x}",
        f"The result of cubing the number {x}",
        f"Performing the cube operation on the number {x}",
        f"The cube of the number {x}",
        f"CUBE calculation: {x}",
        f"The result after cubing the number {x}, what is it?",
        f"The cube value of {x}, what does it give?",
        f"Let's find the cube value of {x}",
        f"Cube the number {x}, result is",
        f"Calculating the cube for the number {x}",
        f"The cubed result after cubing the number {x}",
        f"The cube of the number {x}, what is its value?",
        f"Let's determine the cube of the number {x}",
        f"The cube value of {x}",
        f"Cube {x}, what is the result?",
        f"The cube of the number {x}, what does it give?",
        f"Cube {x} and provide the result",
        f"CUBE({x}), what does it yield?",
        f"The cube value of {x}, ignoring order",
        f"The result after cubing the number {x}",
        f"The cube of the number {x}, what is it?",
        f"Calculate the cube for the number {x}, find the answer",
        f"The cube value of {x}, what does it give?",
        f"Let's find the result after cubing the number {x}",
        f"Cube {x}, what is the output?",
        f"The cubed result after cubing the number {x}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_cube_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
